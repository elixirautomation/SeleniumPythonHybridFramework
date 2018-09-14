[![BrowserStack Status](https://www.browserstack.com/automate/badge.svg?badge_key=WElIeEtLWlV3c09hdFprZXJlbFl0ZXpJVk8xQk9PT0J0K0s4L1BCVytFVT0tLXNVMFNWOHA2TllQMjBKWFhrTWpSK1E9PQ==--06ddf268990a113d732ff257cd70cb8a6fafd7c8)](https://www.browserstack.com/automate/public-build/WElIeEtLWlV3c09hdFprZXJlbFl0ZXpJVk8xQk9PT0J0K0s4L1BCVytFVT0tLXNVMFNWOHA2TllQMjBKWFhrTWpSK1E9PQ==--06ddf268990a113d732ff257cd70cb8a6fafd7c8)

# Selenium Python Hybrid Framework
## Selenium Hybrid Framework Development Using Python
- Page Object Model
- Allure Reporting
- Pytest, Unittest framework
- Data Driven (Pyexcel)
- Logging

### Initial Setup:
- Install and configure [Python3](https://www.python.org/downloads/)
- Setup your IDE (Preferably [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/#section=windows))
- Import cloned repository as project
- Install allure plugin for reporting

    - For Windows:
      - Run this command in powershell
          ```sh
            iex (new-object net.webclient).downloadstring('https://get.scoop.sh')
          ```
      - After installing scoop run this command
          ```sh
            scoop install allure
          ```

    - For Mac:
      - Run this command on terminal to install homebrew
          ```sh
            /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
          ```
      - After installing homebrew run this command
          ```sh
            brew install allure
          ```

    - For Linux:
      - Run following commands to install the allure on linux
          ```sh
            sudo apt-add-repository ppa:qameta/allure
            sudo apt-get update
            sudo apt-get install allure
          ```

- Install all required packages using this command
    ```sh
    pip install -r requirements.txt
    ```
- Add your test case under TestScripts folder
- Add your test data to TestData.xslx file
- Goto ConfigFiles -> execution_commands.txt and select specific command to execute the test case

### Example:
- Open pycharm terminal (Alt+F12) and run following command to invoke the chrome browser locally
    ```sh
    pytest TestScripts/test_manager.py --browser=local_chrome --alluredir ExecutionReports/ & allure serve ExecutionReports
    ```