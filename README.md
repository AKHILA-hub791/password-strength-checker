# Password Strength Checker

A simple Python tool that checks if a password is strong or weak based on security rules.

## Features
- Checks password length (must be 8+ characters)
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for numbers
- Checks for special characters (!@#$%^&*)
- Gives final rating: STRONG, MODERATE, or WEAK

## How to Use

```bash
python password_checker.py
```

Enter your password and see the result!

## Example Output

**Weak password (hello):**

✗ Too short (needs 8+ characters)
✗ No uppercase letter
✓ Has lowercase letter
✗ No number
✗ No special character
RESULT: WEAK PASSWORD ✗

text

**Strong password (Hello@123!):**
✓ Good length (8+ characters)
✓ Has uppercase letter
✓ Has lowercase letter
✓ Has number
✓ Has special character
RESULT: STRONG PASSWORD ✓

text

## Security Note
This is for educational purposes. Always use strong passwords for real accounts.

## Built For
Learning cybersecurity basics and password security fundamentals.
