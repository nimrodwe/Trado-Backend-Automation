import random
import allure
import pytest
import Assets.Pages.Branches_Page as BP
from Assets.Pages.Commons import LogIn


@allure.epic('Test Branches')
@allure.id(43)
@allure.title("Create new branch")
@allure.description('Creating a new branch works as intended')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_branch_valid(driver):
    branch = BP.BranchesPage(driver)
    login = LogIn(driver)
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Navigating to branch area'):
        branch.click_go_to_branches()
    with allure.step('Navigating to the add new branch page'):
        branch.go_to_create_branch()
    with allure.step('Creating new branch'):
        testbranch = f'Bananabranch{random.randint(1, 99)}'
        branch.create_branch(testbranch, False)
    with allure.step('Asserting new branch has been created'):
        supposed_branch = branch.get_text(branch.CREATED_BRANCH_NAME)
        assert supposed_branch == testbranch


