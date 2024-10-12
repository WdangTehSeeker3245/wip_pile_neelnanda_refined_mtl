import csv
import os

# File paths
csv_file = 'pile-100-part-1.csv'
output_dir = './part-1'

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open the CSV file and process each row
with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)  # Use DictReader to access columns by header name
    
    # Iterate over rows
    for row_number, row in enumerate(csv_reader, start=1):
        # Extract only the 'text' column (adjust the column name if necessary)
        text_content = row.get('text', '').strip()  # Default to empty string if 'text' column doesn't exist
        
        # Create a filename for each row, based on row number
        output_file = os.path.join(output_dir, f'row_{row_number}.txt')
        
        # Write the text content to a .txt file
        with open(output_file, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_content)

print(f"Extraction complete. Files saved in: {output_dir}")
