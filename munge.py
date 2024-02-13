import os

# Import the raw data as seperate lines. 
raw_data_path = os.path.join('data', 'GLB.Ts+dSST.txt')
f = open(raw_data_path, 'r')
lines = f.readlines()

# Find the start of actual data (i.e. the first line that starts with 'Year'). 
start_index = 0
for i, line in enumerate(lines):
    if line.strip().startswith('Year'):
        start_index = i
        break

# Extract the column headings and clean it up. 
col_headings = lines[start_index].strip().split()
col_headings_str = ','.join(col_headings)

# Create a list that holds clean data.
clean_data = [col_headings_str]

# Define a function that cleans and converts temperature. 
def C_to_F(C_str):
    try:
        F = float(C_str) * 0.01 * 1.8
        return f"{F:.1f}" # Format to 1 decimal place. 
    except ValueError:
        return "NaN" # Handle missing data. 

# Munge the data of following lines. 
for line in lines[start_index + 1:]:

    # Remove blank and repeated column headings lines. 
    if line.strip() and line[:4].isdigit():
        data_pts = line.strip().split()

        # Handle missing data by replacing '***' with a placeholder value "NaN". 
        if '***' in data_pts or '****' in data_pts:
            data_pts = [data_pt if data_pt != '***' and data_pt != '****' else "NaN" for data_pt in data_pts]

        # Clean and convert temperature anomalies from Celsius to Fahrenheit. 
        data_pts[1:-1] = [C_to_F(temp) for temp in data_pts[1:-1]]
        clean_data.append(','.join(data_pts))

# Write the clean data into a CSV file. 
clean_data_path = os.path.join('data', 'clean_data.csv')
f_out = open(clean_data_path, 'w')
for line in clean_data:
    f_out.write(line + '\n')
