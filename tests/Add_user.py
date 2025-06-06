# tests/test_add_user.py
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

USERNAME = "Admin"
PASSWORD = "admin123"

@pytest.fixture(scope="function")
def login(page: Page):
    login_page = LoginPage(page)
    login_page.login(USERNAME, PASSWORD)
    return AdminPage(page)

def test_add_user(page: Page, login):
    admin_page = login
    admin_page.navigate_to_admin()
    admin_page.add_user(
        employee_name="Linda Anderson",
        username="testuser123",
        password="TestPass123!",
        role="ESS",
        status="Enabled"
    )
