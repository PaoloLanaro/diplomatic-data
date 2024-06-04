import json

# Function to convert JSON to a single SQL insert statement with multiple values
def json_to_sql(json_file, table_name, output_file):
    # Load JSON data
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Get the column names from the keys of the first dictionary
    columns = data[0].keys()
    
    # Generate the SQL insert statement with multiple values
    values_list = []
    for entry in data:
        values = [f"'{str(value).replace('\'', '\'\'')}'" if isinstance(value, str) else str(value) for value in entry.values()]
        values_list.append(f"({', '.join(values)})")
    
    sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES\n{',\n'.join(values_list)};"
    
    # Write the SQL statement to the output file
    with open(output_file, 'w') as file:
        file.write(sql + '\n')

# Example usage
json_file = 'Mockaroo_manager.json'
table_name = 'manager'
output_file = 'dylan_manager.sql'
json_to_sql(json_file, table_name, output_file)

