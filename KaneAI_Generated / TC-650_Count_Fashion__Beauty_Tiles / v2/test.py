
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.support import expected_conditions as EC
import time,requests,re,os, traceback
try:
    from condition import Condition, ResolvedCondition, ConcatenationOperator
except Exception as e:
    pass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from lambdatest_selenium_driver import smartui_snapshot
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
try:

    actions = ActionChains(driver)
    def get_element(driver,locators):
        driver.implicitly_wait(6)
        if isinstance(locators[0], str):
            for locator in locators:
                try:
                    element = driver.find_element(By.XPATH, locator)
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        else:
            for locator in locators:
                by_method = By.XPATH if str(locator['isXPath']).lower() == "true" else By.CSS_SELECTOR
                try:
                    element = driver.find_element(by_method, locator['selector'])
                    if element.is_displayed() and element.is_enabled():
                        return element
                except:
                    continue
        return None

    class element_to_be_input_and_text(object):
        def __call__(self, driver):
            focused_element = driver.execute_script("return document.activeElement;")
            if focused_element.tag_name == "input" or focused_element.tag_name == "textarea" or focused_element.get_attribute("contenteditable") == "true":
                return focused_element
            else:
                return False

    def select_option(select_element, option):
        select = Select(select_element)
        select.select_by_value(option)
    driver.implicitly_wait(6)

    # Step - 1 : Open https://t2online.in/
    driver.get("https://t2online.in/")
    driver.implicitly_wait(6)

    # Step - 2 : Click 'Goodlife' tab in top nav bar
    element_locators = ['.scrollHeader > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)', '.scrollHeader > div:nth-child(2) > div:nth-child(2) > a:nth-child(1)', "//a[text()='Goodlife']", "//a[contains(text(),'Goodlife')]", "//div[contains(@class,'scrollHeader')]/div[2]/div[1]/a[1]", "//div[contains(@class,'scrollHeader')]/div[2]/div[1]/a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 3 : Click Fashion & Beauty section header
    element_locators = ["//h1[text()='Fashion & Beauty']/ancestor::a[1]", "//ion-router-outlet[@id='main-content']/app-goodlife[1]/ion-content[1]/div[1]/div[1]/a[1]", '#main-content > app-goodlife:nth-child(2) > ion-content:nth-child(2) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1)', "//h1[contains(text(),'Fashion & Beauty')]/ancestor::a[1]"]
    element = get_element(driver,element_locators)

    try:
        actions.move_to_element(element).click().perform()
    except:
        element.click()
    driver.implicitly_wait(6)

    # Step - 4 : Get count of cards below Fashion & Beauty → {{cards_count}}
    'This Instruction Is Carried Out By The Vision Model'
    driver.implicitly_wait(6)

    # Step - 5 : Set i = 1
    i = "1"
    driver.implicitly_wait(6)

    # Step - 6 : If {{i}} < {{tiles_count}} then (no actions yet)
    # While loop: If {{i}} < {{tiles_count}} then (no actions yet)
    _loop_counter_CUkv = 1
    _max_iterations_CUkv = 30
    while _loop_counter_CUkv < _max_iterations_CUkv:
        user_variables["loop_counter"] = _loop_counter_CUkv
        _conditions_CUkv = [ResolvedCondition.from_string(condition) for condition in ['{{i}} < {{cards_count}}']]
        _connectors_CUkv = [ConcatenationOperator(connector) for connector in []]
        _condition_CUkv = Condition(_conditions_CUkv, _connectors_CUkv)
        _result_CUkv, _ = _condition_CUkv.evaluate(user_variables, get_variable_value)
        if not _result_CUkv:
            break
        driver.implicitly_wait(6)

        # Step - 7 : {{i}} + 1 → {{j}}driver.implicitly_wait(6)

        # Step - 8 : Get title of card number 7.0 → {{card_title}}
        'This Instruction Is Carried Out By The Vision Model'
        driver.implicitly_wait(6)

        # Step - 9 : Get title below card number 8.0 → {{title_below_card}}
        'This Instruction Is Carried Out By The Vision Model'
        driver.implicitly_wait(6)

        # Step - 10 : Click card number 7.0
        element_locators = ['ion-grid.md > ion-row:nth-child(1) > ion-col:nth-child(8) > a:nth-child(1)', 'ion-grid.md > ion-row:nth-child(1) > ion-col:nth-child(8) > a:nth-child(1)', "//h2[text()='Mohammed Siraj channels relaxed streetwear energy in Snitch’s latest drop']/ancestor::a[1]", "//h2[contains(text(),'Mohammed Siraj channels relaxed streetwear energy in Snitch’s latest drop')]/ancestor::a[1]", "//ion-grid[contains(@class,'md')]/ion-row[1]/ion-col[8]/a[1]", "//ion-grid[contains(@class,'md')]/ion-row[1]/ion-col[8]/a[1]"]
        element = get_element(driver,element_locators)

        try:
            actions.move_to_element(element).click().perform()
        except:
            element.click()
        driver.implicitly_wait(6)

        # Step - 11 : Read title below next story → {{title_below_next_story}}
        'This Instruction Is Carried Out By The Vision Model'
        driver.implicitly_wait(6)

        # Step - 12 : Click Fashion & Beauty section header
        element_locators = ['../a[1]', '../a[1]', 'a:nth-child(1)', 'a:nth-child(1)']
        element = get_element(driver,element_locators)

        try:
            actions.move_to_element(element).click().perform()
        except:
            element.click()
        driver.implicitly_wait(6)

        # Step - 13 : {{i}} + 1 → {{i}}
        try:
            actions.move_to_element(element).click().perform()
        except:
            element.click()
        driver.implicitly_wait(6)

        # Step - 14 : {{j}} + 1 → {{j}}
        try:
            actions.move_to_element(element).click().perform()
        except:
            element.click()

        _loop_counter_CUkv += 1
    if _loop_counter_CUkv >= _max_iterations_CUkv:
        raise Exception("While loop exceeded maximum iterations (30)")

    driver.quit()
except Exception as e:
    driver.quit()
