# RAFT - Reusable Automation Framework For Testing

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
- Add your test data to TestData_Prod.xslx/ TestData_Staging.xslx file
- Goto execution_commands.md and select specific command to execute the test case

### Example:
- Open pycharm terminal (Alt+F12) and run following command to invoke the chrome browser locally on staging environment
    ```sh
    py.cleanup -p && py.test --environment=staging --browser=local_chrome --alluredir ExecutionReports/
    ```
- Trigger Allure Reports
    ```sh
    allure serve ExecutionReports/
    ```