import allure
import pytest
from Assets.Pages.Commons import LogIn
import Assets.Pages.Backend_utils as U


@allure.epic('Test Login')
@allure.id(1)
@allure.title("Enter valid login")
@allure.description('Reached the dashboard')
@allure.severity(allure.severity_level.CRITICAL)
def test_valid_login(driver):
    login = LogIn(driver)
    with allure.step('Logging in with valid credentials'):
        login.log_in('1951111111', '1234', False)
    with allure.step('asserting dashboard page has been reached'):
        assert driver.current_url == 'http://qa-admin.trado.co.il/#/'


@allure.epic('Test Login')
@allure.id(2)
@allure.title("Invalid login(phone number)")
@allure.description('Error message displayed')
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login_number(driver):
    login = LogIn(driver)
    with allure.step('Logging in with invalid phone number'):
        login.log_in('0000000000', '0000', False)
    with allure.step('Asserting error is visible'):
        assert login.wait_for(login.NO_SUCH_USER_ERROR)


@allure.epic('Test Login')
@allure.id(3)
@allure.title("Invalid login(code)")
@allure.description('Error message displayed')
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login_code(driver):
    login = LogIn(driver)
    with allure.step('Logging in with invalid code'):
        login.log_in('2222222222', '000000', False)
    with allure.step('Asserting error is visible'):
        err = login.get_text(login.NO_SUCH_USER_ERROR)
        assert err == 'faild to login undefined'


@allure.epic('Test Login')
@allure.id(4)
@allure.title("Validate secure password visual")
@allure.description('Password is encrypted visually')
@allure.severity(allure.severity_level.CRITICAL)
def test_password_visibility(driver):
    login = LogIn(driver)
    with allure.step('Logging in with invalid phone number'):
        passwd = login.eye_visibility('2222222222', '000000')
        assert passwd == '000000'


@allure.epic('Test Login')
@allure.id(5)
@allure.title("Validate remember me login")
@allure.description('Site will remember user for next time')
@allure.severity(allure.severity_level.CRITICAL)
def test_password_saved(driver):
    login = LogIn(driver)
    with allure.step('Logging in with remember me'):
        login.log_in('1951111111', '1234', True)
    with allure.step('Logging out'):
        ac = U.ac(driver)
        U.sleep(2)
        invis = login.find_logout()
        ac.move_to_element(invis).perform()
        invis.click()
    with allure.step('Asserting number has been remembered'):
        login.wait_for(login.LOGIN)
        num = login.get_text(login.LOGIN)
        assert num == '1951111111'




