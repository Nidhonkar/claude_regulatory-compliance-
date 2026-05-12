"""
Regulatory Compliance AI Agent — CLI Entry Point

Usage:
    # Interactive mode
    python main.py

    # Direct lookup
    python main.py --company "Emaar Properties" --region UAE
    python main.py --company "Al Rajhi Bank" --region KSA --sector BFSI
    python main.py --company "First Abu Dhabi Bank" --region Both
"""

import argparse
import sys
import os

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.prompt import Prompt
    from rich.text import Text
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

from src.agent import RegulatoryComplianceAgent

console = Console() if RICH_AVAILABLE else None


def print_header():
    if RICH_AVAILABLE:
        console.print(Panel(
            Text("🏛  Regulatory Compliance AI Agent", justify="center", style="bold cyan"),
            subtitle="UAE & KSA | Real Estate & BFSI Sectors",
            style="cyan",
        ))
        console.print()
    else:
        print("=" * 60)
        print("  Regulatory Compliance AI Agent")
        print("  UAE & KSA | Real Estate & BFSI Sectors")
        print("=" * 60)
        print()


def print_response(response: str):
    if RICH_AVAILABLE:
        console.print(Panel(
            Markdown(response),
            title="[bold green]Compliance Report[/bold green]",
            border_style="green",
        ))
    else:
        print("\n" + "=" * 60)
        print("COMPLIANCE REPORT")
        print("=" * 60)
        print(response)
        print("=" * 60)


def print_error(msg: str):
    if RICH_AVAILABLE:
        console.print(f"[bold red]Error:[/bold red] {msg}")
    else:
        print(f"Error: {msg}")


def print_info(msg: str):
    if RICH_AVAILABLE:
        console.print(f"[dim]{msg}[/dim]")
    else:
        print(msg)


def run_interactive(agent: RegulatoryComplianceAgent):
    """Run the agent in interactive chat mode."""
    print_header()

    if RICH_AVAILABLE:
        console.print(
            "[bold yellow]Interactive Mode[/bold yellow] — "
            "Ask about any company in Real Estate or BFSI sector operating in UAE/KSA.\n"
            "Type [bold]'exit'[/bold] or [bold]'quit'[/bold] to leave. "
            "Type [bold]'reset'[/bold] to start a new conversation.\n"
        )
        console.print("[dim]Examples:[/dim]")
        console.print("  • What are the compliance requirements for Emaar Properties in UAE?")
        console.print("  • Tell me about Al Rajhi Bank's regulatory obligations in KSA")
        console.print("  • Compare regulations for BFSI sector in UAE vs KSA")
        console.print()
    else:
        print("Interactive Mode - Ask about companies in Real Estate or BFSI (UAE/KSA)")
        print("Type 'exit' or 'quit' to leave. Type 'reset' to start a new conversation.")
        print()

    while True:
        try:
            if RICH_AVAILABLE:
                user_input = Prompt.ask("[bold blue]You[/bold blue]").strip()
            else:
                user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit", "q"):
            print("\nGoodbye!")
            break

        if user_input.lower() == "reset":
            agent.reset()
            print_info("Conversation history cleared. Starting fresh.\n")
            continue

        print_info("\nAnalysing... (this may take a few seconds)\n")
        try:
            response = agent.query(user_input)
            print_response(response)
        except Exception as e:
            err = str(e).lower()
            if "api_key" in err or "permission" in err or "auth" in err:
                print_error("Invalid API key. Check GEMINI_API_KEY in your .env file.")
            elif "quota" in err or "rate" in err:
                print_error("Rate limit reached. Please wait a moment and try again.")
            elif "connect" in err or "network" in err:
                print_error("Could not connect to Google API. Check your internet connection.")
            else:
                print_error(f"Unexpected error: {e}")

        print()


def run_direct(agent: RegulatoryComplianceAgent, company: str, region: str, sector: str | None):
    """Run a single direct company lookup."""
    print_header()

    sector_display = f" [{sector}]" if sector else ""
    print_info(f"Looking up: {company}{sector_display} — Region: {region}\n")

    try:
        response = agent.lookup_company(company, region=region, sector=sector)
        print_response(response)
    except Exception as e:
        err = str(e).lower()
        if "api_key" in err or "permission" in err or "auth" in err:
            print_error("Invalid API key. Check GEMINI_API_KEY in your .env file.")
        else:
            print_error(f"Unexpected error: {e}")
        sys.exit(1)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Regulatory Compliance AI Agent for UAE & KSA (Real Estate & BFSI)"
    )
    parser.add_argument(
        "--company", "-c",
        type=str,
        help="Company name to look up (e.g. 'Emaar Properties')",
    )
    parser.add_argument(
        "--region", "-r",
        type=str,
        choices=["UAE", "KSA", "Both"],
        default="Both",
        help="Region to check compliance for (default: Both)",
    )
    parser.add_argument(
        "--sector", "-s",
        type=str,
        choices=["Real Estate", "BFSI"],
        help="Sector hint (optional — agent will auto-detect if not provided)",
    )
    parser.add_argument(
        "--api-key",
        type=str,
        help="Anthropic API key (overrides ANTHROPIC_API_KEY env var)",
    )

    args = parser.parse_args()

    api_key = args.api_key or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print_error(
            "No API key found. Set GEMINI_API_KEY in your environment or .env file, "
            "or pass --api-key."
        )
        sys.exit(1)

    agent = RegulatoryComplianceAgent(api_key=api_key)

    if args.company:
        run_direct(agent, args.company, args.region, args.sector)
    else:
        run_interactive(agent)


if __name__ == "__main__":
    main()
