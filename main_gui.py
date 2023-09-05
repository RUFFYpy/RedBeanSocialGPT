import tkinter as tk
from tkinter import ttk
from Ig_Account_Logic import create_instagram_account
from Reddit_Account_Logic import create_reddit_account
from TikTok_Account_Logic import create_tiktok_account

def generate_button_clicked():
    num_accounts = int(num_accounts_entry.get())
    selected_platforms = ["Instagram", "Reddit", "TikTok"]  # Placeholder for selected platforms
    
# Loop through the number of accounts to create
    for _ in range(num_accounts):
        username = f"user{_}"
        password = f"password{_}"
        email = f"{username}@example.com"

        # Create accounts for selected platforms
        for platform in selected_platforms:
            if platform == "Instagram":
                create_instagram_account(email, username, password)
            elif platform == "Reddit":
                create_reddit_account(email, username, password)
            elif platform == "TikTok":
                create_tiktok_account(email, username, password)

# Create the main application window
root = tk.Tk()
root.title("Account Generation Script")

# Label and Entry for specifying the number of accounts
num_accounts_label = ttk.Label(root, text="Number of Accounts:")
num_accounts_label.pack()

num_accounts_entry = ttk.Entry(root)
num_accounts_entry.pack()

# Button to generate accounts
generate_button = ttk.Button(root, text="Generate Accounts", command=generate_button_clicked)
generate_button.pack()

# Start the GUI event loop
root.mainloop()
