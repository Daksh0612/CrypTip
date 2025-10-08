import re, random, json
# Very basic regexes for demo purposes
ETH_REGEX = re.compile(r'^(0x)[0-9a-fA-F]{40}$')
BTC_REGEX = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')

def validate_address(addr: str, chain: str):
    chain = (chain or "ETH").upper()
    if chain == "ETH":
        return True if ETH_REGEX.match(addr) else False
    if chain == "BTC":
        return True if BTC_REGEX.match(addr) else False
    # fallback: accept non-empty
    return bool(addr and len(addr) > 10)

def analyze_address(addr: str, chain: str):
    # Demo analyzer: returns fake metadata and risk score
    metadata = {
        "checksum_ok": True,
        "balance_checked": False,
        "sample_tags": ["demo"]
    }
    risk_score = round(random.random()*100, 2)
    # categorize roughly
    category = "exchange" if risk_score < 30 else ("scam" if risk_score > 70 else "wallet")
    return metadata, risk_score, category