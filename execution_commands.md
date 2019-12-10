#### Local Commands

##### --environment={staging, prod} --browser={local_chrome, local_firefox}

```sh
py.cleanup -p && py.test --environment=staging --browser=local_chrome --alluredir ExecutionReports/
py.cleanup -p && py.test --environment=prod --browser=local_firefox --alluredir ExecutionReports/

```

#### Run Test Suites (Mark your test cases with test suites)
```sh
py.cleanup -p && py.test -m smoke --environment=staging --browser=local_chrome --alluredir ExecutionReports/
py.cleanup -p && py.test -m regression --environment=staging --browser=local_chrome --alluredir ExecutionReports/
```

#### Grid Specific Commands

##### --environment={staging, prod} --browser={chrome, firefox, safari}

##### MAC

```sh
py.cleanup -p && py.test --platform=MAC --browser=chrome --environment=staging --alluredir ExecutionReports/
py.cleanup -p && py.test --platform=MAC --browser=safari --environment=staging --alluredir ExecutionReports/
py.cleanup -p && py.test --platform=MAC --browser=firefox --environment=staging --alluredir ExecutionReports/
```

##### WINDOWS

```sh
py.cleanup -p && py.test --platform=WINDOWS --browser=chrome --environment=staging --alluredir ExecutionReports/
py.cleanup -p && py.test --platform=WINDOWS --browser=edge --environment=staging --alluredir ExecutionReports/
py.cleanup -p && py.test --platform=WINDOWS --browser=firefox --environment=staging --alluredir ExecutionReports/
```

#### Cloud Grid Specific Commands
##### --environment={staging, prod} --browser={sauce, browserstack_mobile, browserstack_web}

```sh
py.cleanup -p && py.test --browser=sauce --environment=staging --alluredir ExecutionReports/
py.cleanup -p && py.test --browser=browserstack_mobile --environment=staging --alluredir ExecutionReports/
py.cleanup -p && py.test --browser=browserstack_web --environment=staging --alluredir ExecutionReports/
```

#### Trigger Allure Reports

```sh
allure serve ExecutionReports
```

