import aiofiles
from mindee import Client
import tempfile
from utils import parse_digits

client = Client(api_key="your_mindee_api_key")

async def process_document(file):
    async with aiofiles.tempfile.NamedTemporaryFile(delete=False) as temp_file:
        await temp_file.write(file.file.read())
        temp_file.seek(0)
        
        response = client.pdf.parse(temp_file.name)
        ocr_result = response.to_json()
        
        structured_data = process_ocr_result(ocr_result)
        return structured_data

def process_ocr_result(ocr_result):
    # Convert OCR result into structured format and parse digits
    structured_data = {}  # Implement your logic here
    structured_data["parsed_numbers"] = parse_digits(ocr_result)
    return structured_data
