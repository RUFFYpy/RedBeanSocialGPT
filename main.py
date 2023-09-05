import tkinter as tk
from tkinter import ttk
import csv
import random

# Your CapMonster and API integration code would go here

def generate_accounts(num_accounts, selected_platforms):
    # Generate random account data (placeholder)
    accounts = []
    for _ in range(num_accounts):
        username = f"user{random.randint(1000, 9999)}"
        password = f"password{random.randint(1000, 9999)}"
        email = f"{username}@example.com"
        accounts.append([username, password, email])

    # Save account data to a CSV file
    with open('accounts.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Username', 'Password', 'Email'])
        writer.writerows(accounts)

def main():
    # Step 1: Create a GUI
    root = tk.Tk()
    root.title("Account Generation Script")

    num_accounts_label = ttk.Label(root, text="Number of Accounts:")
    num_accounts_label.pack()
    num_accounts_entry = ttk.Entry(root)
    num_accounts_entry.pack()

    # ... (Create checkboxes for platforms as in previous example)

    def generate_button_clicked():
        num_accounts = int(num_accounts_entry.get())
        selected_platforms = ["Instagram", "Reddit", "TikTok"]  # Placeholder for selected platforms
        generate_accounts(num_accounts, selected_platforms)

    generate_button = ttk.Button(root, text="Generate Accounts", command=generate_button_clicked)
    generate_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
