"""
Test Data Generator - Comprehensive Fixes
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional, List
import random
import uuid

app = FastAPI(title="Test Data Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.get("/index.html")
async def index():
    return FileResponse("index.html")

# Pydantic models for API
class GenerateRequest(BaseModel):
    type: str
    count: int = 5
    prefix: Optional[str] = None
    suffix: Optional[str] = None

# Countries for phone/address
COUNTRIES = {
    "US": {"name": "United States", "code": "+1"},
    "GB": {"name": "United Kingdom", "code": "+44"},
    "IN": {"name": "India", "code": "+91"},
    "DE": {"name": "Germany", "code": "+49"},
    "FR": {"name": "France", "code": "+33"},
    "CA": {"name": "Canada", "code": "+1"},
    "AU": {"name": "Australia", "code": "+61"},
    "JP": {"name": "Japan", "code": "+81"},
    "BR": {"name": "Brazil", "code": "+55"},
    "IT": {"name": "Italy", "code": "+39"},
    "ES": {"name": "Spain", "code": "+34"},
    "MX": {"name": "Mexico", "code": "+52"},
    "KR": {"name": "South Korea", "code": "+82"},
    "CN": {"name": "China", "code": "+86"},
    "RU": {"name": "Russia", "code": "+7"},
    "NL": {"name": "Netherlands", "code": "+31"},
    "SE": {"name": "Sweden", "code": "+46"},
    "NO": {"name": "Norway", "code": "+47"},
    "DK": {"name": "Denmark", "code": "+45"},
    "FI": {"name": "Finland", "code": "+358"},
    "CH": {"name": "Switzerland", "code": "+41"},
    "AT": {"name": "Austria", "code": "+43"},
    "BE": {"name": "Belgium", "code": "+32"},
    "PT": {"name": "Portugal", "code": "+351"},
    "PL": {"name": "Poland", "code": "+48"},
    "CZ": {"name": "Czech Republic", "code": "+420"},
    "HU": {"name": "Hungary", "code": "+36"},
    "GR": {"name": "Greece", "code": "+30"},
    "TR": {"name": "Turkey", "code": "+90"},
    "ZA": {"name": "South Africa", "code": "+27"},
    "NZ": {"name": "New Zealand", "code": "+64"},
    "SG": {"name": "Singapore", "code": "+65"},
    "HK": {"name": "Hong Kong", "code": "+852"},
    "AE": {"name": "UAE", "code": "+971"},
    "SA": {"name": "Saudi Arabia", "code": "+966"},
    "IL": {"name": "Israel", "code": "+972"},
    "TH": {"name": "Thailand", "code": "+66"},
    "VN": {"name": "Vietnam", "code": "+84"},
    "PH": {"name": "Philippines", "code": "+63"},
    "ID": {"name": "Indonesia", "code": "+62"},
    "MY": {"name": "Malaysia", "code": "+60"},
    "AR": {"name": "Argentina", "code": "+54"},
    "CL": {"name": "Chile", "code": "+56"},
    "CO": {"name": "Colombia", "code": "+57"},
    "PE": {"name": "Peru", "code": "+51"},
    "EG": {"name": "Egypt", "code": "+20"},
    "NG": {"name": "Nigeria", "code": "+234"},
    "KE": {"name": "Kenya", "code": "+254"},
    "MA": {"name": "Morocco", "code": "+212"},
}

# IMEI Brands
IMEI_BRANDS = {
    "Apple": "35",
    "Samsung": "49",
    "Google": "49",
    "Huawei": "86",
    "Xiaomi": "86",
    "OnePlus": "86",
    "Sony": "35",
    "LG": "35",
    "Motorola": "35",
    "Nokia": "35",
}

# Credit Card Types
CREDIT_CARD_TYPES = {
    "Visa": {"prefix": "4", "length": 16},
    "Mastercard": {"prefix": str(random.randint(51, 55)), "length": 16},
    "American Express": {"prefix": "37", "length": 15},
    "Discover": {"prefix": "6011", "length": 16},
    "JCB": {"prefix": "3528", "length": 16},
    "Diners Club": {"prefix": "36", "length": 14},
    "UnionPay": {"prefix": "62", "length": 16},
}

# URL Domains
URL_DOMAINS = ["google", "facebook", "amazon", "apple", "microsoft", "twitter", "linkedin", "github", "stackoverflow", "youtube", "netflix", "instagram", "pinterest", "reddit", "tumblr", "whatsapp", "telegram", "discord", "slack", "zoom"]
URL_TLDS = ["com", "org", "net", "io", "co", "ai", "app", "dev", "tech", "info", "biz"]

# Real-world username patterns
USERNAME_NAMES = ["alex", "sam", "jordan", "taylor", "morgan", "riley", "jamie", "quinn", "casey", "dakota", "avery", "skyler", "dylan", "tanner", "emma", "olivia", "ava", "isabella", "sophia", "mia", "charlotte", "amelia", "harper", "evelyn", "liam", "noah", "oliver", "elijah", "james", "william", "benjamin"]
USERNAME_ADJ = ["cool", "happy", "sunny", "lucky", "smart", "swift", "bright", "wild", "funny", "nice", "epic", "super", "mega", "ultra", "hyper", "active", "chill", "fresh", "big", "small", "fast", "slow", "young", "great", "prime", "pro", "max", "ace"]
USERNAME_NOUN = ["cat", "dog", "wolf", "shark", "lion", "bear", "fox", "hawk", "eagle", "panda", "koala", "puppy", "kitten", "bunny", "duck", "bird", "fish", "unicorn", "dragon", "ninja", "coder", "geek", "hero", "star", "moon", "sun", "wave", "fire", "ice", "storm", "king", "queen", "prince", "lord", "lady"]

# Job Titles
JOB_TITLES = [
    "Software Engineer", "Senior Software Engineer", "Staff Engineer", "Principal Engineer",
    "Full Stack Developer", "Frontend Developer", "Backend Developer", "Mobile Developer",
    "DevOps Engineer", "Site Reliability Engineer", "Cloud Engineer", "Platform Engineer",
    "Data Engineer", "Machine Learning Engineer", "AI Engineer", "Data Scientist",
    "Cloud Architect", "Solutions Architect", "Technical Architect",
    "Engineering Manager", "Director of Engineering", "VP of Engineering", "CTO",
    "UI Designer", "UX Designer", "Product Designer", "Visual Designer",
    "Creative Director", "Art Director",
    "Product Manager", "Senior Product Manager", "Director of Product", "VP of Product",
    "Project Manager", "Senior Project Manager", "Program Manager", "Scrum Master",
    "Data Analyst", "Senior Data Analyst", "Analytics Engineer", "BI Developer",
    "System Administrator", "Network Engineer", "Security Engineer",
    "Penetration Tester", "SOC Analyst", "DevSecOps Engineer",
    "QA Engineer", "QA Automation Engineer", "Test Engineer",
    "Technical Writer", "Documentation Engineer",
    "Customer Success Engineer", "Support Engineer", "Sales Engineer",
    "Recruiter", "Technical Recruiter", "HR Manager",
    "Marketing Manager", "Digital Marketing Manager", "SEO Specialist",
]

# Company suffixes
COMPANY_SUFFIXES = ["Inc", "Corp", "LLC", "Ltd", "Group", "Solutions", "Systems", "Tech", "Labs", "Ventures", "Holdings", "Enterprises", "Co", "Partners", "Associates"]

# Street names
US_STREETS = ["Main St", "Oak Ave", "Park Blvd", "First St", "Second St", "Elm St", "Maple Dr", "Cedar Ln", "Pine St", "Elmwood Ave", "Washington St", "Lake Dr", "Hill Rd", "River Rd", "Forest Ave", "Broadway", "Market St", "Church St", "School Ave", "Mill Rd"]
UK_STREETS = ["High Street", "Station Road", "London Road", "Victoria Road", "Church Lane", "Manor Road", "Park Road", "Queens Road", "Kings Road", "Church Street", "Main Road", "River Close", "Hill View", "Station Lane", "Park Lane"]
DE_STREETS = ["Hauptstraße", "Bahnhofstraße", "Schulstraße", "Gartenstraße", "Dorfstraße", "Bergstraße", "Waldstraße", "Kirchstraße", "Lindenstraße", "Brunnenstraße", "Schloßstraße", "Friedrichstraße", "Bismarckstraße", "Goethestraße", "Schillerstraße"]
FR_STREETS = ["Rue de la Paix", "Avenue des Champs-Élysées", "Boulevard Saint-Michel", "Place de la République", "Rue Victor Hugo", "Rue du Commerce", "Avenue Jean Jaurès", "Rue de la Gare", "Place du Marché", "Avenue de la Libération"]

# Cities
CITIES = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Boston", "London", "Manchester", "Birmingham", "Edinburgh", "Glasgow", "Paris", "Lyon", "Marseille", "Berlin", "Munich", "Hamburg", "Tokyo", "Osaka", "Sydney", "Melbourne", "Toronto", "Vancouver", "Mumbai", "Delhi", "Bangalore", "Shanghai", "Beijing", "Singapore", "Dubai", "Amsterdam", "Barcelona", "Milan", "Rome", "Lisbon", "Vienna", "Prague"]

# Countries list
COUNTRIES_LIST = ["United States", "Canada", "United Kingdom", "Germany", "France", "Australia", "India", "Japan", "Brazil", "Italy", "Spain", "Mexico", "South Korea", "Netherlands", "Sweden", "Norway", "Denmark", "Finland", "Switzerland", "Austria", "Belgium", "Portugal", "Poland", "Czech Republic", "Hungary", "Greece", "Turkey", "Russia", "China", "Singapore", "UAE", "Thailand", "Vietnam", "Philippines", "Indonesia", "Malaysia", "New Zealand", "South Africa", "Egypt", "Nigeria", "Kenya", "Argentina", "Chile", "Colombia", "Peru"]

# Meaningful words for text generator
TEXT_WORDS = ["the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog", "hello", "world", "test", "data", "generator", "sample", "text", "random", "useful", "helpful", "amazing", "awesome", "brilliant", "fantastic", "wonderful", "excellent", "perfect", "beautiful", "lovely", "nice", "good", "great"]

# Categories for UI navigation
CATEGORIES = [
    {"id": "identifiers_security", "name": "Identifiers & Security", "icon": "🔑", "order": 1},
    {"id": "contact_identity", "name": "Contact & Identity", "icon": "📞", "order": 2},
    {"id": "financial_sensitive", "name": "Financial & Sensitive", "icon": "💳", "order": 3},
    {"id": "network_web", "name": "Network & Web", "icon": "🌐", "order": 4},
    {"id": "time_text", "name": "Time & Text", "icon": "🕐", "order": 5},
    {"id": "colors", "name": "Colors", "icon": "🎨", "order": 6},
    {"id": "work_org", "name": "Work & Organization", "icon": "🏢", "order": 7},
]

# Data types configuration with category mapping
DATA_TYPES = [
    # Identifiers & Security
    {"type": "uuid", "name": "UUID", "icon": "🎲", "category": "identifiers_security", "supports_prefix_suffix": True, "options": [
        {"key": "prefix", "label": "Prefix", "type": "text", "placeholder": "e.g., ID_"},
        {"key": "suffix", "label": "Suffix", "type": "text", "placeholder": "e.g., _test"}
    ]},
    {"type": "password", "name": "Password", "icon": "🔐", "category": "identifiers_security", "supports_prefix_suffix": False, "options": [
        {"key": "uppercase", "label": "Uppercase (A-Z)", "type": "checkbox", "default": True},
        {"key": "lowercase", "label": "Lowercase (a-z)", "type": "checkbox", "default": True},
        {"key": "numbers", "label": "Numbers (0-9)", "type": "checkbox", "default": True},
        {"key": "special", "label": "Special (!@#$)", "type": "checkbox", "default": False},
        {"key": "length", "label": "Length", "type": "number", "default": 16, "min": 4, "max": 128}
    ]},
    {"type": "username", "name": "Username", "icon": "🎮", "category": "identifiers_security", "supports_prefix_suffix": False, "options": [
        {"key": "prefix", "label": "Prefix", "type": "text", "placeholder": "e.g., user_"},
        {"key": "style", "label": "Style", "type": "select", "values": [("name_year", "name + year"), ("adj_noun", "adjective + noun"), ("name_random", "name + random"), ("mrx", "mrx + name")], "default": "name_year"}
    ]},
    {"type": "imei", "name": "IMEI", "icon": "📱", "category": "identifiers_security", "supports_prefix_suffix": False, "options": [
        {"key": "brand", "label": "Manufacturer", "type": "select", "values": [("Apple", "Apple"), ("Samsung", "Samsung"), ("Xiaomi", "Xiaomi"), ("Generic", "Generic")], "default": "Generic"},
        {"key": "valid_checksum", "label": "Valid checksum only", "type": "checkbox", "default": True}
    ]},
    {"type": "mac_address", "name": "MAC Address", "icon": "🔌", "category": "identifiers_security", "supports_prefix_suffix": True, "options": [
        {"key": "uppercase", "label": "Uppercase", "type": "checkbox", "default": True},
        {"key": "separator", "label": "Separator", "type": "radio", "values": [(":", ":"), ("-", "-")], "default": ":"}
    ]},
    
    # Contact & Identity
    {"type": "name", "name": "Name", "icon": "👤", "category": "contact_identity", "supports_prefix_suffix": False, "options": [
        {"key": "starts_with", "label": "Starts with", "type": "text", "placeholder": "Letter or word"},
        {"key": "ends_with", "label": "Ends with", "type": "text", "placeholder": "Letter or word"}
    ]},
    {"type": "email", "name": "Email", "icon": "📧", "category": "contact_identity", "supports_prefix_suffix": False, "options": [
        {"key": "domain", "label": "Domain", "type": "text", "placeholder": "e.g., example"},
        {"key": "extension", "label": "Extension", "type": "select", "values": [("com", ".com"), ("org", ".org"), ("net", ".net"), ("io", ".io"), ("test", ".test"), ("co", ".co")], "default": "com"}
    ]},
    {"type": "phone", "name": "Phone", "icon": "📞", "category": "contact_identity", "supports_prefix_suffix": False, "options": [
        {"key": "country", "label": "Country", "type": "select", "values": [[k, f"{v['code']} - {v['name']}"] for k, v in COUNTRIES.items()], "default": "US"},
        {"key": "include_code", "label": "Include country code", "type": "checkbox", "default": True}
    ]},
    {"type": "address", "name": "Address", "icon": "🏠", "category": "contact_identity", "supports_prefix_suffix": False, "options": [
        {"key": "country", "label": "Country", "type": "select", "values": [[k, v['name']] for k, v in COUNTRIES.items()], "default": "US"}
    ]},
    {"type": "country", "name": "Country", "icon": "🌍", "category": "contact_identity", "supports_prefix_suffix": False, "options": [
        {"key": "starts_with", "label": "Starts with", "type": "text", "placeholder": "e.g., U"}
    ]},
    {"type": "city", "name": "City", "icon": "🏙️", "category": "contact_identity", "supports_prefix_suffix": False, "options": [
        {"key": "starts_with", "label": "Starts with", "type": "text", "placeholder": "e.g., N"},
        {"key": "country_specific", "label": "Country-specific cities", "type": "checkbox", "default": False}
    ]},
    {"type": "zipcode", "name": "ZIP Code", "icon": "📮", "category": "contact_identity", "supports_prefix_suffix": False, "options": [
        {"key": "country_rules", "label": "Use country rules", "type": "checkbox", "default": True},
        {"key": "from", "label": "From", "type": "number", "default": 10000},
        {"key": "to", "label": "To", "type": "number", "default": 99999},
        {"key": "length", "label": "Length", "type": "number", "default": 5, "min": 3, "max": 10}
    ]},
    
    # Financial & Sensitive
    {"type": "credit_card", "name": "Credit Card", "icon": "💳", "category": "financial_sensitive", "supports_prefix_suffix": False, "options": [
        {"key": "card_type", "label": "Card variant", "type": "select", "values": [("Visa", "Visa"), ("Mastercard", "Mastercard"), ("American Express", "AmEx"), ("Random", "Random")], "default": "Random"},
        {"key": "valid", "label": "Valid", "type": "radio", "values": [("valid", "Valid"), ("invalid", "Invalid")], "default": "valid"}
    ]},
    {"type": "ssn", "name": "SSN", "icon": "🔢", "category": "financial_sensitive", "supports_prefix_suffix": False, "options": [
        {"key": "country", "label": "Country", "type": "select", "values": [("US", "US"), ("UK", "UK"), ("Random", "Random")], "default": "US"}
    ]},
    {"type": "barcode", "name": "Barcode", "icon": "📊", "category": "financial_sensitive", "supports_prefix_suffix": True, "options": [
        {"key": "numeric_only", "label": "Numeric only", "type": "checkbox", "default": True},
        {"key": "length", "label": "Length", "type": "number", "default": 13, "min": 8, "max": 20}
    ]},
    {"type": "isbn", "name": "ISBN", "icon": "📚", "category": "financial_sensitive", "supports_prefix_suffix": True, "options": [
        {"key": "format", "label": "Format", "type": "radio", "values": [("isbn10", "ISBN-10"), ("isbn13", "ISBN-13")], "default": "isbn13"}
    ]},
    
    # Network & Web
    {"type": "ip", "name": "IP Address", "icon": "🌐", "category": "network_web", "supports_prefix_suffix": True, "options": [
        {"key": "version", "label": "IP Version", "type": "radio", "values": [("ipv4", "IPv4"), ("ipv6", "IPv6")], "default": "ipv4"}
    ]},
    {"type": "url", "name": "URL", "icon": "🔗", "category": "network_web", "supports_prefix_suffix": False, "options": [
        {"key": "domain", "label": "Domain", "type": "text", "placeholder": "e.g., google"},
        {"key": "extension", "label": "Extension", "type": "select", "values": [("com", ".com"), ("net", ".net"), ("org", ".org"), ("io", ".io"), ("test", ".test"), ("co", ".co")], "default": "com"},
        {"key": "protocol", "label": "Protocol", "type": "radio", "values": [("https", "https"), ("http", "http")], "default": "https"}
    ]},
    
    # Time & Text
    {"type": "datetime", "name": "DateTime", "icon": "🕐", "category": "time_text", "supports_prefix_suffix": False, "options": [
        {"key": "include_date", "label": "Date (dd/mm/yyyy)", "type": "checkbox", "default": True},
        {"key": "include_time", "label": "Time (hh:mm:ss)", "type": "checkbox", "default": True},
        {"key": "include_timezone", "label": "Timezone (Z)", "type": "checkbox", "default": False}
    ]},
    {"type": "sentence", "name": "Sentence", "icon": "📚", "category": "time_text", "supports_prefix_suffix": False, "options": [
        {"key": "grammatically_valid", "label": "Grammatically valid", "type": "checkbox", "default": True}
    ]},
    {"type": "paragraph", "name": "Paragraph", "icon": "📖", "category": "time_text", "supports_prefix_suffix": False, "options": [
        {"key": "min_sentences", "label": "Min sentences", "type": "number", "default": 3, "min": 1, "max": 10},
        {"key": "max_sentences", "label": "Max sentences", "type": "number", "default": 6, "min": 1, "max": 20}
    ]},
    
    # Colors
    {"type": "hex_color", "name": "Hex Color", "icon": "🎨", "category": "colors", "supports_prefix_suffix": False, "options": [
        {"key": "uppercase", "label": "Uppercase", "type": "checkbox", "default": True}
    ]},
    {"type": "rgb_color", "name": "RGB Color", "icon": "🌈", "category": "colors", "supports_prefix_suffix": False, "options": [
        {"key": "min_value", "label": "Min value", "type": "number", "default": 0, "min": 0, "max": 255},
        {"key": "max_value", "label": "Max value", "type": "number", "default": 255, "min": 0, "max": 255}
    ]},
    
    # Work & Organization
    {"type": "company", "name": "Company", "icon": "🏢", "category": "work_org", "supports_prefix_suffix": False, "options": [
        {"key": "starts_with", "label": "Starts with", "type": "text", "placeholder": "e.g., Tech"}
    ]},
    {"type": "job", "name": "Job Title", "icon": "💼", "category": "work_org", "supports_prefix_suffix": False, "options": [
        {"key": "seniority", "label": "Seniority", "type": "select", "values": [("any", "Any"), ("junior", "Junior"), ("senior", "Senior"), ("lead", "Lead")], "default": "any"}
    ]},
]

FUN_MESSAGES = [
    "✨ Poof! All done!", "🎉 Boom! Data incoming!", "🚀 Ready for liftoff!",
    "🎯 Bullseye!", "🪄 Magic happens here!", "⚡ ZAP! Done!",
    "🔥 Hot fresh data!", "🌟 Shining bright!", "💥 Pow!", "🎊 Party time!"
]

# ============ API Endpoints ============

@app.get("/api/types")
async def get_types():
    """Get all data types"""
    return [{"type": t["type"], "name": t["name"], "icon": t["icon"], "category": t["category"]} for t in DATA_TYPES]

@app.get("/api/types/{type_id}")
async def get_type_config(type_id: str):
    """Get configuration options for a specific type"""
    t = next((t for t in DATA_TYPES if t["type"] == type_id), None)
    if not t:
        raise HTTPException(status_code=404, detail="Type not found")
    return {
        "type": t["type"],
        "name": t["name"],
        "icon": t["icon"],
        "category": t["category"],
        "supports_prefix_suffix": t["supports_prefix_suffix"],
        "options": t.get("options", [])
    }

@app.get("/api/categories")
async def get_categories():
    """Get all categories with their types"""
    result = []
    for cat in sorted(CATEGORIES, key=lambda x: x["order"]):
        types = [{"type": t["type"], "name": t["name"], "icon": t["icon"]} 
                 for t in DATA_TYPES if t["category"] == cat["id"]]
        result.append({"id": cat["id"], "name": cat["name"], "icon": cat["icon"], "types": types})
    return result

@app.post("/api/generate")
async def generate_data(request: GenerateRequest):
    """Generate test data"""
    t = next((t for t in DATA_TYPES if t["type"] == request.type), None)
    if not t:
        raise HTTPException(status_code=400, detail=f"Unknown type: {request.type}")
    
    prefix = request.prefix if t["supports_prefix_suffix"] else None
    suffix = request.suffix if t["supports_prefix_suffix"] else None
    
    results = []
    request_dict = request.model_dump()
    options = {k: v for k, v in request_dict.items() if k not in ["type", "count", "prefix", "suffix"] and v is not None}
    
    for _ in range(request.count):
        value = generate_by_type(request.type, options)
        if prefix or suffix:
            value = apply_prefix_suffix(value, prefix, suffix)
        results.append(value)
    
    return {
        "success": True,
        "message": random.choice(FUN_MESSAGES),
        "data": results
    }

# ============ Generator Functions ============

def generate_by_type(type_id: str, options: dict) -> str:
    """Generate a single value of the specified type"""
    options = {k: v for k, v in options.items() if v is not None}
    
    if type_id == "uuid":
        return str(uuid.uuid4())
    elif type_id == "password":
        return generate_password(
            uppercase=options.get("uppercase", True),
            lowercase=options.get("lowercase", True),
            numbers=options.get("numbers", True),
            special=options.get("special", False),
            length=options.get("length", 16)
        )
    elif type_id == "username":
        return generate_username(
            prefix=options.get("prefix"),
            style=options.get("style", "name_year")
        )
    elif type_id == "imei":
        return generate_imei(
            brand=options.get("brand", "Generic"),
            valid_checksum=options.get("valid_checksum", True)
        )
    elif type_id == "mac_address":
        return generate_mac_address(
            uppercase=options.get("uppercase", True),
            separator=options.get("separator", ":")
        )
    elif type_id == "name":
        return generate_name(
            starts_with=options.get("starts_with"),
            ends_with=options.get("ends_with")
        )
    elif type_id == "email":
        return generate_email(
            domain=options.get("domain"),
            extension=options.get("extension")
        )
    elif type_id == "phone":
        return generate_phone(
            country=options.get("country", "US"),
            include_code=options.get("include_code", True)
        )
    elif type_id == "address":
        return generate_address(country=options.get("country", "US"))
    elif type_id == "country":
        return generate_country(starts_with=options.get("starts_with"))
    elif type_id == "city":
        return generate_city(
            starts_with=options.get("starts_with"),
            country_specific=options.get("country_specific", False)
        )
    elif type_id == "zipcode":
        return generate_zipcode(
            country_rules=options.get("country_rules", True),
            zip_from=options.get("from", 10000),
            zip_to=options.get("to", 99999),
            length=options.get("length", 5)
        )
    elif type_id == "credit_card":
        return generate_credit_card(
            card_type=options.get("card_type", "Random"),
            valid=options.get("valid", "valid") == "valid"
        )
    elif type_id == "ssn":
        return generate_ssn(country=options.get("country", "US"))
    elif type_id == "barcode":
        return generate_barcode(
            numeric_only=options.get("numeric_only", True),
            length=options.get("length", 13)
        )
    elif type_id == "isbn":
        return generate_isbn(format=options.get("format", "isbn13"))
    elif type_id == "ip":
        return generate_ip(version=options.get("version", "ipv4"))
    elif type_id == "url":
        return generate_url(
            domain=options.get("domain"),
            extension=options.get("extension", "com"),
            protocol=options.get("protocol", "https")
        )
    elif type_id == "datetime":
        return generate_datetime(
            include_date=options.get("include_date", True),
            include_time=options.get("include_time", True),
            include_timezone=options.get("include_timezone", False)
        )
    elif type_id == "sentence":
        return generate_sentence(grammatically_valid=options.get("grammatically_valid", True))
    elif type_id == "paragraph":
        return generate_paragraph(
            min_sentences=options.get("min_sentences", 3),
            max_sentences=options.get("max_sentences", 6)
        )
    elif type_id == "hex_color":
        return generate_hex_color(uppercase=options.get("uppercase", True))
    elif type_id == "rgb_color":
        return generate_rgb_color(
            min_value=options.get("min_value", 0),
            max_value=options.get("max_value", 255)
        )
    elif type_id == "company":
        return generate_company(starts_with=options.get("starts_with"))
    elif type_id == "job":
        return generate_job(seniority=options.get("seniority", "any"))
    elif type_id == "street":
        return generate_street()
    elif type_id == "text":
        return generate_text(length=options.get("length", 5))
    return ""

def apply_prefix_suffix(value: str, prefix: str = None, suffix: str = None) -> str:
    """Apply prefix and suffix to a value"""
    prefix = prefix or ""
    suffix = suffix or ""
    if not prefix and not suffix:
        return value
    max_len = len(value) - len(prefix) - len(suffix)
    if max_len < 1:
        return prefix + suffix
    return prefix + value[:max_len] + suffix

def generate_uuid():
    return str(uuid.uuid4())

def generate_phone(country="US", include_code=True):
    c = COUNTRIES.get(country, COUNTRIES["US"])
    code = c["code"]
    
    if country in ["US", "CA"]:
        num = f"({random.randint(200, 999)}) {random.randint(200, 999)}-{random.randint(1000, 9999)}"
        return f"{code} {num}" if include_code else num
    elif country == "IN":
        num = str(random.randint(7000000000, 9999999999))
        return f"{code} {num}" if include_code else num
    elif country == "GB":
        num = f"{random.randint(20, 99)} {random.randint(1000, 9999)} {random.randint(100, 999)}"
        return f"{code} {num}" if include_code else num
    else:
        num = str(random.randint(100000000, 999999999))
        return f"{code} {num}" if include_code else num

def generate_email(domain=None, extension=None):
    names = ["alex", "sam", "jordan", "taylor", "morgan", "riley", "jamie", "quinn", "casey", "dakota", "avery", "skyler"]
    
    if domain and extension:
        return f"{random.choice(names).lower()}{random.randint(1, 999)}@{domain}.{extension}"
    elif domain:
        return f"{random.choice(names).lower()}{random.randint(1, 999)}@{domain}"
    elif extension:
        return f"{random.choice(names).lower()}{random.randint(1, 999)}@{random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])}"
    else:
        return f"{random.choice(names).lower()}{random.randint(1, 999)}@{random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])}"

def generate_address(country="US"):
    if country == "US":
        return f"{random.randint(100, 9999)} {random.choice(US_STREETS)}, {random.choice(CITIES[:20])}, {random.choice(['CA', 'NY', 'TX', 'FL', 'IL'])} {random.randint(10000, 99999)}"
    elif country == "UK":
        return f"{random.randint(1, 200)} {random.choice(UK_STREETS)}, {random.choice(['London', 'Manchester', 'Birmingham'])}, {random.choice(['SW1A', 'EC1A', 'W1A'])}"
    else:
        return f"{random.randint(100, 9999)} {random.choice(US_STREETS)}, {random.choice(CITIES[:10])} {random.randint(10000, 99999)}"

def generate_name(starts_with=None, ends_with=None):
    first_names = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda", "David", "Elizabeth", "William", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen", "Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn", "Liam", "Noah", "Oliver", "Elijah"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"]
    
    if starts_with:
        starts_with = starts_with.strip().upper()
        candidates = []
        for f in first_names:
            if f.upper().startswith(starts_with):
                candidates.append(f"{f} {random.choice(last_names)}")
        for l in last_names:
            if l.upper().startswith(starts_with):
                candidates.append(f"{random.choice(first_names)} {l}")
        if candidates:
            return random.choice(candidates)
    
    if ends_with:
        ends_with = ends_with.strip().upper()
        candidates = []
        for f in first_names:
            if f.upper().endswith(ends_with):
                candidates.append(f"{f} {random.choice(last_names)}")
        for l in last_names:
            if l.upper().endswith(ends_with):
                candidates.append(f"{random.choice(first_names)} {l}")
        if candidates:
            return random.choice(candidates)
    
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_imei(brand="Generic", valid_checksum=True):
    if brand == "Generic":
        tac = str(random.randint(35, 86))
    else:
        tac = IMEI_BRANDS.get(brand, "35")
    
    imei = tac + "".join([str(random.randint(0, 9)) for _ in range(12)])
    
    if not valid_checksum:
        return imei + str((int(imei[-1]) + 1) % 10)
    
    total = 0
    doubled = False
    for digit in imei[::-1]:
        d = int(digit) * (2 if doubled else 1)
        total += d if d < 10 else d - 9
        doubled = not doubled
    check = (10 - (total % 10)) % 10
    return imei + str(check)

def generate_mac_address(uppercase=True, separator=":"):
    parts = [f"{random.randint(0, 255):02x}" for _ in range(6)]
    result = separator.join(parts)
    return result.upper() if uppercase else result

def generate_credit_card(card_type="Random", valid=True):
    if card_type == "Random":
        card_type = random.choice(["Visa", "Mastercard", "American Express"])
    
    config = CREDIT_CARD_TYPES.get(card_type, CREDIT_CARD_TYPES["Visa"])
    prefix = config["prefix"]
    length = config["length"]
    
    cc = prefix
    while len(cc) < length - 1:
        cc += str(random.randint(0, 9))
    
    total = 0
    doubled = True
    for digit in cc[::-1]:
        d = int(digit) * (2 if doubled else 1)
        if d > 9: d -= 9
        total += d
        doubled = not doubled
    check = (10 - (total % 10)) % 10
    cc += str(check)
    
    if not valid:
        cc = cc[:-1] + str((int(cc[-1]) + 1) % 10)
    
    if card_type == "American Express":
        return f"{cc[:4]}-{cc[4:10]}-{cc[10:]}"
    else:
        return "-".join([cc[i:i+4] for i in range(0, len(cc), 4)])

def generate_ssn(country="US"):
    if country == "US":
        return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"
    elif country == "UK":
        return f"{random.randint(10, 99)} {random.randint(100000, 999999)} {random.randint(100000, 999999)}"
    else:
        return f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000, 9999)}"

def generate_barcode(numeric_only=True, length=13):
    if numeric_only:
        return "".join([str(random.randint(0, 9)) for _ in range(length)])
    else:
        chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "".join([random.choice(chars) for _ in range(length)])

def generate_isbn(format="isbn13"):
    if format == "isbn10":
        digits = "".join([str(random.randint(0, 9)) for _ in range(9)])
        total = sum((10 - i) * int(d) for i, d in enumerate(digits))
        check = (11 - (total % 11)) % 11
        check_char = 'X' if check == 10 else str(check)
        return f"{digits[:3]}-{digits[3:4]}-{digits[4:8]}-{digits[8:9]}-{check_char}"
    else:
        prefix = "978" + "".join([str(random.randint(0, 9)) for _ in range(7)])
        total = sum((3 if i % 2 else 1) * int(d) for i, d in enumerate(prefix))
        check = (10 - (total % 10)) % 10
        return f"{prefix[:3]}-{prefix[3:4]}-{prefix[4:7]}-{prefix[7:9]}-{prefix[9:]}{check}"

def generate_ip(version="ipv4"):
    if version == "ipv6":
        return ":".join([f"{random.randint(0, 65535):x}" for _ in range(8)])
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def generate_url(domain=None, extension="com", protocol="https"):
    if domain:
        dom = domain
    else:
        dom = random.choice(URL_DOMAINS)
    path = random.choice(["about", "products", "services", "blog", "contact"])
    return f"{protocol}://{dom}.{extension}/{path}"

def generate_datetime(include_date=True, include_time=True, include_timezone=False):
    year = random.randint(2020, 2025)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    
    parts = []
    if include_date:
        parts.append(f"{day:02d}/{month:02d}/{year}")
    if include_time:
        parts.append(f"{hour:02d}:{minute:02d}:{second:02d}")
    if include_timezone:
        parts.append("Z")
    
    return " ".join(parts)

def generate_sentence(grammatically_valid=True):
    if grammatically_valid:
        subjects = ["The quick brown fox", "A happy dog", "The clever cat", "An innovative startup", "A dedicated team", "The talented developer", "An amazing product", "A revolutionary idea"]
        verbs = ["jumps over", "runs through", "explores", "discovers", "builds", "creates", "transforms", "improves"]
        objects = ["the lazy bear", "the tall building", "new horizons", "exciting opportunities", "powerful solutions", "beautiful designs", "complex problems", "amazing experiences"]
        return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."
    else:
        words = TEXT_WORDS
        sentence = " ".join([random.choice(words) for _ in range(random.randint(5, 12))])
        return sentence[0].upper() + sentence[1:] + "."

def generate_paragraph(min_sentences=3, max_sentences=6):
    sentences = []
    for _ in range(random.randint(min_sentences, max_sentences)):
        sentences.append(generate_sentence(grammatically_valid=True))
    return " ".join(sentences)

def generate_hex_color(uppercase=True):
    color = "#" + "".join([f"{random.randint(0, 255):02x}" for _ in range(3)])
    return color.upper() if uppercase else color

def generate_rgb_color(min_value=0, max_value=255):
    r = random.randint(min_value, max_value)
    g = random.randint(min_value, max_value)
    b = random.randint(min_value, max_value)
    return f"rgb({r}, {g}, {b})"

def generate_company(starts_with=None):
    name = random.choice(USERNAME_ADJ).capitalize() + " " + random.choice(["Solutions", "Systems", "Technologies", "Labs", "Ventures", "Group", "Inc"])
    if starts_with:
        if starts_with.strip().upper() in name.upper():
            return name
        return starts_with + name
    return name

def generate_job(seniority="any"):
    if seniority != "any":
        jobs = [j for j in JOB_TITLES if seniority.lower() in j.lower()]
        if jobs:
            return random.choice(jobs)
    return random.choice(JOB_TITLES)

def generate_password(uppercase=True, lowercase=True, numbers=True, special=False, length=16):
    chars = ""
    if uppercase:
        chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if lowercase:
        chars += "abcdefghijklmnopqrstuvwxyz"
    if numbers:
        chars += "0123456789"
    if special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not chars:
        chars = "abcdefghijklmnopqrstuvwxyz"
    
    return "".join([random.choice(chars) for _ in range(length)])

def generate_username(prefix=None, style="name_year"):
    name = random.choice(USERNAME_NAMES)
    adj = random.choice(USERNAME_ADJ)
    noun = random.choice(USERNAME_NOUN)
    
    if style == "name_year":
        result = f"{name}{random.randint(1, 99)}"
    elif style == "adj_noun":
        result = f"{adj}_{noun}"
    elif style == "name_random":
        result = f"{name}.{random.randint(100, 999)}"
    else:
        result = f"mrx_{name}"
    
    return (prefix or "") + result

def generate_country(starts_with=None):
    if starts_with:
        starts_with = starts_with.strip().upper()
        candidates = [c for c in COUNTRIES_LIST if c.upper().startswith(starts_with)]
        if candidates:
            return random.choice(candidates)
    return random.choice(COUNTRIES_LIST)

def generate_city(starts_with=None, country_specific=False):
    if starts_with:
        starts_with = starts_with.strip().upper()
        candidates = [c for c in CITIES if c.upper().startswith(starts_with)]
        if candidates:
            return random.choice(candidates)
    return random.choice(CITIES)

def generate_zipcode(country_rules=True, zip_from=10000, zip_to=99999, length=5):
    return str(random.randint(zip_from, zip_to)).zfill(length)

def generate_street():
    return f"{random.randint(100, 9999)} {random.choice(US_STREETS)}"

def generate_text(length=5):
    return " ".join(random.choice(TEXT_WORDS) for _ in range(length))
