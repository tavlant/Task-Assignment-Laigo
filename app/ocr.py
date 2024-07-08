from mindee import Client, PredictResponse, product
import mimetypes
import logging

mindee_client = Client(api_key="d5db2a5c8805f0e93fab9946a3a872c7")

def parse_number(value):
    if isinstance(value, str):
        try:
            return float(value.replace(',', '').replace(' ', ''))
        except (ValueError, TypeError):
            return value
    elif isinstance(value, (int, float)):
        return value
    return None

async def process_document(file_path: str):

    input_doc = mindee_client.source_from_path(file_path)

    result: PredictResponse = mindee_client.parse(product.InvoiceV4, input_doc)

    prediction = result.document.inference.prediction
    invoice_data = {
        "document_name": result.document.filename,
        "inference_prediction": {
            "locale": getattr(prediction.locale, "value", None),
            "invoice_number": getattr(prediction.invoice_number, "value", None),
            "reference_numbers": [ref.value for ref in getattr(prediction, "reference_numbers", [])],
            "purchase_date": getattr(prediction.date, "value", None),
            "due_date": getattr(prediction.due_date, "value", None),
            "total_net": parse_number(getattr(prediction.total_net, "value", None)),
            "total_amount": parse_number(getattr(prediction.total_amount, "value", None)),
            "total_tax": parse_number(getattr(prediction.total_tax, "value", None)),
            "taxes": [
                {
                    "base": parse_number(tax.basis),
                    "code": tax.code,
                    "rate": parse_number(tax.rate),
                    "amount": parse_number(tax.value)
                }
                for tax in getattr(prediction, "taxes", [])
            ],
            "supplier_name": getattr(prediction.supplier_name, "value", None),
            "supplier_payment_details": getattr(prediction.supplier_payment_details, "value", None),
            "supplier_company_registrations": [reg.value for reg in getattr(prediction, "supplier_company_registrations", [])],
            "supplier_address": getattr(prediction.supplier_address, "value", None),
            "supplier_phone_number": getattr(prediction.supplier_phone_number, "value", None),
            "supplier_website": getattr(prediction.supplier_website, "value", None),
            "supplier_email": getattr(prediction.supplier_email, "value", None),
            "customer_name": getattr(prediction.customer_name, "value", None),
            "customer_company_registrations": [reg.value for reg in getattr(prediction, "customer_company_registrations", [])],
            "customer_address": getattr(prediction.customer_address, "value", None),
            "customer_id": getattr(prediction.customer_id, "value", None),
            "shipping_address": getattr(prediction.shipping_address, "value", None),
            "billing_address": getattr(prediction.billing_address, "value", None),
            "items": [
                {
                    "description": item.description,
                    "quantity": parse_number(item.quantity),
                    "unit_price": parse_number(item.unit_price),
                    "total_amount": parse_number(item.total_amount),
                }
                for item in getattr(prediction, "line_items", [])
            ],
            "po_number": getattr(prediction, "po_number", None),
            "notes": getattr(prediction, "notes", None),
            "terms": getattr(prediction, "terms", None),
        }
    }
    return invoice_data
