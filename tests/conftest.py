import pytest
from selenium import webdriver
# variable global ***
driver = None

@pytest.fixture(scope="class")
def config(request):
    #Utilizar una variable global dento de la funcion ***
    global driver
    #Asigna el valor de la variable a la global de la clase
    driver = webdriver.Chrome(executable_path='D://DEV//chromedriver.exe')
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                _capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

    def _capture_screenshot(name):
        # utiliza el valor de la variable global que se inicializo en config
        driver.get_screenshot_as_file(name)

