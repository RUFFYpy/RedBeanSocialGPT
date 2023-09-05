from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def create_instagram_account(email, username, password, cookies):
    try:
        # Create a new instance of the Chrome driver (you may need to configure it)
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

        # Assuming account creation is successful, add the account details to cookies
        account_details = {
            "email": email,
            "username": username,
            "password": password,
            # Add other relevant details if necessary
        }
        cookies.append(account_details)

        # Close the browser
        driver.quit()

        return True

    except Exception as error:
        return False, error
