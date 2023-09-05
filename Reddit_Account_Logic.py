def create_reddit_account(email, username, password, cookies):
    try:
        # Create a new instance of the Chrome driver (you may need to configure it)
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
