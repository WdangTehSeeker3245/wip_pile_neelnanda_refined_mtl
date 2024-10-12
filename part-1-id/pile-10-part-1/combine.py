import os
import pandas as pd

# Get the current directory
current_directory = os.getcwd()

# List all .txt files in the current directory
txt_files = sorted([f for f in os.listdir(current_directory) if f.endswith('.txt')],
                   key=lambda x: int(x.split('.')[0]))  # Sort by the numeric part of the filename

# Read the content of each file and store it in a list
texts = []
for file in txt_files:
    with open(file, 'r', encoding='utf-8') as f:
        texts.append(f.read())

# Create a DataFrame
df = pd.DataFrame({'text': texts})

# Save the DataFrame as a CSV file
csv_file_name = 'combined_texts.csv'
df.to_csv(csv_file_name, index=False)

print(f'Successfully saved to {csv_file_name}')
