def check_password(password):
    """Check if password is strong or weak"""
    
    # Start with score = 0
    score = 0
    
    # Check length
    if len(password) >= 8:
        score += 1
        print("✓ Good length (8+ characters)")
    else:
        print("✗ Too short (needs 8+ characters)")
    
    # Check for uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        score += 1
        print("✓ Has uppercase letter")
    else:
        print("✗ No uppercase letter")
    
    # Check for lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if has_lower:
        score += 1
        print("✓ Has lowercase letter")
    else:
        print("✗ No lowercase letter")
    
    # Check for number
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break
    if has_number:
        score += 1
        print("✓ Has number")
    else:
        print("✗ No number")
    
    # Check for special character
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = False
    for char in password:
        if char in special_chars:
            has_special = True
            break
    if has_special:
        score += 1
        print("✓ Has special character")
    else:
        print("✗ No special character")
    
    # Give final rating
    print("\n" + "="*40)
    if score >= 4:
        print("RESULT: STRONG PASSWORD ✓")
    elif score >= 2:
        print("RESULT: MODERATE PASSWORD")
    else:
        print("RESULT: WEAK PASSWORD ✗")
    print("="*40)

# Main program
print("PASSWORD STRENGTH CHECKER")
print("Enter a password to check its strength")
print()

password = input("Enter password: ")
check_password(password)
