# create_accounts.py
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Function to create an Instagram account
def create_instagram_account(email, username, password, proxies=None):
    try:
        # Initialize a webdriver with a randomly selected proxy (if proxies are provided)
        if proxies:
            proxy = random.choice(proxies)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={proxy}')
            driver = webdriver.Chrome(executable_path='path_to_chromedriver', options=chrome_options)
        else:
            # Create a webdriver without a proxy
            driver = webdriver.Chrome(executable_path='path_to_chromedriver')

        # Navigate to the Instagram signup page
        driver.get("https://www.instagram.com/accounts/emailsignup/")

        # Fill in the signup form
        email_field = driver.find_element_by_name("emailOrPhone")
        email_field.send_keys(email)
        full_name_field = driver.find_element_by_name("fullName")
        full_name_field.send_keys(username)
        username_field = driver.find_element_by_name("username")
        username_field.send_keys(username)
        password_field = driver.find_element_by_name("password")
        password_field.send_keys(password)

        # Submit the form
        submit_button = driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()

        # Handle any additional steps like email confirmation or captcha if needed

        # Assuming account creation is successful

        # Close the browser
        driver.quit()

        return True

    except Exception as error:
        return False, error

# Function to create a Reddit account
def create_reddit_account(email, username, password, proxies=None):
    try:
        # Initialize a webdriver with a randomly selected proxy (if proxies are provided)
        if proxies:
            proxy = random.choice(proxies)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={proxy}')
            driver = webdriver.Chrome(executable_path='path_to_chromedriver', options=chrome_options)
        else:
            # Create a webdriver without a proxy
            driver = webdriver.Chrome(executable_path='path_to_chromedriver')

        # Navigate to the Reddit signup page
        driver.get("https://www.reddit.com/register")

        # Fill in the signup form
        email_field = driver.find_element_by_name("email")
        email_field.send_keys(email)
        username_field = driver.find_element_by_name("user")
        username_field.send_keys(username)
        password_field = driver.find_element_by_name("passwd")
        password_field.send_keys(password)

        # Submit the form
        submit_button = driver.find_element_by_name("submit")
        submit_button.click()

        # Handle any additional steps like captcha if needed

        # Assuming account creation is successful

        # Close the browser
        driver.quit()

        return True

    except Exception as error:
        return False, error

# Function to create a TikTok account
def create_tiktok_account(email, username, password, proxies=None):
    try:
        # Initialize a webdriver with a randomly selected proxy (if proxies are provided)
        if proxies:
            proxy = random.choice(proxies)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument(f'--proxy-server={proxy}')
            driver = webdriver.Chrome(executable_path='path_to_chromedriver', options=chrome_options)
        else:
            # Create a webdriver without a proxy
            driver = webdriver.Chrome(executable_path='path_to_chromedriver')

        # Navigate to the TikTok signup page
        driver.get("https://www.tiktok.com/signup")

        # Fill in the signup form
        email_field = driver.find_element_by_name("email")
        email_field.send_keys(email)
        username_field = driver.find_element_by_name("username")
        username_field.send_keys(username)
        password_field = driver.find_element_by_name("password")
        password_field.send_keys(password)

        # Submit the form
        submit_button = driver.find_element_by_xpath("//button[@type='submit']")
        submit_button.click()

        # Handle any additional steps like phone verification or captcha if needed

        # Assuming account creation is successful

        # Close the browser
        driver.quit()

        return True

    except Exception as error:
        return False, error
