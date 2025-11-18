from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
import time


def setup_driver():
    """Set up and return Appium driver"""
    caps = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "emulator-5554",
        "appium:platformVersion": "16",
        "appium:appPackage": "com.darkempire78.opencalculator",
        "appium:appActivity": "com.darkempire78.opencalculator.activities.MainActivity",
        "appium:noReset": True,
    }
    
    options = UiAutomator2Options().load_capabilities(caps)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(5)
    return driver


def get_result(driver):
    """Get calculator result and normalize it"""
    result_id = "com.darkempire78.opencalculator:id/input"
    result = driver.find_element(AppiumBy.ID, result_id).text
    return result.replace(",", "").strip()


def clear_calculator(driver):
    """Click the clear button"""
    clear_btn = "com.darkempire78.opencalculator:id/clearButton"
    driver.find_element(AppiumBy.ID, clear_btn).click()
    time.sleep(0.5)


def test_addition():
    """Test: 1 + 9 = 10"""
    driver = setup_driver()
    try:
        clear_calculator(driver)
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/oneButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/addButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/nineButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/equalsButton").click()  # Fixed: equals not equal
        
        time.sleep(1)
        result = get_result(driver)
        assert result == "10", f"Expected 10, got {result}"
        print("✅ Addition test passed: 1 + 9 = 10")
    finally:
        driver.quit()


def test_subtraction():
    """Test: 9 - 4 = 5"""
    driver = setup_driver()
    try:
        clear_calculator(driver)
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/nineButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/subtractButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/fourButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/equalsButton").click()
        
        time.sleep(1)
        result = get_result(driver)
        assert result == "5", f"Expected 5, got {result}"
        print("✅ Subtraction test passed: 9 - 4 = 5")
    finally:
        driver.quit()


def test_multiplication():
    """Test: 3 × 4 = 12"""
    driver = setup_driver()
    try:
        clear_calculator(driver)
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/threeButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/multiplyButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/fourButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/equalsButton").click()
        
        time.sleep(1)
        result = get_result(driver)
        assert result == "12", f"Expected 12, got {result}"
        print("✅ Multiplication test passed: 3 × 4 = 12")
    finally:
        driver.quit()


def test_division():
    """Test: 20 ÷ 4 = 5"""
    driver = setup_driver()
    try:
        clear_calculator(driver)
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/twoButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/zeroButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/divideButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/fourButton").click()
        driver.find_element(AppiumBy.ID, "com.darkempire78.opencalculator:id/equalsButton").click()
        
        time.sleep(1)
        result = get_result(driver)
        assert result == "5", f"Expected 5, got {result}"
        print("✅ Division test passed: 20 ÷ 4 = 5")
    finally:
        driver.quit()


if __name__ == "__main__":
    print("Running calculator automation tests...\n")
    test_addition()
    test_subtraction()
    test_multiplication()
    test_division()
    print("\n✅ All tests passed!")
