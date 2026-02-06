"""
Secure Input Validation - Educational Example
==============================================
Demonstrates safe input handling to prevent common attacks.

This shows:
- Input validation patterns
- Sanitization techniques
- Safe database queries
"""

import re


# ===========================================
# VALIDATION FUNCTIONS
# ===========================================

def validate_username(username):
    """
    Validate username meets security requirements.
    
    Rules:
    - 3-20 characters
    - Alphanumeric and underscores only
    - Must start with a letter
    """
    if not username:
        return False, "Username cannot be empty"
    
    if len(username) < 3:
        return False, "Username must be at least 3 characters"
    
    if len(username) > 20:
        return False, "Username cannot exceed 20 characters"
    
    # Only allow safe characters
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]*$'
    if not re.match(pattern, username):
        return False, "Username must start with a letter and contain only letters, numbers, underscores"
    
    return True, "Valid"


def validate_email(email):
    """
    Validate email format.
    """
    if not email:
        return False, "Email cannot be empty"
    
    # Basic email pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, "Invalid email format"
    
    if len(email) > 254:
        return False, "Email too long"
    
    return True, "Valid"


def sanitize_string(text, max_length=500):
    """
    Sanitize text input to prevent injection attacks.
    
    - Removes dangerous characters
    - Limits length
    - Strips whitespace
    """
    if not text:
        return ""
    
    # Limit length first
    text = text[:max_length]
    
    # Remove null bytes (used in some attacks)
    text = text.replace('\x00', '')
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    # Remove HTML/script tags (basic XSS prevention)
    text = re.sub(r'<[^>]*>', '', text)
    
    return text


# ===========================================
# DATABASE EXAMPLES
# ===========================================

def unsafe_query(username):
    """
    ❌ UNSAFE: SQL Injection vulnerable!
    
    DO NOT USE THIS PATTERN!
    Shown only to demonstrate what NOT to do.
    """
    # This is INSECURE - attacker can inject SQL!
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query


def safe_query(username):
    """
    ✅ SAFE: Parameterized query
    
    Use this pattern instead!
    """
    # Parameterized query - user input is never part of SQL
    query = "SELECT * FROM users WHERE username = ?"
    params = (username,)
    return query, params


# ===========================================
# DEMO
# ===========================================

def main():
    print("=" * 50)
    print("🛡️ INPUT VALIDATION DEMO")
    print("=" * 50)
    print()
    
    # Test valid inputs
    print("Testing Valid Inputs:")
    print(f"  'cyber_trainee': {validate_username('cyber_trainee')}")
    print(f"  'test@example.com': {validate_email('test@example.com')}")
    print()
    
    # Test invalid inputs
    print("Testing Invalid Inputs:")
    print(f"  'ab': {validate_username('ab')}")
    print(f"  '123start': {validate_username('123start')}")
    print(f"  'not-an-email': {validate_email('not-an-email')}")
    print()
    
    # Demonstrate SQL injection prevention
    print("SQL Injection Prevention:")
    malicious_input = "admin'; DROP TABLE users; --"
    print(f"  Malicious input: {malicious_input}")
    print(f"  Unsafe query: {unsafe_query(malicious_input)}")
    print(f"  Safe query: {safe_query(malicious_input)}")
    
    print()
    print("=" * 50)


if __name__ == "__main__":
    main()
