"""
Tool definitions for the regulatory compliance agent.
"""

from .regulatory_data import get_regulatory_requirements, get_sector_for_company

TOOLS = [
    {
        "name": "get_company_information",
        "description": (
            "Retrieve general information about a company operating in the "
            "Real Estate or BFSI (Banking, Financial Services & Insurance) sector. "
            "Provides company overview, key operations, market presence, and sector classification."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "company_name": {
                    "type": "string",
                    "description": "The full or common name of the company to look up.",
                },
                "sector": {
                    "type": "string",
                    "enum": ["Real Estate", "BFSI", "Unknown"],
                    "description": (
                        "The sector the company operates in. Use 'Unknown' if unclear from "
                        "the company name and context alone."
                    ),
                },
            },
            "required": ["company_name", "sector"],
        },
    },
    {
        "name": "get_regulatory_compliance",
        "description": (
            "Retrieve the detailed regulatory compliance requirements that a company must follow "
            "based on its sector (Real Estate or BFSI) and operating region (UAE or KSA). "
            "Returns primary regulators, key legislation, compliance requirements, and recent updates."
        ),
        "input_schema": {
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
                    "description": (
                        "The region for which compliance requirements are needed. "
                        "Use 'Both' if the company operates in both UAE and KSA."
                    ),
                },
            },
            "required": ["company_name", "sector", "region"],
        },
    },
    {
        "name": "compare_regulations",
        "description": (
            "Compare regulatory requirements between UAE and KSA for a specific sector. "
            "Highlights key similarities, differences, and cross-border operational considerations."
        ),
        "input_schema": {
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


def execute_tool(tool_name: str, tool_input: dict) -> str:
    """Execute a tool call and return the result as a string."""
    if tool_name == "get_company_information":
        return _get_company_information(
            tool_input["company_name"], tool_input["sector"]
        )
    elif tool_name == "get_regulatory_compliance":
        return _get_regulatory_compliance(
            tool_input["company_name"],
            tool_input["sector"],
            tool_input["region"],
        )
    elif tool_name == "compare_regulations":
        return _compare_regulations(tool_input["sector"])
    else:
        return f"Unknown tool: {tool_name}"


def _get_company_information(company_name: str, sector: str) -> str:
    """Generate structured company information context."""
    resolved_sector = get_sector_for_company(company_name, sector)

    sector_display = "Real Estate" if resolved_sector == "REAL_ESTATE" else "BFSI"
    sector_desc = {
        "REAL_ESTATE": (
            "This company operates in the Real Estate sector, which encompasses property "
            "development, sales, leasing, brokerage, property management, and real estate "
            "investment. Companies in this sector are subject to property registration laws, "
            "anti-money laundering requirements, and sector-specific licensing by real estate "
            "regulatory authorities."
        ),
        "BFSI": (
            "This company operates in the Banking, Financial Services & Insurance (BFSI) sector, "
            "which includes banks, investment firms, insurance companies, payment processors, "
            "FinTechs, and asset managers. Companies in this sector are subject to central bank "
            "regulations, capital market authority rules, and strict AML/CFT requirements."
        ),
    }

    result = {
        "company_name": company_name,
        "identified_sector": sector_display,
        "sector_description": sector_desc.get(resolved_sector, ""),
        "note": (
            "The agent has identified the sector based on the company name and context provided. "
            "For accurate compliance guidance, please confirm the company's primary business activities."
        ),
        "typical_operations": _get_typical_operations(resolved_sector),
    }

    lines = [
        f"Company: {result['company_name']}",
        f"Sector: {result['identified_sector']}",
        f"",
        f"Sector Overview:",
        result["sector_description"],
        f"",
        f"Typical Operations:",
    ]
    for op in result["typical_operations"]:
        lines.append(f"  - {op}")
    lines.append(f"")
    lines.append(result["note"])

    return "\n".join(lines)


def _get_typical_operations(sector: str) -> list[str]:
    ops = {
        "REAL_ESTATE": [
            "Property development and construction",
            "Sales and leasing of residential/commercial properties",
            "Real estate brokerage and agency services",
            "Property management and facilities management",
            "Real estate investment and fund management (REITs)",
            "PropTech and digital real estate platforms",
        ],
        "BFSI": [
            "Retail and commercial banking",
            "Investment banking and capital markets",
            "Insurance underwriting and claims management",
            "Asset and wealth management",
            "Payment processing and digital finance (FinTech)",
            "Islamic banking and Takaful (in GCC context)",
        ],
    }
    return ops.get(sector, [])


def _get_regulatory_compliance(
    company_name: str, sector: str, region: str
) -> str:
    resolved_sector = get_sector_for_company(company_name, sector)
    regions = ["UAE", "KSA"] if region == "Both" else [region.upper()]

    output_parts = [
        f"Regulatory Compliance Requirements for: {company_name}",
        f"Sector: {'Real Estate' if resolved_sector == 'REAL_ESTATE' else 'BFSI'}",
        f"Region(s): {', '.join(regions)}",
        "=" * 60,
    ]

    for reg in regions:
        data = get_regulatory_requirements(reg, resolved_sector)
        if not data:
            output_parts.append(f"\n{reg}: No data available for this sector.")
            continue

        output_parts.append(f"\n{'=' * 20} {reg} {'=' * 20}")

        output_parts.append("\nPRIMARY REGULATORS:")
        for r in data.get("primary_regulators", []):
            output_parts.append(f"  • {r}")

        output_parts.append("\nKEY LEGISLATION:")
        for law in data.get("key_laws", []):
            output_parts.append(f"  • {law}")

        output_parts.append("\nCOMPLIANCE REQUIREMENTS:")
        for req in data.get("compliance_requirements", []):
            output_parts.append(f"  ✓ {req}")

        output_parts.append("\nRECENT REGULATORY UPDATES:")
        for update in data.get("recent_updates", []):
            output_parts.append(f"  ➤ {update}")

    return "\n".join(output_parts)


def _compare_regulations(sector: str) -> str:
    resolved_sector = get_sector_for_company("", sector)

    uae_data = get_regulatory_requirements("UAE", resolved_sector)
    ksa_data = get_regulatory_requirements("KSA", resolved_sector)

    sector_display = "Real Estate" if resolved_sector == "REAL_ESTATE" else "BFSI"

    uae_reqs = set(uae_data.get("compliance_requirements", []))
    ksa_reqs = set(ksa_data.get("compliance_requirements", []))

    common_themes = [
        "AML/CFT compliance (both follow FATF standards)",
        "KYC/CDD requirements for all transactions",
        "Licensing and registration with sector regulators",
        "Beneficial ownership disclosure",
        "Consumer/investor protection frameworks",
        "Islamic finance / Sharia-compliant product oversight",
        "Data protection obligations",
    ]

    output = [
        f"UAE vs KSA Regulatory Comparison: {sector_display} Sector",
        "=" * 60,
        "",
        "COMMON REGULATORY THEMES (Both UAE & KSA):",
    ]
    for theme in common_themes:
        output.append(f"  ✓ {theme}")

    output.extend([
        "",
        "UAE-SPECIFIC HIGHLIGHTS:",
        f"  • Regulators: {', '.join(uae_data.get('primary_regulators', [])[:2])}",
        "  • FATF Grey List removal (2024) - enhanced international standing",
        "  • DIFC/ADGM international financial centres (common law jurisdictions)",
        "  • Dubai Virtual Assets Regulatory Authority (VARA) for crypto",
        "  • Federal + Emirate-level dual regulatory structure",
        "  • Free zone regulations and 100% foreign ownership zones",
        "",
        "KSA-SPECIFIC HIGHLIGHTS:",
        f"  • Regulators: {', '.join(ksa_data.get('primary_regulators', [])[:2])}",
        "  • SAMA as dominant central regulator (merged insurance supervision)",
        "  • Vision 2030 Financial Sector Development Program (FSDP)",
        "  • Zakat obligations for Saudi nationals and entities",
        "  • Real Estate Transaction Tax (RETT) - 5% on property transfers",
        "  • Saudization (Nitaqat) workforce localisation requirements",
        "  • Personal Data Protection Law (PDPL) effective 2023-2024",
        "",
        "CROSS-BORDER OPERATIONAL CONSIDERATIONS:",
        "  • Companies operating in both must maintain separate compliance programmes",
        "  • Different tax regimes: UAE (VAT 5%) vs KSA (VAT 15%)",
        "  • GCC Unified AML framework applies to both",
        "  • Separate licensing in each jurisdiction required",
        "  • Data localisation requirements differ between UAE and KSA",
    ])

    return "\n".join(output)
