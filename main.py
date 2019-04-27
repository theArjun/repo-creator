# Importing webdriver
from selenium import webdriver
# Options for headless mode in this context
from selenium.webdriver.chrome.options import Options
# Exceptions
from selenium.common.exceptions import NoSuchElementException, WebDriverException
# Hides password while
import getpass
# For copying link to clipboard
import pyperclip

# For opening browser in headless mode
options = Options()
options.headless = True

try:
    browser = webdriver.Chrome(
        options=options, executable_path="../driver/chromedriver.exe")
except WebDriverException:
    browser = webdriver.Firefox(
        options=options, executable_path="../driver/geckodriver.exe")

# Not needed while opening in headless mode.
# browser.maximize_window()

browser.get("https://github.com/login")

try:
    # Getting the forms
    username = browser.find_element_by_name("login")
    password = browser.find_element_by_name("password")
    sign_in = browser.find_element_by_name("commit")
    sign_in.is_displayed()

    uname = input("Enter username/email : ").rstrip()
    username.send_keys(uname)

    pwd = getpass.getpass("Enter password : ")
    password.send_keys(pwd)

    sign_in.click()

    if browser.title == 'GitHub':
        browser.get("https://github.com/new")

        # Repository Name
        repo_name = input("\nEnter repository name : ")
        browser.find_element_by_id("repository_name").send_keys(repo_name)

        # Repository Description
        repo_description = input("\nEnter description : ")
        browser.find_element_by_id(
            "repository_description").send_keys(repo_description)

        # Initialize public or private repository
        privacy = True if int(
            input("\nEnter 1 for private, 0 for public repository : ")) == 1 else False
        if privacy:
            browser.find_element_by_xpath("//*[@value = 'private']").click()
        else:
            browser.find_element_by_xpath("//*[@value = 'public']").click()

        # Initialize this repository with a README
        readme_init = True if int(
            input("\nEnter 1 initializing repository with readme : ")) == 1 else False
        if readme_init:
            browser.find_element_by_xpath(
                "//*[@id='repository_auto_init']").click()

        print("Doing magic stuffs ...")

        # Clicks create repository.
        create_repo = browser.find_elements_by_css_selector(
            "button.btn:nth-child(12)")[0]
        create_repo.click()

    else:
        print("Error logging in !")


except NoSuchElementException:
    print("Error occured. Please enter correct details.")

else:
    github_repo_link_https = "https://github.com/" + uname + "/" + repo_name + ".git"
    github_repo_link_ssh = "git@github.com:" + uname + "/" + repo_name + ".git"

    print("\n1. HTTPS - {}".format(github_repo_link_https))
    print("2. HTTPS - {}".format(github_repo_link_ssh))

    link = int(input(
        "If you want in clipboard,\nPress 1 for HTTPS, 2 for SSH Github Repo Link : "))
    if link == 1:
        pyperclip.copy(github_repo_link_https)
    elif link == 2:
        pyperclip.copy(github_repo_link_ssh)

    print("\nLink is copied on Clipboard.")

finally:
    print("\nStalk me on GitHub : https://github.com/thearjun")
