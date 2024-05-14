#Task 1:


import re

def extract_value(text, key):
    pattern = r"\b" + key + r":\s*([^;]+)"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
key = "Occupation"
occupation = extract_value(text, key)
print(occupation)
