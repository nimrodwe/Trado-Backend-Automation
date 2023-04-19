import random
import allure
import pytest
import Assets.Pages.Departments_page as BP
from Assets.Pages.Commons import LogIn
import Assets.Pages.MongoDB_requests as R


@allure.epic('Test Departments')
@allure.id(43)
@allure.title("Create new department (no image)")
@allure.description('Creating a new department works as intended')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_department_valid(driver):
    department = BP.DepartmentsPage(driver)
    login = LogIn(driver)
    request = R.MongoRequests()
    with allure.step('Logging in'):
        login.log_in('1951111111', '1234', False)
    with allure.step('Navigating to branch area'):
        department.click_go_to_department()
    with allure.step('Navigating to the add new branch page'):
        department.go_to_create_department()
    with allure.step('Creating new branch'):
        test_branch = f'BananaDogDepartment{random.randint(1, 9999)}'
        department.create_department(test_branch, False)
    with allure.step('Asserting new branch has been created in '):
        name_in_db = request.find_existing_branch(test_branch)
        supposed_branch = department.get_text(department.CREATED_DEPARTMENT_NAME)
        assert supposed_branch == test_branch
        assert name_in_db == test_branch



