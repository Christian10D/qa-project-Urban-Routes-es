import time
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import main


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    order_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    comfort_tariff_button = (By.CSS_SELECTOR, '.tcard:nth-child(5)')
    phone_number = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.np-button > div')
    phone_number_field = (By.ID, 'phone')
    submit_phone_number_button = (By. XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    code_sms = (By.ID, 'code')
    confirm_code = (By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    payment_method = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled')
    add_card_button = (By. CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled > div.pp-checkbox > div')
    card_number = (By.ID, 'number')
    card_code = (By.CSS_SELECTOR, '#code')
    submit_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_payment_method = (By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > button')
    added_card = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[1]')
    message_to_driver = (By.XPATH, '//*[@id="comment"]')
    order_requests_button = (By.CLASS_NAME, 'reqs-arrow')
    blanket_and_kerchief_button = (By.XPATH, "//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    add_ice_cream_button = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body > div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
    ice_cream_counter = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    order_taxi_submit = (By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper > button')
    order_taxi_details = (By.XPATH, '//*[@id="root"]/div/div[5]')

    def __init__(self, driver):
        self.driver = driver

    def set_route(self, address_from, address_to):
        self.set_from(data.address_from)
        self.set_to(data.address_to)

    def set_from(self, address_from):
        from_input = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.from_address_field))
        from_input.clear()
        self.driver.find_element(*self.from_address_field).send_keys(data.address_from)

    def set_to(self, address_to):
        from_input = WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.to_address_field))
        from_input.clear()
        self.driver.find_element(*self.to_address_field).send_keys(data.address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_address_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_address_field).get_property('value')

    def order_taxi_button_enabled(self):
        order_taxi_button = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located(self.order_taxi_button))
        return order_taxi_button.is_enabled()

    def click_order_taxi_button(self):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(self.order_taxi_button))
        self.driver.find_element(*self.order_taxi_button).click()

    def select_comfort_tariff_enabled(self):
        comfort_tariff_button = WebDriverWait(self.driver, 25).until(
            EC.visibility_of_element_located(self.comfort_tariff_button))
        return comfort_tariff_button.is_enabled()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number).click()
        from_input = WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(self.phone_number_field))
        from_input.clear()
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def set_phone_number(self, phone_number):
        self.driver.find_element(*self.phone_number).click()
        from_input = WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(self.phone_number_field))
        from_input.clear()
        self.driver.find_element(*self.phone_number_field).send_keys(phone_number)
        self.driver.find_element(*self.submit_phone_number_button).click()
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(self.code_sms))
        self.driver.find_element(*self.code_sms).send_keys(main.retrieve_phone_code(driver=self.driver))
        self.driver.find_element(*self.confirm_code).click()

    def set_payment_method(self, card_number, card_code):
        self.driver.find_element(*self.payment_method).click()
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(self.add_card_button))
        self.driver.find_element(*self.add_card_button).click()
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.card_number))
        card_number_field = self.driver.find_element(*self.card_number)
        card_number_field.clear()
        card_number_field.send_keys(card_number + Keys.TAB + card_code)
        card_number_field.send_keys(Keys.TAB)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.submit_card_button))
        self.driver.find_element(*self.submit_card_button).click()
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.close_payment_method))
        self.driver.find_element(*self.close_payment_method).click()

    def send_message_to_driver(self, message_to_driver):
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.message_to_driver))
        self.driver.find_element(*self.message_to_driver).send_keys(data.message_to_driver)

    def get_message_to_driver(self):
        return self.driver.find_element(*self.message_to_driver).get_property('value')

    def order_blanket_and_kerchief(self):
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.order_requests_button))
        self.driver.find_element(*self.order_requests_button).click()
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.blanket_and_kerchief_button))
        self.driver.find_element(*self.blanket_and_kerchief_button).click()

    def order_2_ice_cream(self):
        self.driver.find_element(*self.comfort_tariff_button).click()
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.add_ice_cream_button))
        self.driver.find_element(*self.add_ice_cream_button).click()
        self.driver.find_element(*self.add_ice_cream_button).click()

    def ice_creams_counter(self):
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.ice_cream_counter))
        counter_text = self.driver.find_element(*self.ice_cream_counter).text.strip()
        return int(counter_text)

    def car_search_modal_appear(self):
        route_page = UrbanRoutesPage(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.click_order_taxi_button()
        route_page.select_comfort_tariff_enabled()
        route_page.set_payment_method(data.card_number, data.card_code)
        route_page.set_phone_number(data.phone_number)
        WebDriverWait(self.driver, 25).until(EC.visibility_of_element_located(self.order_taxi_submit))
        self.driver.find_element(*self.order_taxi_submit).click()
