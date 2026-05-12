"""
Demo script — runs several example queries to showcase the agent.
Requires ANTHROPIC_API_KEY to be set.
"""

import os
import sys

try:
    from rich.console import Console
    from rich.rule import Rule
    console = Console()
    def section(title): console.print(Rule(f"[bold cyan]{title}[/bold cyan]"))
    def info(msg): console.print(f"[dim]{msg}[/dim]")
    def result(msg): console.print(msg)
except ImportError:
    def section(title): print(f"\n{'='*60}\n{title}\n{'='*60}")
    def info(msg): print(msg)
    def result(msg): print(msg)

from src.agent import RegulatoryComplianceAgent

DEMO_QUERIES = [
    {
        "title": "UAE Real Estate — Emaar Properties",
        "company": "Emaar Properties",
        "region": "UAE",
        "sector": "Real Estate",
    },
    {
        "title": "KSA BFSI — Al Rajhi Bank",
        "company": "Al Rajhi Bank",
        "region": "KSA",
        "sector": "BFSI",
    },
    {
        "title": "Both Regions — First Abu Dhabi Bank (FAB)",
        "company": "First Abu Dhabi Bank",
        "region": "Both",
        "sector": "BFSI",
    },
]


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY not set.")
        sys.exit(1)

    agent = RegulatoryComplianceAgent(api_key=api_key)

    section("Regulatory Compliance AI Agent — Demo")
    info(f"Running {len(DEMO_QUERIES)} demo queries...\n")

    for i, demo in enumerate(DEMO_QUERIES, 1):
        section(f"Demo {i}: {demo['title']}")
        info(f"Company: {demo['company']} | Region: {demo['region']} | Sector: {demo['sector']}")
        info("Processing...\n")

        # Reset per query so each is independent
        agent.reset()

        response = agent.lookup_company(
            demo["company"],
            region=demo["region"],
            sector=demo["sector"],
        )
        result(response)
        print()

    section("Demo Complete")
    info("Run 'python main.py' for interactive mode.")


if __name__ == "__main__":
    main()
