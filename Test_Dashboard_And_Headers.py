import allure
import pytest
from Assets.Pages.Commons import DashboardAndHeaders


@allure.epic('Test Departments')
@allure.id(43)
@allure.title("Create new department (no image)")
@allure.description('Creating a new department works as intended')
@allure.severity(allure.severity_level.CRITICAL)