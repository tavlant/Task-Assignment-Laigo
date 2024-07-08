import os

def get_downloads_folder():
    if os.name == 'nt':  
        return os.path.join(os.path.expanduser('~'), 'Downloads')
    else:  
        return os.path.join(os.path.expanduser('~'), 'Downloads')

def save_document_to_txt(document_data: str, file_path: str):
    with open(file_path, 'w') as file:
        file.write(document_data)

def format_invoice_data(invoice_data):
    formatted_data = f"Locale: {invoice_data['inference_prediction']['locale']}\n"
    formatted_data += f"Invoice Number: {invoice_data['inference_prediction']['invoice_number']}\n"
    formatted_data += f"Reference Numbers: {', '.join(invoice_data['inference_prediction']['reference_numbers'])}\n"
    formatted_data += f"Purchase Date: {invoice_data['inference_prediction']['purchase_date']}\n"
    formatted_data += f"Due Date: {invoice_data['inference_prediction']['due_date']}\n"
    formatted_data += f"Total Net: {invoice_data['inference_prediction']['total_net']}\n"
    formatted_data += f"Total Amount: {invoice_data['inference_prediction']['total_amount']}\n"
    formatted_data += f"Total Tax: {invoice_data['inference_prediction']['total_tax']}\n"
    formatted_data += "Taxes:\n"
    formatted_data += "  +---------------+--------+----------+---------------+\n"
    formatted_data += "  | Base          | Code   | Rate (%) | Amount        |\n"
    formatted_data += "  +===============+========+==========+===============+\n"
    for tax in invoice_data['inference_prediction']['taxes']:
        formatted_data += f"  | {tax['base']}          | {tax['code']}   | {tax['rate']}    | {tax['amount']}         |\n"
    formatted_data += "  +---------------+--------+----------+---------------+\n"
    formatted_data += f"Supplier Name: {invoice_data['inference_prediction']['supplier_name']}\n"
    formatted_data += f"Supplier Payment Details: {invoice_data['inference_prediction']['supplier_payment_details']}\n"
    formatted_data += f"Supplier Company Registrations: {', '.join(invoice_data['inference_prediction']['supplier_company_registrations'])}\n"
    formatted_data += f"Supplier Address: {invoice_data['inference_prediction']['supplier_address']}\n"
    formatted_data += f"Supplier Phone Number: {invoice_data['inference_prediction']['supplier_phone_number']}\n"
    formatted_data += f"Supplier Website: {invoice_data['inference_prediction']['supplier_website']}\n"
    formatted_data += f"Supplier Email: {invoice_data['inference_prediction']['supplier_email']}\n"
    formatted_data += f"Customer Name: {invoice_data['inference_prediction']['customer_name']}\n"
    formatted_data += f"Customer Company Registrations: {', '.join(invoice_data['inference_prediction']['customer_company_registrations'])}\n"
    formatted_data += f"Customer Address: {invoice_data['inference_prediction']['customer_address']}\n"
    formatted_data += f"Customer ID: {invoice_data['inference_prediction']['customer_id']}\n"
    formatted_data += f"Shipping Address: {invoice_data['inference_prediction']['shipping_address']}\n"
    formatted_data += f"Billing Address: {invoice_data['inference_prediction']['billing_address']}\n"
    formatted_data += "Items:\n"
    formatted_data += "  +--------------------------------------+--------------+----------+------------+--------------+--------------+------------+\n"
    formatted_data += "  | Description                          | Product code | Quantity | Tax Amount | Tax Rate (%) | Total Amount | Unit Price |\n"
    formatted_data += "  +======================================+==============+==========+============+==============+==============+============+\n"
    for item in invoice_data['inference_prediction']['items']:
        formatted_data += f"  | {item['description']}                                 |              | {item['quantity']}     |            |              | {item['total_amount']}       | {item['unit_price']}     |\n"
    formatted_data += "  +--------------------------------------+--------------+----------+------------+--------------+--------------+------------+\n"
    formatted_data += f"PO Number: {invoice_data['inference_prediction']['po_number']}\n"
    formatted_data += f"Notes: {invoice_data['inference_prediction']['notes']}\n"
    formatted_data += f"Terms: {invoice_data['inference_prediction']['terms']}\n"
    return formatted_data

def format_and_save_response(result, base_file_name: str):
    document_name = result.get("document_name", "Unknown Document")
    inference_prediction = result.get("inference_prediction", {})

    
    document_data = format_invoice_data({"inference_prediction": inference_prediction})

 
    output_dir = get_downloads_folder()

 
    file_path = os.path.join(output_dir, f"{base_file_name}.txt")

    
    save_document_to_txt(document_data, file_path)

    return {
        "document": document_name,
        "inference_prediction": inference_prediction
    }
