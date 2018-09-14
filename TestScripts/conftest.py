from SupportLibraries.driver_factory import DriverFactory
import pytest


@pytest.fixture(scope="class")
def before_class(request, browser, platform):
    print("method_level_setup: Running method level setup.")
    df = DriverFactory(browser, platform)
    driver = df.get_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    print("method_level_setup: Running method level teardown.")
    driver.delete_all_cookies()
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser Type")
    parser.addoption("--platform", help="Operating System Type")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def platform(request):
    return request.config.getoption("--platform")