import re

def check_password(pwd):
    score = 0
    feedback = []
    
    if len(pwd) >= 8: score += 1
    else: feedback.append("Too short (min 8 chars)")
    
    if re.search("[a-z]", pwd): score += 1
    else: feedback.append("Add lowercase letters")
    
    if re.search("[A-Z]", pwd): score += 1
    else: feedback.append("Add uppercase letters")
    
    if re.search("[0-9]", pwd): score += 1
    else: feedback.append("Add numbers")
    
    if re.search(r"[@$!%*?&]", pwd): score += 1
    else: feedback.append("Add special characters")

    levels = {0: "Weak", 1: "Weak", 2: "Weak", 3: "Medium", 4: "Medium", 5: "Strong"}
    print(f"Score: {score}/5 - Strength: {levels[score]}")
    if feedback:
        print("Recommendations:", ", ".join(feedback))

password = input("Enter password to check: ")
check_password(password)
