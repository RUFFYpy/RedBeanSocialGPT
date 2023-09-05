import random

from create_accounts import Ig_Account_Logic, Reddit_Account_Logic, TikTok_Account_Logic
# Function to read account data from a text file
def read_account_data(file_path):
    accounts = []
    with open(file_path, 'r') as file:
        for line in file:
            username, password, email = line.strip().split(',')
            accounts.append((username, password, email))
    return accounts

# Function to read proxy data from a text file
def read_proxy_data(file_path):
    proxies = []
    with open(file_path, 'r') as file:
        for line in file:
            proxy = line.strip()
            proxies.append(proxy)
    return proxies

# Specify the path to your accounts.txt and proxy.txt files
accounts_file_path = 'accounts.txt'
proxy_file_path = 'proxy.txt'

# Read account data from the file
account_data = read_account_data(accounts_file_path)

# Read proxy data from the file
proxies = read_proxy_data(proxy_file_path)

# Initialize an empty list to store account details
account_cookies = []

# Loop through the account data and create accounts on each platform
for username, password, email in account_data:
    # Randomly select a proxy from the list
    selected_proxy = random.choice(proxies)

    # Create Instagram account
    instagram_result = create_instagram_account(email, username, password, account_cookies, selected_proxy)
    if instagram_result:
        print(f"Instagram account created: {username}")

    # Create Reddit account
    reddit_result = create_reddit_account(email, username, password, account_cookies, selected_proxy)
    if reddit_result:
        print(f"Reddit account created: {username}")

    # Create TikTok account
    tiktok_result = create_tiktok_account(email, username, password, account_cookies, selected_proxy)
    if tiktok_result:
        print(f"TikTok account created: {username}")

# At this point, account_cookies will contain the details of the created accounts
# You can use this data for further actions or storage
