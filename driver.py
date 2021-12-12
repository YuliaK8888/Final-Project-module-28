import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    path = str(request.fspath)
    # my_tmp_var = 123
    print(">>>" + request.fspath)
    driver = webdriver.Chrome('C:\chromewebdriver')
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
