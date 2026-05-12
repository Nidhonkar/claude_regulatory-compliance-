"""
Static regulatory compliance knowledge base for UAE and KSA
across Real Estate and BFSI sectors.
"""

REGULATORY_FRAMEWORK = {
    "UAE": {
        "REAL_ESTATE": {
            "primary_regulators": [
                "Real Estate Regulatory Agency (RERA) - Dubai",
                "Department of Municipalities and Transport (DMT) - Abu Dhabi",
                "Ajman Real Estate Regulatory Agency (ARREA)",
                "Sharjah Real Estate Registration Department",
            ],
            "key_laws": [
                "Law No. 7 of 2006 - Property Ownership in Dubai",
                "Law No. 13 of 2008 - Interim Real Estate Register in Dubai",
                "Law No. 27 of 2007 - Ownership of Jointly Owned Properties (Strata Law)",
                "Federal Law No. 5 of 1985 - Civil Transactions Law (property provisions)",
                "Abu Dhabi Law No. 19 of 2005 - Property Ownership",
            ],
            "compliance_requirements": [
                "RERA registration for real estate brokers and agents (Broker Registration Certificate)",
                "Real Estate Developers must register all off-plan projects with RERA",
                "Mandatory escrow accounts for off-plan property sales",
                "Anti-Money Laundering (AML) compliance - Federal Decree-Law No. 20 of 2018",
                "Know Your Customer (KYC) procedures for all property transactions",
                "Beneficial Ownership Registration for corporate buyers",
                "VAT registration (if annual turnover exceeds AED 375,000) - 5% VAT on commercial property",
                "Real estate advertisements must comply with RERA standards",
                "Freehold zones designation compliance (e.g., Palm Jumeirah, Downtown Dubai)",
                "MOLLAK system registration for service charges in jointly owned properties",
                "Ejari registration for all tenancy contracts in Dubai",
                "Tawtheeq registration for tenancy contracts in Abu Dhabi",
            ],
            "recent_updates": [
                "Golden Visa for property investors (AED 2 million+ investment)",
                "Virtual Assets regulation affecting real estate tokenisation",
                "Increased foreign ownership zones across all Emirates",
                "Dubai Land Department (DLD) blockchain property registration",
            ],
        },
        "BFSI": {
            "primary_regulators": [
                "Central Bank of the UAE (CBUAE)",
                "Securities and Commodities Authority (SCA)",
                "Insurance Authority (IA) - merged into CBUAE",
                "Dubai Financial Services Authority (DFSA) - DIFC",
                "Financial Services Regulatory Authority (FSRA) - ADGM",
            ],
            "key_laws": [
                "Federal Decree-Law No. 14 of 2018 - Central Bank and Financial Sector",
                "Federal Law No. 4 of 2000 - Emirates Securities and Commodities Authority",
                "Federal Decree-Law No. 20 of 2018 - Anti-Money Laundering",
                "Federal Law No. 6 of 2007 - Insurance Authority",
                "Cabinet Resolution No. 10 of 2019 - Beneficial Ownership",
                "DIFC Law No. 1 of 2004 - Financial Services",
            ],
            "compliance_requirements": [
                "CBUAE licensing for banks, finance companies, exchange houses",
                "Basel III capital adequacy requirements (minimum CAR 13%)",
                "AML/CFT compliance - Federal Decree-Law No. 20 of 2018",
                "Customer Due Diligence (CDD) and Enhanced Due Diligence (EDD)",
                "Suspicious Transaction Reporting to UAE Financial Intelligence Unit (FIU/goAML)",
                "FATF Recommendations compliance (UAE removed from FATF Grey List in 2024)",
                "Data Protection - Federal Decree-Law No. 45 of 2021 (PDPL)",
                "Open Banking Framework compliance (CBUAE 2023)",
                "Digital Payment Token Service Provider regulations",
                "Consumer Protection Regulations (CBUAE 2020)",
                "Mortgage Cap regulations (80% LTV for expats, 85% for nationals on first property)",
                "SCA regulations for listed securities and investment funds",
                "Insurance companies: solvency margin requirements, actuarial certifications",
                "FinTech regulatory sandbox (CBUAE/DFSA/FSRA)",
                "Islamic Finance compliance for Sharia-compliant products",
            ],
            "recent_updates": [
                "CBUAE Open Finance Regulation 2023",
                "UAE removed from FATF Grey List (February 2024) - enhanced global access",
                "CBUAE Retail Payment Services & Card Schemes Regulations 2021",
                "Digital Bank licensing framework",
                "Crypto Asset regulations under CBUAE/SCA/VARA (Dubai)",
            ],
        },
    },
    "KSA": {
        "REAL_ESTATE": {
            "primary_regulators": [
                "Real Estate General Authority (REGA)",
                "Ministry of Municipal and Rural Affairs and Housing (MOMRAH)",
                "Saudi Central Bank (SAMA) - for real estate financing",
                "Capital Market Authority (CMA) - for REITs",
            ],
            "key_laws": [
                "Real Estate Regulation and Services Law (Royal Decree M/71 of 2017)",
                "Real Estate Development Fund Law",
                "Mortgage Law (Royal Decree M/49 of 2012)",
                "Foreign Ownership Law - Non-Saudis permitted in specific areas",
                "Waqf Property Regulations",
                "Subsurface Resources Law",
            ],
            "compliance_requirements": [
                "REGA licensing for real estate brokers, developers, and property managers",
                "Nafidh platform registration for all real estate professionals",
                "Aqarmap and Ejar platform compliance for rental contracts",
                "Certified Real Estate Broker (CREB) certification requirement",
                "AML/CFT compliance under Saudi AML Law and FATF standards",
                "KYC/CDD for all real estate transactions",
                "Beneficial Ownership disclosure for corporate transactions",
                "Zakat compliance for Saudi property owners (2.5% on eligible assets)",
                "VAT registration (15% VAT on commercial property transactions)",
                "Real Estate Transaction Tax (RETT) - 5% on residential transfers",
                "White Land Tax (WLT) - 2.5% annual on undeveloped urban land",
                "SAMA regulations for mortgage financing (maximum 90% LTV for first home)",
                "REIT compliance with CMA regulations for listed real estate funds",
                "Saudization (Nitaqat) requirements for real estate company workforce",
                "MOMRAH building codes and municipal permits",
            ],
            "recent_updates": [
                "Vision 2030 NEOM and mega-project compliance frameworks",
                "Real Estate Exchange (Tadawul) REIT expansion regulations",
                "Foreign investor real estate ownership expansion (2023)",
                "Digital real estate transaction platform (Ejar 2.0)",
                "Affordable housing programme compliance requirements",
            ],
        },
        "BFSI": {
            "primary_regulators": [
                "Saudi Central Bank (SAMA)",
                "Capital Market Authority (CMA)",
                "Insurance Authority (IA) - under SAMA",
                "Financial Sector Development Program (FSDP) - Vision 2030",
            ],
            "key_laws": [
                "Banking Control Law (Royal Decree M/5 of 1966, amended)",
                "Capital Market Law (Royal Decree M/30 of 2003)",
                "Insurance Regulation Law (Royal Decree M/32 of 2003)",
                "Anti-Money Laundering Law (Royal Decree M/20 of 2017)",
                "Personal Data Protection Law (Royal Decree M/19 of 2021)",
                "Payments System Law (Royal Decree M/17 of 2022)",
                "Cybersecurity Law (Royal Decree M/17 of 2020)",
                "Finance Companies Control Law (Royal Decree M/51 of 2012)",
            ],
            "compliance_requirements": [
                "SAMA licensing for banks, finance companies, insurance companies",
                "Capital adequacy requirements - Basel III (minimum CAR 12.5%)",
                "AML/CFT compliance - Anti-Money Laundering Law 2017",
                "Customer Due Diligence (CDD) and Enhanced Due Diligence (EDD)",
                "Suspicious Transaction Reporting to Saudi FIU (Financial Intelligence Unit)",
                "PDPL compliance - Personal Data Protection Law (effective 2023)",
                "Open Banking Framework (SAMA 2022) - API standards",
                "Cyber Security Framework (SAMA CSF) compliance",
                "Outsourcing Rules for regulated activities",
                "Consumer Protection Principles (SAMA 2020)",
                "Mortgage finance compliance (SAMA Real Estate Finance rules)",
                "CMA regulations for capital markets, investment funds, securities",
                "Tadawul listing requirements for publicly traded companies",
                "Insurance supervision - minimum solvency margin, actuarial certification",
                "Zakat and Income Tax compliance (Zakat, Tax and Customs Authority - ZATCA)",
                "Islamic finance compliance - Sharia supervisory board requirements",
                "Saudization (Nitaqat) for financial sector workforce",
                "SAMA FinTech Lab regulatory sandbox participation requirements",
            ],
            "recent_updates": [
                "SAMA Open Banking Framework implementation (2023-2024)",
                "Buy Now Pay Later (BNPL) regulations under SAMA",
                "Saudi Digital Currency (Project Aber) developments",
                "Fintech licensing regime expansion",
                "PDPL enforcement commencement (2024)",
                "Vision 2030 Financial Sector Development Program milestones",
            ],
        },
    },
}

SECTOR_KEYWORDS = {
    "REAL_ESTATE": [
        "real estate", "propert", "realty", "developer", "construction",
        "housing", "land", "estate", "reit", "mortgage", "proptech",
        "residential", "commercial", "infrastructure", "urban", "emaar",
        "damac", "aldar", "nakheel", "maf properties", "majid al futtaim properties",
    ],
    "BFSI": [
        "bank", "banking", "finance", "financial", "insurance", "investment",
        "capital", "securities", "fund", "asset management", "fintech",
        "payment", "lending", "credit", "wealth", "brokerage", "exchange",
        "risk", "actuarial", "treasury", "islamic finance", "takaful",
        "al rajhi", "fab", "adcb", "enbd", "mashreq", "riyad", "snb", "samba",
    ],
}


def get_sector_for_company(company_name: str, sector_hint: str | None = None) -> str:
    """Determine sector based on company name keywords or explicit hint."""
    if sector_hint:
        s = sector_hint.upper().replace(" ", "_")
        if "REAL" in s:
            return "REAL_ESTATE"
        if any(k in s for k in ["BFSI", "BANK", "FINANC", "INSUR"]):
            return "BFSI"

    name_lower = company_name.lower()
    re_score = sum(1 for kw in SECTOR_KEYWORDS["REAL_ESTATE"] if kw in name_lower)
    bfsi_score = sum(1 for kw in SECTOR_KEYWORDS["BFSI"] if kw in name_lower)

    if bfsi_score > re_score:
        return "BFSI"
    if re_score > bfsi_score:
        return "REAL_ESTATE"
    return "BFSI"  # default fallback


def get_regulatory_requirements(region: str, sector: str) -> dict:
    """Retrieve regulatory requirements for a given region and sector."""
    region = region.upper()
    sector = sector.upper().replace(" ", "_")

    if region not in REGULATORY_FRAMEWORK:
        return {}
    if sector not in REGULATORY_FRAMEWORK[region]:
        return {}

    return REGULATORY_FRAMEWORK[region][sector]
