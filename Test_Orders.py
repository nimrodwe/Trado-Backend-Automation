import allure
import pytest
import Assets.Pages.Orders_Page as OP
from Assets.Pages.Commons import LogIn


@allure.epic('Test Orders')
@allure.id(24)
@allure.title("Navigate to orders page")
@allure.description('Orders page is displayed')
@allure.severity(allure.severity_level.NORMAL)
def test_orders_page(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Asserting orders page has been reached'):
        assert driver.current_url == 'http://qa-admin.trado.co.il/#/orders'


@allure.epic('Test Orders')
@allure.id(25)
@allure.title("Search for an order")
@allure.description('Orders is displayed in list')
@allure.severity(allure.severity_level.NORMAL)
def test_orders_page(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('searching for specific order (690)'):
        orders.search_orders('690')
    with allure.step('Asserting first order is the desired order'):
        first_order_id = orders.get_text(orders.ORDER_LIST_FIRST_ITEM_NUMBER)
        assert first_order_id == '690'

@allure.epic('Test Orders')
@allure.id(26)
@allure.title("Move to next page")
@allure.description('Next page is displayed')
@allure.severity(allure.severity_level.NORMAL)
def test_orders_next(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step(""):


