import Assets.Pages.Backend_utils as U
from Assets.Pages.Commons import Commons


class OrdersPage(Commons):
    ORDER_LIST_FIRST_ITEM_NUMBER = (U.By.CSS_SELECTOR, '.table_table > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1)')

    def click_orders(self):
        U.sleep(1)
        self.click(self.ORDERS)
        U.sleep(4)

    def search_orders(self, search_term):
        self.insert(self.PAGE_SEARCH, search_term)
        U.sleep(3)

