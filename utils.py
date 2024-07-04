import re

def parse_digits(ocr_result):
    digits = []
    text_data = ocr_result.get("document", {}).get("content", "")
    
    matches = re.findall(r'\b\d+(\.\d+)?\b', text_data)
    for match in matches:
        digits.append(float(match))
    
    return digits
