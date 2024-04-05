import re

def check_password_complexity(password):
    # Check if the password meets minimum length requirement
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    else:

    # Check if the password contains uppercase letters
      if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."

    # Check if the password contains lowercase letters
      if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."

    # Check if the password contains numbers
      if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number."

    # Check if the password contains special characters
      if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."

    # Check if the password is not a common pattern or dictionary word
      common_patterns = ["password", "123456", "qwerty", "letmein"]
      if password.lower() in common_patterns:
        return False, "Password is too common or easily guessable."

      return True, "Password meets complexity requirements."

# Example usage:
password = input("Enter your password: ")
is_complex, message = check_password_complexity(password)
print(message)
