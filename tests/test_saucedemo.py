import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"
VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"


@pytest.fixture
def driver():
    """Open a fresh browser per test and always close it."""
    options = webdriver.ChromeOptions()
    # Uncomment for headless/CI execution:
    # options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()


def login(browser, username, password):
    """Reusable helper for login."""
    browser.get(BASE_URL)
    browser.find_element(By.ID, "user-name").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "login-button").click()


def test_login_with_valid_credentials(driver):
    login(driver, VALID_USERNAME, VALID_PASSWORD)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    assert driver.current_url.endswith("/inventory.html")
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"


def test_login_with_invalid_password_shows_error(driver):
    login(driver, VALID_USERNAME, "wrong_password")
    error = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert "Username and password do not match" in error.text


def test_products_page_has_product_cards(driver):
    login(driver, VALID_USERNAME, VALID_PASSWORD)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0


def test_add_product_to_cart_updates_badge(driver):
    login(driver, VALID_USERNAME, VALID_PASSWORD)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    badge = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == "1"


def test_added_product_appears_in_cart(driver):
    login(driver, VALID_USERNAME, VALID_PASSWORD)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "cart_list"))
    )
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) == 1
    assert "Sauce Labs Backpack" in cart_items[0].text
