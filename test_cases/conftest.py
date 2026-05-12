import pytest
from selenium import webdriver
# import undetected_chromedriver as uc

def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default="chrome",
                     help="Specify the browser: chrome or firefox or edge or brave")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
        # driver = uc.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        # driver = uc.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()
    elif browser == "edge":
        driver = webdriver.Edge()
        driver.maximize_window()
        # driver = uc.Chrome(options=options)
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

    else:
        raise ValueError("Unsupported browser")
    return driver
    # options = uc.ChromeOptions()
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver = uc.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()