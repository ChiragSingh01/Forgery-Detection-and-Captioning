import pandas as pd

# File paths
log_file_path = 'output_dir/log.txt'  # replace with your actual log filename
excel_output_path = 'output_dir/log_data.xlsx'

# Read JSON lines into a DataFrame
df = pd.read_json(log_file_path, lines=True)

# Save DataFrame to Excel
df.to_excel(excel_output_path, index=False)

print(f"Log file successfully converted to Excel: {excel_output_path}")
