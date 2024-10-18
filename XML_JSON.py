import os
import xmltodict
import json

# Function to extract specific fields: OrderID, Customer (name), and Products (names only)
def extract_key_fields(data_dict):
    order_data = {}

    # Extract the OrderID
    order_data['OrderID'] = data_dict.get('Order', {}).get('OrderID', 'N/A')

    # Extract Customer Name
    customer = data_dict.get('Order', {}).get('Customer', {})
    order_data['Customer'] = customer.get('Name', 'N/A')

    # Extract Product Names (list of product names)
    products = data_dict.get('Order', {}).get('Products', {}).get('Product', [])
    
    # Ensure products are in a list, even if there is only one product
    if isinstance(products, dict):  # If there's only one product, convert to a list
        products = [products]
    
    order_data['Products'] = [
        product.get('Name', 'N/A') for product in products
    ]

    return order_data

# Function to convert a single XML file to JSON with specific fields
def convert_xml_to_json(xml_file, json_file):
    with open(xml_file, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    # Convert XML to Python dictionary
    data_dict = xmltodict.parse(xml_content)

    # Extract the key fields
    extracted_data = extract_key_fields(data_dict)

    # Convert extracted fields to JSON format
    json_data = json.dumps(extracted_data, indent=4)

    # Write JSON data to the output file
    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json_data)

# Function to convert all XML files in the "xml-files" folder to JSON
def convert_all_xml_to_json():
    xml_folder = 'xml-files'
    json_folder = 'json-files'

    # Create the "json-files" directory if it doesn't exist
    if not os.path.exists(json_folder):
        os.makedirs(json_folder)

    # Loop through all files in the "xml-files" folder
    for xml_filename in os.listdir(xml_folder):
        # Only process files with .xml extension
        if xml_filename.endswith('.xml'):
            xml_file_path = os.path.join(xml_folder, xml_filename)
            json_filename = os.path.splitext(xml_filename)[0] + '.json'
            json_file_path = os.path.join(json_folder, json_filename)

            # Convert XML to JSON and save the result
            print(f'Converting {xml_filename} to {json_filename}')
            convert_xml_to_json(xml_file_path, json_file_path)

    print("Conversion complete. JSON files saved in 'json-files' folder.")

# Call the function to start the conversion process
convert_all_xml_to_json()
