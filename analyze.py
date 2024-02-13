import os
import csv

# Open the CSV file. 
clean_data_path = os.path.join('data', 'clean_data.csv')
f = open(clean_data_path, newline = '')
reader = csv.reader(f)
next(reader) # Skip the row of column headings.

# Define a function that identifies the decade. 
def dec(year):
    return (year // 10) * 10

# Set up variables.
dec_anomalies = {}
dec_counts = {}
for row in reader:
    year = int(row[0])
    anomaly_str = row[13] # I'll just use the J-D AnnMean variable.

    # Check for "NaN" and skip if found.
    if anomaly_str.lower() != 'nan':
        anomaly = float(anomaly_str)
        decade = dec(year)
        
        # Accumulate sums and counts. 
        if decade not in dec_anomalies:
            dec_anomalies[decade] = 0.0
            dec_counts[decade] = 0
        dec_anomalies[decade] += anomaly
        dec_counts[decade] += 1

# Calculate and print the average temperature anomalies by decades. 
for decade in sorted(dec_anomalies.keys()):
    anomaly_mean = dec_anomalies[decade] / dec_counts[decade]
    print(f"{decade}s: {anomaly_mean:.2f}°F") # 2 decimal spaces for higher accuracy.
