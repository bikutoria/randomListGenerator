import csv
from faker import Faker
import random
import os
from datetime import datetime, timedelta
import string

fake = Faker()

# Date definition
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

start = datetime(2022, 12, 1)
end = datetime(2023, 12, 31)

#Client ID definition
def generate_random_string():
    parts = []
    for i in [8, 4, 4, 4, 12]:
        part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=i))
        parts.append(part)
    return '-'.join(parts)


# Generate 300 rows of data
rows = []
for _ in range(300):
    browser_type = random.choice(['Chrome', 'Edge', 'Safari', 'Brave', 'Firefox'])
    language = random.choice(['en_US', 'fr_ FR', 'en_CA', 'fr_CA'])
    random_dates = [random_date(start, end).isoformat() for _ in range(1)]
    #client_id = random.randint(10000, 99999)
    client_id = [generate_random_string() for _ in range(1)]

    # Create a row with 50 columns
    row = [browser_type, language, random_dates, client_id]
    rows.append(row)

# Get the desktop directory
desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

# Get the current timestamp
current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# Create the string variable
filename = f"random_data_{current_timestamp}.csv"

# Specify the CSV file path on the desktop
csv_file_path = os.path.join(desktop_path, filename)

# Write to CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['browserType', 'language', 'clientTimestamp', 'clientId'])
    csv_writer.writerows(rows) 