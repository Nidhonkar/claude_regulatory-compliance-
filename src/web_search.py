"""
Web search functionality using DuckDuckGo (no API key required).
Used by the agent to fetch live regulatory news and updates.
"""

from ddgs import DDGS


def search_web(query: str, max_results: int = 5) -> list[dict]:
    """
    Search the web using DuckDuckGo and return structured results.

    Returns a list of dicts with keys: title, href, body
    Falls back to an empty list on any error so the agent can still
    answer from the static knowledge base.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        return results
    except Exception:
        return []


def format_search_results(results: list[dict]) -> str:
    """Format raw DuckDuckGo results into a readable string for the agent."""
    if not results:
        return "No web results found. Using static knowledge base only."

    lines = [f"Web Search Results ({len(results)} found):", "=" * 50]
    for i, r in enumerate(results, 1):
        title = r.get("title", "No title")
        url = r.get("href", "")
        snippet = r.get("body", "No description available.")
        lines.append(f"\n[{i}] {title}")
        lines.append(f"    URL: {url}")
        lines.append(f"    {snippet}")

    return "\n".join(lines)
