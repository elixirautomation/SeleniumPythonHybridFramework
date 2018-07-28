from SupportLibraries.driver_factory import DriverFactory
import pytest


@pytest.fixture(scope="function")
def method_level_setup(request, browser):
    print("method_level_setup: Running method level setup.")
    df = DriverFactory(browser)
    driver = df.get_driver_instance()

    # Login the application directly from here
    # login_page = LoginPage(driver)
    # login_page.login("abhilash04sharma@gmail.com", "sonetel@2018")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("method_level_setup: Running method level teardown.")
    driver.delete_all_cookies()
    driver.quit()


@pytest.fixture(scope="class")
def one_time_set_up(request, browser):
    print("OneTimeSetup: Running class level setup.")
    df = DriverFactory(browser)
    driver = df.get_driver_instance()

    # Login the application directly from here
    # login_page = LoginPage(driver)
    # login_page.login("abhilash04sharma@gmail.com", "sonetel@2018")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("OneTimeTeardown: Running class level teardown.")


def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser Type")
    parser.addoption("--os_type", help="Operating System Type")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--os_type")


