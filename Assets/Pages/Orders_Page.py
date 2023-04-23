import Assets.Pages.Backend_utils as U
from Assets.Pages.Commons import Commons
import re


class OrdersPage(Commons):
    ORDER_LIST_FIRST_ITEM_NUMBER = (U.By.CSS_SELECTOR, '.table_table > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)')
    FIRST_ORDER_IN_LIST = (U.By.CSS_SELECTOR, '.table_table > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')
    NEXT_ARROW = (U.By.CSS_SELECTOR, '.fa-angle-right')
    PREVIOUS_ARROW = (U.By.CSS_SELECTOR, '.fa-angle-left')
    SECOND_PAGE_INDICATOR = (U.By.CSS_SELECTOR, 'span.paging_paginationNum:nth-child(4)')
    FIRST_PAGE_INDICATOR = (U.By.CSS_SELECTOR, 'span.paging_paginationNum:nth-child(1)')
    ORDER_UI = (U.By.CSS_SELECTOR,'.modal_modal')
    ORDERS_ADDRESS = (U.By.CSS_SELECTOR, 'a.orderInfo_infoItem:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
    GOOGLE_DIRECTIONS = (U.By.CSS_SELECTOR, 'div.etWJQ:nth-child(1) > button:nth-child(1) > span:nth-child(1)')
    ORDERS_PHONE = (U.By.CSS_SELECTOR, 'a.orderInfo_infoItem:nth-child(2) > div:nth-child(2) > div:nth-child(1)')
    FIRST_PRODUCT_MISSING_BTN = (U.By.CSS_SELECTOR, 'div.product_product:nth-child(1) > div:nth-child(3) > div:nth-child(1)')
    ORDERS_AMOUNT = (U.By.CSS_SELECTOR, 'div.product_product:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(2)')
    ORDER_AMOUNT_1 = (U.By.CSS_SELECTOR, 'div.input_autocompleteItem:nth-child(2)')
    ORDERS_AMOUNT_4 = (U.By.CSS_SELECTOR, 'div.input_autocompleteItem:nth-child(5)')
    ORDER_IN_CART = (U.By.CSS_SELECTOR, 'div.product_product:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(2) > span:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
    ORDER_PRICE = (U.By.CSS_SELECTOR, 'div.orderSummary_row:nth-child(3) > strong:nth-child(2)')
    ORDER_WEIGHT = (U.By.CSS_SELECTOR, 'div.orderSummary_row:nth-child(5) > input:nth-child(2)')
    SEND_TO_DELIVERY = (U.By.CSS_SELECTOR, '.button_button')
    READY_ORDERS = (U.By.CSS_SELECTOR, 'span.tabs_tab:nth-child(2)')
    READY_ORDERS_CHART = (U.By.CSS_SELECTOR, '.table_table > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(3)')
    IN_DELIVERY = (U.By.CSS_SELECTOR, 'span.tabs_tab:nth-child(3)')
    ORDER_END = (U.By.CSS_SELECTOR, 'span.tabs_tab:nth-child(4)')

    def click_in_delivery(self):
        U.sleep(3)
        self.click(self.IN_DELIVERY)

    def click_ready_orders(self):
        U.sleep(3)
        self.click(self.READY_ORDERS)

    def click_order_end(self):
        U.sleep(3)
        self.click(self.ORDER_END)

    def click_orders(self):
        U.sleep(1)
        self.click(self.ORDERS)
        U.sleep(4)

    def click_address(self):
        self.click(self.ORDERS_ADDRESS)
        U.sleep(4)

    def click_phone(self):
        self.click(self.ORDERS_PHONE)
        U.sleep(4)

    def click_product_missing(self):
        self.click(self.FIRST_PRODUCT_MISSING_BTN)
        U.sleep(2)

    def add_one_item_to_order(self):
        self.click(self.ORDERS_AMOUNT)
        U.sleep(1)
        self.click(self.ORDER_AMOUNT_1)
        U.sleep(1)

    def add_four_items_to_order(self):
        self.click(self.ORDERS_AMOUNT)
        U.sleep(1)
        self.click(self.ORDERS_AMOUNT_4)
        U.sleep(10)

    def click_first_order(self):
        self.wait_for(self.FIRST_ORDER_IN_LIST)
        self.click(self.FIRST_ORDER_IN_LIST)
        U.sleep(1)

    def search_orders(self, search_term):
        self.insert(self.PAGE_SEARCH, search_term)
        U.sleep(3)

    def next_page(self):
        self.click(self.NEXT_ARROW)
        U.sleep(2)

    def previous_page(self):
        self.click(self.PREVIOUS_ARROW)
        U.sleep(2)

    def get_decimal_number(self, locator):
        self.wait_for(locator)
        txt = self.get_text(locator)
        count = re.findall(r'\d+\.\d+', f'{txt}')
        for i in count:
            num = i
            return float(num)

