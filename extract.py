import re
import pandas as pd

# Load the Excel file
xlsx_file = 'bk1.xlsx'
df = pd.read_excel(xlsx_file, header=None)

# Define regular expressions for extracting Item Number and Part Number
item_regex = r'(\d+)[\[\]]'
part_regex = r'(\d{6})'

# Initialize lists to store extracted data
data = []

# Extract data using regular expressions
for index, row in df.iterrows():
    entry = ' '.join([str(cell) for cell in row])  # Combine all cells in the row
    item_match = re.search(item_regex, entry)
    part_match = re.search(part_regex, entry)

    if item_match and part_match:
        data.append({
            'Item Number': item_match.group(1),
            'Part Number': part_match.group(1),
            'Sheet': 1,  # Assuming all data is from Sheet 1
            'Parent': '20224686018'  # Assuming the constant parent value
        })

# Create a DataFrame from the extracted data
df_extracted = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df_extracted.to_csv('extract_data.csv', index=False)

print("Data has been extracted and saved to extracted_data.csv")
