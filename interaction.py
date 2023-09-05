import os
import csv
from Ig_Account_Logic import create_instagram_account
from Reddit_Account_Logic import create_reddit_account
from TikTok_Account_Logic import create_tiktok_account

# Function to read account data from a text file
def read_account_data(file_path):
    accounts = []
    with open(file_path, 'r') as file:
        for line in file:
            username, password, email = line.strip().split(',')
            accounts.append((username, password, email))
    return accounts

# Specify the paths to your account data and CSV file
accounts_file_path = 'accounts.txt'
csv_file_path = 'accounts.csv'

# Initialize an empty list to store account details
account_credentials = []

# Loop through the account data and create accounts on each platform
account_data = read_account_data(accounts_file_path)

for username, password, email in account_data:
    # Create Instagram account
    instagram_result = create_instagram_account(email, username, password)
    if instagram_result:
        account_credentials.append([email, username, password])

    # Create Reddit account
    reddit_result = create_reddit_account(email, username, password)
    if reddit_result:
        account_credentials.append([email, username, password])

    # Create TikTok account
    tiktok_result = create_tiktok_account(email, username, password)
    if tiktok_result:
        account_credentials.append([email, username, password])

# Save account credentials to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Email', 'Username', 'Password'])
    writer.writerows(account_credentials)

print(f"Account credentials saved to {csv_file_path}")
