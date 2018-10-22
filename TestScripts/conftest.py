from SupportLibraries.driver_factory import DriverFactory
import pytest


@pytest.fixture(scope="session")
def get_driver(request, browser, platform):
    print("session_level_setup: Running session level setup.")
    df = DriverFactory(browser, platform)
    driver = df.get_driver_instance()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield
    print("session_level_setup: Running session level teardown.")
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