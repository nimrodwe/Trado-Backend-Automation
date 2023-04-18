import Assets.Pages.Backend_utils as U
from Assets.Pages.Commons import Commons


class BranchesPage(Commons):

    ADD_BRANCH = (U.By.CSS_SELECTOR, 'div.dropMenu_option:nth-child(1) > span:nth-child(2)')
    BRANCH_NAME = (U.By.CSS_SELECTOR, 'span.input_input:nth-child(2) > div:nth-child(1) > input:nth-child(1)')
    ACTIVE_BRANCH = (U.By.CSS_SELECTOR, '.checkbox_checkboxCircle')
    ADD_NEW_BRANCH = (U.By.CSS_SELECTOR, '.form_submitBtn')
    SORT_BY_DATE = (U.By.CSS_SELECTOR, '.table_table > table:nth-child(1) > thead:nth-child(1) > tr:nth-child(1) > th:nth-child(6)')
    CREATED_BRANCH_NAME = (U.By.CSS_SELECTOR, '.table_table > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2)')

    def click_go_to_branches(self):
        self.wait_for(self.BRANCHES)
        self.click(self.BRANCHES)
        # Buffer for stupid site
        self.wait_for(self.SORT_BY_DATE)


    def go_to_create_branch(self):
        self.wait_for(self.PAGE_SETTING)
        self.click(self.PAGE_SETTING)
        self.wait_for(self.ADD_BRANCH)
        self.click(self.ADD_BRANCH)

    def create_branch(self, name, active):
        self.wait_for(self.ADD_NEW_BRANCH)
        if active:
            self.click(self.ACTIVE_BRANCH)
        self.insert(self.BRANCH_NAME, name)
        self.wait_for(self.ADD_NEW_BRANCH)
        self.click(self.ADD_NEW_BRANCH)
        U.sleep(2)

    def sort_by_date(self):
        self.wait_for(self.SORT_BY_DATE)
        self.click(self.SORT_BY_DATE)



