import re
import PyPDF2
import pandas as pd

# Open the PDF file
pdf_file = 'ORC-v3.pdf'
pdf_object = open(pdf_file, 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_object)

# Initialize lists to store extracted data
data = []

# Extract data from each page
for page_num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(page_num)
    page_text = page.extractText()

    # Find item and part numbers using regex
    item_matches = re.findall(r'\b(\d{2})', page_text)
    if len(item_matches) >= 2:
        item_number = item_matches[0]
        part_number = item_matches[1]
        data.append({
            'Item Number': item_number,
            'Part Number': part_number,
            'Sheet': 1,  # Assuming all data is from Sheet 1
            'Parent': '20224686018'  # Assuming the constant parent value
        })

# Create a DataFrame from the extracted data
df_extracted = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df_extracted.to_csv('extracted_data_from_pdf.csv', index=False)

print("Data has been extracted and saved to extracted_data_from_pdf.csv")
