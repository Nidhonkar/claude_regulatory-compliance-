"""
Regulatory Compliance AI Agent — powered by Google Gemini (free tier).

Uses Gemini 2.0 Flash with function calling to answer queries about company
regulatory compliance in UAE and KSA (Real Estate & BFSI sectors).
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv

from .tools import execute_tool

load_dotenv()

SYSTEM_PROMPT = """You are an expert regulatory compliance advisor specialising in the
UAE and KSA (Kingdom of Saudi Arabia) markets, with deep expertise in two sectors:

1. Real Estate - property development, brokerage, leasing, REITs, PropTech
2. BFSI - Banking, Financial Services and Insurance (including Islamic Finance and FinTech)

You have access to both a static regulatory knowledge base AND live web search.

When a user provides a company name, you MUST follow this sequence:
1. Call get_company_information to identify the company's sector and operations
2. Call get_regulatory_compliance to retrieve the full static compliance requirements
3. Call web_search at least once to find the latest regulatory news and updates
4. Optionally call compare_regulations if the user asks for a UAE vs KSA comparison

Then present a structured, actionable compliance report covering:
  - Primary regulatory bodies they must engage with
  - Key legislation applicable to their operations
  - Specific compliance requirements they must meet
  - Recent regulatory updates from both static data and live web search
  - Actionable next steps

When presenting compliance information:
- Clearly distinguish between established requirements and recent updates
- Flag any high-risk areas such as AML, licensing, and capital requirements
- Note recent changes from web search that may require immediate attention
- Be specific, structured, and practical"""

# Tool definitions in Gemini's function-calling format
GEMINI_TOOLS = [
    {
        "function_declarations": [
            {
                "name": "get_company_information",
                "description": (
                    "Retrieve general information about a company operating in the "
                    "Real Estate or BFSI sector. Provides company overview, key operations, "
                    "market presence, and sector classification."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "company_name": {
                            "type": "string",
                            "description": "The full or common name of the company to look up.",
                        },
                        "sector": {
                            "type": "string",
                            "enum": ["Real Estate", "BFSI", "Unknown"],
                            "description": "The sector the company operates in.",
                        },
                    },
                    "required": ["company_name", "sector"],
                },
            },
            {
                "name": "get_regulatory_compliance",
                "description": (
                    "Retrieve detailed regulatory compliance requirements for a company "
                    "based on its sector and operating region. Returns primary regulators, "
                    "key legislation, compliance requirements, and recent updates."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "company_name": {
                            "type": "string",
                            "description": "Name of the company.",
                        },
                        "sector": {
                            "type": "string",
                            "enum": ["Real Estate", "BFSI"],
                            "description": "The sector the company operates in.",
                        },
                        "region": {
                            "type": "string",
                            "enum": ["UAE", "KSA", "Both"],
                            "description": "The region for compliance requirements.",
                        },
                    },
                    "required": ["company_name", "sector", "region"],
                },
            },
            {
                "name": "web_search",
                "description": (
                    "Search the internet for the latest regulatory news and updates "
                    "related to a company, sector, or regulatory body in UAE or KSA. "
                    "Use this to find recent regulatory changes and enforcement actions."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": (
                                "Search query. Be specific — include company name, "
                                "region, and topic. Example: 'Emaar Properties RERA compliance 2025'."
                            ),
                        },
                        "max_results": {
                            "type": "integer",
                            "description": "Number of results to return (1-10). Default is 5.",
                        },
                    },
                    "required": ["query"],
                },
            },
            {
                "name": "compare_regulations",
                "description": (
                    "Compare regulatory requirements between UAE and KSA for a specific sector. "
                    "Highlights key similarities, differences, and cross-border considerations."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sector": {
                            "type": "string",
                            "enum": ["Real Estate", "BFSI"],
                            "description": "The sector to compare regulations for.",
                        },
                    },
                    "required": ["sector"],
                },
            },
        ]
    }
]


class RegulatoryComplianceAgent:
    """AI Agent for regulatory compliance queries using Google Gemini (free)."""

    def __init__(self, api_key: str | None = None):
        key = api_key or os.environ.get("GEMINI_API_KEY")
        genai.configure(api_key=key)
        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            tools=GEMINI_TOOLS,
            system_instruction=SYSTEM_PROMPT,
        )
        self.chat = self.model.start_chat()

    def query(self, user_message: str) -> str:
        """
        Process a user query with Gemini's function-calling loop.
        Keeps calling tools until Gemini produces a final text response.
        """
        response = self.chat.send_message(user_message)

        while True:
            # Collect any function calls in this response
            function_calls = [
                part.function_call
                for part in response.parts
                if hasattr(part, "function_call") and part.function_call.name
            ]

            if not function_calls:
                # No tool calls — extract and return final text
                return "".join(
                    part.text for part in response.parts if hasattr(part, "text")
                )

            # Execute each tool and collect results
            tool_results = []
            for fc in function_calls:
                result = execute_tool(fc.name, dict(fc.args))
                tool_results.append(
                    genai.protos.Part(
                        function_response=genai.protos.FunctionResponse(
                            name=fc.name,
                            response={"output": result},
                        )
                    )
                )

            # Send all tool results back to Gemini
            response = self.chat.send_message(tool_results)

    def reset(self):
        """Start a fresh conversation."""
        self.chat = self.model.start_chat()

    def lookup_company(
        self,
        company_name: str,
        region: str = "Both",
        sector: str | None = None,
    ) -> str:
        """Convenience method: look up a company's compliance profile directly."""
        sector_part = f" in the {sector} sector" if sector else ""
        region_part = f"for {region}" if region != "Both" else "for both UAE and KSA"

        message = (
            f"Please provide a complete regulatory compliance profile for "
            f"'{company_name}'{sector_part} operating {region_part}. "
            f"Include company information, applicable regulations, compliance "
            f"requirements, and any recent regulatory changes I should be aware of."
        )
        return self.query(message)
