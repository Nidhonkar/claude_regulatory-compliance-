"""
Regulatory Compliance AI Agent

Uses Claude claude-opus-4-7 with tool use to answer queries about company information
and regulatory compliance requirements for UAE and KSA in the Real Estate
and BFSI sectors.
"""

import os
import anthropic
from dotenv import load_dotenv

from .tools import TOOLS, execute_tool

load_dotenv()

SYSTEM_PROMPT = """You are an expert regulatory compliance advisor specialising in the
UAE and KSA (Kingdom of Saudi Arabia) markets, with deep expertise in two sectors:

1. **Real Estate** – property development, brokerage, leasing, REITs, PropTech
2. **BFSI** – Banking, Financial Services & Insurance (including Islamic Finance/FinTech)

When a user provides a company name, you must:
- Identify the company's sector (Real Estate or BFSI)
- Use the available tools to retrieve company information and regulatory requirements
- Present a structured, actionable compliance report covering:
  • Primary regulatory bodies they must engage with
  • Key legislation applicable to their operations
  • Specific compliance requirements they must meet
  • Recent regulatory updates relevant to their business

Always use the tools to gather information before responding. Be specific, structured,
and practical. If a company could operate in both UAE and KSA, cover both jurisdictions.

When presenting compliance information:
- Prioritise the most critical compliance requirements
- Flag any high-risk areas (AML, licensing, capital requirements)
- Note recent changes that may require immediate attention
- Provide actionable next steps where appropriate

You must always call at least the get_company_information and get_regulatory_compliance
tools before providing your final answer."""


class RegulatoryComplianceAgent:
    """AI Agent for regulatory compliance queries in UAE and KSA."""

    def __init__(self, api_key: str | None = None):
        self.client = anthropic.Anthropic(
            api_key=api_key or os.environ.get("ANTHROPIC_API_KEY")
        )
        self.model = "claude-opus-4-7"
        self.conversation_history: list[dict] = []

    def query(self, user_message: str) -> str:
        """
        Process a user query about a company's regulatory compliance.

        Runs the agentic tool-use loop until Claude produces a final answer.
        """
        self.conversation_history.append(
            {"role": "user", "content": user_message}
        )

        while True:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=8192,
                system=SYSTEM_PROMPT,
                thinking={"type": "adaptive"},
                tools=TOOLS,
                messages=self.conversation_history,
            )

            # Append the full assistant response to history
            self.conversation_history.append(
                {"role": "assistant", "content": response.content}
            )

            if response.stop_reason == "end_turn":
                # Extract the final text response
                final_text = ""
                for block in response.content:
                    if hasattr(block, "type") and block.type == "text":
                        final_text += block.text
                return final_text

            if response.stop_reason == "tool_use":
                tool_results = []
                for block in response.content:
                    if hasattr(block, "type") and block.type == "tool_use":
                        result = execute_tool(block.name, block.input)
                        tool_results.append(
                            {
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": result,
                            }
                        )

                if tool_results:
                    self.conversation_history.append(
                        {"role": "user", "content": tool_results}
                    )
                continue

            # Unexpected stop reason — return whatever text exists
            final_text = ""
            for block in response.content:
                if hasattr(block, "type") and block.type == "text":
                    final_text += block.text
            return final_text or "No response generated."

    def reset(self):
        """Clear conversation history to start a fresh session."""
        self.conversation_history = []

    def lookup_company(
        self,
        company_name: str,
        region: str = "Both",
        sector: str | None = None,
    ) -> str:
        """
        Convenience method: look up a company's compliance profile directly.

        Args:
            company_name: Name of the company (e.g. "Emaar Properties")
            region: "UAE", "KSA", or "Both"
            sector: Optional hint — "Real Estate", "BFSI", or None to auto-detect
        """
        sector_part = f" in the {sector} sector" if sector else ""
        region_part = f"for {region}" if region != "Both" else "for both UAE and KSA"

        message = (
            f"Please provide a complete regulatory compliance profile for "
            f"'{company_name}'{sector_part} operating {region_part}. "
            f"Include company information, applicable regulations, compliance "
            f"requirements, and any recent regulatory changes I should be aware of."
        )
        return self.query(message)
