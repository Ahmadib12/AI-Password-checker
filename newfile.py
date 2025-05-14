import re

def extract_features(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    is_common = password.lower() in ["password", "123456", "qwerty"]
    has_keyboard_walk = any(pattern in password.lower() for pattern in ["qwerty", "asdfgh", "zxcvbn"])
    has_date_pattern = re.search(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\d{2,4}\b', password, re.IGNORECASE) is not None
    has_repeated_char = re.search(r'(.)\1{2,}', password) is not None # Check for 3 or more repeating chars

    return {
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "is_common": is_common,
        "has_keyboard_walk": has_keyboard_walk,
        "has_date_pattern": has_date_pattern,
        "has_repeated_char": has_repeated_char,
    }

def assess_strength(features):
    score = 0
    feedback = []

    if features["length"] < 8:
        feedback.append("Consider making your password longer (at least 8 characters).")
    elif features["length"] >= 12:
        score += 2

    if features["has_upper"]:
        score += 1
    else:
        feedback.append("Try including uppercase letters.")

    if features["has_lower"]:
        score += 1
    else:
        feedback.append("Try including lowercase letters.")

    if features["has_digit"]:
        score += 1
    else:
        feedback.append("Try including numbers.")

    if features["has_symbol"]:
        score += 1
    else:
        feedback.append("Try including symbols (e.g., !, @, #).")

    if features["is_common"]:
        feedback.append("Avoid using common passwords like 'password' or '123456'.")
        score -= 3

    if features["has_keyboard_walk"]:
        feedback.append("Avoid using keyboard patterns like 'qwerty' or 'asdfgh'.")
        score -= 2

    if features["has_date_pattern"]:
        feedback.append("Avoid using easily guessable date patterns.")
        score -= 1

    if features["has_repeated_char"]:
        feedback.append("Avoid using too many repeated characters (e.g., 'aaa').")
        score -= 1

    if score >= 4:
        strength = "Strong"
    elif score >= 2:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

if __name__ == "__main__":
    password = input("Enter your password: ")
    features = extract_features(password)
    strength, feedback = assess_strength(features)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions for improvement:")
        for suggestion in feedback:
            print(f"- {suggestion}")
    else:
        print("Good job!")
