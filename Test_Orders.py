import allure
import pytest
import Assets.Pages.Orders_Page as OP
from Assets.Pages.Commons import LogIn


@allure.epic('Test Orders')
@allure.id(23)
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
@allure.id(24)
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
@allure.id(25)
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
    with allure.step("Navigating to the next page"):
        orders.next_page()
    with allure.step('Asserting next page is displayed'):
        classes = orders.get_class(orders.SECOND_PAGE_INDICATOR)
        assert classes == 'paging_paginationNum paging_active'


@allure.epic('Test Orders')
@allure.id(26)
@allure.title("Move to previous page")
@allure.description('Previous page is displayed')
@allure.severity(allure.severity_level.NORMAL)
def test_orders_previous(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step("Navigating to the next page"):
        orders.next_page()
    with allure.step('Navigating to the previous page'):
        orders.previous_page()
    with allure.step('Asserting next page is displayed'):
        classes = orders.get_class(orders.FIRST_PAGE_INDICATOR)
        assert classes == 'paging_paginationNum paging_active'


@allure.epic('Test Orders')
@allure.id(27)
@allure.title("Open order")
@allure.description('Order card is displayed')
@allure.severity(allure.severity_level.NORMAL)
def test_open_order(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Clicking first visible order'):
        orders.click_first_order()
    with allure.step('Asserting first order is displayed'):
        assert orders.wait_for(orders.ORDER_UI)


@allure.epic('Test Orders')
@allure.id(28)
@allure.title("Click address button in order card")
@allure.description('Google maps tab opens')
@allure.severity(allure.severity_level.NORMAL)
def test_open_order_address(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Clicking first visible order'):
        orders.click_first_order()
        orders.wait_for(orders.ORDER_UI)
    with allure.step('Clicking on address'):
        trado_tab = driver.current_window_handle
        orders.click_address()
    with allure.step('Switching to google maps tab'):
        orders.switch_tabs(trado_tab)
    with allure.step('Wating for google directions (asserting we reached the site'):
        assert orders.wait_for(orders.GOOGLE_DIRECTIONS)
    with allure.step('Cleanup'):
        driver.close()
        driver.switch_to.window(trado_tab)


@allure.epic('Test Orders')
@allure.id(29)
@allure.title("Click on order phone number")
@allure.description('Phone number message opens')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail('NO WAY TO TEST WITHOUT EXTERNAL PACKAGES')
def test_open_phone_number(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Clicking first visible order'):
        orders.click_first_order()
        orders.wait_for(orders.ORDER_UI)
    with allure.step('Clicking on phone number'):
        orders.click_phone()
        orders.wait_for_alert()
        alert = driver.switch_to.alert
        alert.dismiss()


@allure.epic('Test Orders')
@allure.id(30)
@allure.title("Click on order mail button")
@allure.description('mail alert  opens')
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail('NO WAY TO TEST WITHOUT EXTERNAL PACKAGES')
def test_open_mail_options(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Clicking first visible order'):
        orders.click_first_order()
        orders.wait_for(orders.ORDER_UI)
    with allure.step('FAIL'):
        orders.wait_for_alert()


@allure.epic('Test Orders')
@allure.id(31)
@allure.title("Click missing button in order card")
@allure.description('Order card image turns to gray color')
@allure.severity(allure.severity_level.NORMAL)
def test_item_missing_btn(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Clicking first visible order'):
        orders.click_first_order()
        orders.wait_for(orders.ORDER_UI)
    with allure.step('Clicking missing product button'):
        orders.click_product_missing()
    with allure.step('Asserting product is marked as missing'):
        class_name = orders.get_class(orders.FIRST_PRODUCT_MISSING_BTN)
        assert class_name == 'product_btn product_missing'
    with allure.step('Restoring item amount fo r next test'):
        orders.add_one_item_to_order()


@allure.epic('Test Orders')
@allure.id(32)
@allure.title("Add quantity in order card")
@allure.description('Order quantity is changed')
@allure.severity(allure.severity_level.NORMAL)
def test_add_quantity(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Clicking first visible order'):
        orders.click_first_order()
        orders.wait_for(orders.ORDER_UI)
        orders.add_one_item_to_order()
        bfr = orders.get_decimal_number(orders.ORDER_PRICE)
    with allure.step('Adding items to order'):
        orders.add_four_items_to_order()
        aftr = orders.get_decimal_number(orders.ORDER_PRICE)
        assert bfr < aftr


@allure.epic('Test Orders')
@allure.id(33)
@allure.title("Click button transfer to ready for shipping")
@allure.description('Product moves to ready for shipping list')
@allure.severity(allure.severity_level.NORMAL)
def test_order_to_shipping(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Clicking first visible order'):
        orders.click_first_order()
        orders.wait_for(orders.ORDER_UI)
        orders.insert(orders.ORDER_WEIGHT, '125')
    with allure.step('Adding items to order'):
        orders.click(orders.SEND_TO_DELIVERY)
        orders.click_ready_orders()
    with allure.step('Finding the order in the ready page'):
        pass  # FAILS BEFORE THIS PART


@allure.epic('Test Orders')
@allure.id(34)
@allure.title("Click מוכנה button")
@allure.description('Different product list is displayed')
@allure.severity(allure.severity_level.NORMAL)
def test_ready_orders_page(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Going to ready orders'):
        orders.click_ready_orders()
    with allure.step('asserting ready order is visible'):
        ord_id = orders.get_class(orders.READY_ORDERS)
        assert ord_id == 'tabs_tab tabs_active'


@allure.epic('Test Orders')
@allure.id(37)
@allure.title('Click "במשלוח" button')
@allure.description('Different product list is displayed')
@allure.severity(allure.severity_level.NORMAL)
def test_in_delivery_orders_page(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Going to in delivery orders'):
        orders.click_in_delivery()
    with allure.step('asserting ready order is visible'):
        ord_id = orders.get_class(orders.IN_DELIVERY)
        assert ord_id == 'tabs_tab tabs_active'


@allure.epic('Test Orders')
@allure.id(40)
@allure.title('Click "סיום" button')
@allure.description('Different product list is displayed')
@allure.severity(allure.severity_level.NORMAL)
def test_end_order_page(driver):
    orders = OP.OrdersPage(driver)
    login = LogIn(driver)
    with allure.step("Logging in"):
        login.log_in('1951111111', '1234', False)
    with allure.step("Navigating to order page"):
        orders.click_orders()
    with allure.step('Going to end orders'):
        orders.click_order_end()
    with allure.step('asserting end orders is visible'):
        ord_id = orders.get_class(orders.ORDER_END)
        assert ord_id == 'tabs_tab tabs_active'


