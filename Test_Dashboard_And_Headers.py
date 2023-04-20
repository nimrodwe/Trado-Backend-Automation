import allure
import pytest
from Assets.Pages.Commons import DashboardAndHeaders
from Assets.Pages.Commons import LogIn


@allure.epic('Test Header')
@allure.id(6)
@allure.title("Click hamburger button")
@allure.description('Menu will close (open by default)')
@allure.severity(allure.severity_level.NORMAL)
def test_click_menu_button(driver):
    login = LogIn(driver)
    dashing = DashboardAndHeaders(driver)
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Clicking the menu button'):
        dashing.click_burger_menu()
    with allure.step('Asserting menu has closed'):
        # Menu is open by default when logging in
        class_name = dashing.get_class(dashing.IS_MENU_OPEN)
        # Class name is not empty when menu is visible
        assert class_name == ""


@allure.epic('Test Header')
@allure.id(7)
@allure.title("Click Logo")
@allure.description('Redirected to dashboard page')
@allure.severity(allure.severity_level.TRIVIAL)
def test_click_logo(driver):
    login = LogIn(driver)
    dashing = DashboardAndHeaders(driver)
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Going to a different area'):
        # On user login we start in dashboard by default, so you cannot see the results if you are already in dashboard
        login.click(login.BRANCHES)
    with allure.step('Clicking the logo button'):
        dashing.click_logo()
    with allure.step('Asserting Dashboard has been reached'):
        assert driver.current_url == 'http://qa-admin.trado.co.il/#/'


@allure.epic('Test Dashboard')
@allure.id(8)
@allure.title("Switch Stores")
@allure.description('Stores are switched')
@allure.severity(allure.severity_level.NORMAL)
def test_switch_stores(driver):
    login = LogIn(driver)
    dashing = DashboardAndHeaders(driver)
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Switching store'):
        # The default store which is logged into is TRADO
        dashing.switch_store(dashing.DANI_MAMTAKIM)
    with allure.step('Asserting the store has been switched'):
        dani_mamatakim = dashing.get_text(dashing.STORE_SELECTOR)
        assert dani_mamatakim == 'דני ממתקים'


@allure.epic('Test Dashboard')
@allure.id(9)
@allure.title("Validate dashboard page is loaded")
@allure.description('Dashboard main content is displayed')
@allure.severity(allure.severity_level.CRITICAL)
def test_dashboard_exists(driver):
    login = LogIn(driver)
    dashing = DashboardAndHeaders(driver)
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Waiting for dashboard to load'):
        dashing.wait_for_invisibility(dashing.LOADING)



