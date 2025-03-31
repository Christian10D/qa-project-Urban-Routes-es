import time
from faulthandler import is_enabled
import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import UrbanRoutesPage
from UrbanRoutesPage import UrbanRoutesPage
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from data import phone_number

class TestUrbanRoutes:
    driver = None
    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capabilities("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.UrbanRoutesPage = UrbanRoutesPage(cls.driver)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_order_taxi_button(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_to, data.address_from)
        assert routes_page.order_taxi_button_enabled()
        self.driver.find_element(*self.UrbanRoutesPage.order_taxi_button).click()

    def test_select_comfort_tariff(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutesPage(self.driver)
        route_page.set_route(data.address_to, data.address_from)
        route_page.order_taxi_button()
        is_selected = route_page.select_confort_tarif_enabled()
        assert is_selected == True

    def test__put_phone_number(self):
        self.driver.get(data.urban_routes_url)
        route_page=UrbanRoutesPage(self.driver)
        route_page.set_route(data.address_to, data.address_from)
        route_page.order_taxi_button()
        phone_number=data.phone_number
        route_page.enter_phone_number(phone_number)
        assert route_page.get_phone_number()==phone_number

    def test_set_phone_number(self):
        self.driver.get(data.urban_routes_url)
        route_page = UrbanRoutesPage(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.order_taxi_button()
        phone_number = data.phone_number
        route_page.enter_phone_number(phone_number)
        assert route_page.get_phone_number() == phone_number

    def test_payment_method(self):
        self.driver.get(data.urban_routes_url)
        route_page=UrbanRoutesPage(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.order_taxi_button()
        route_page.payment_method(data.card_code, data.card_number)
        added_card=self.driver.find_element(*route_page.added_card)
        assert "Tarjeta" in added_card.text

    def test_send_messasge_to_driver(self):
        self.driver.get(data.urban_routes_url)
        route_page=UrbanRoutesPage(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.order_taxi_button()
        route_page.send_messahe_to_driver(data.message_for_driver)
        assert route_page.get_message_to_driver()== data.message_for_driver

    def test_order_blanket_and_kerchief(self):
        self.driver.get(data.urban_routes_url)
        route_page=UrbanRoutesPage(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.order_taxi_button()
        route_page.select_confort_tariff_enabled()
        route_page.order_blanked_and_kerchief()
        blanket_kerchief_button=self.driver.find_element(By.CLASS_NAME, 'switch-input')

    def test_order_2_ice_cream(self):
        self.driver.get(data.urban_routes_url)
        route_page=UrbanRoutesPage(self.driver)
        route_page.set_route(data.address_from, data.address_to)
        route_page.order_taxi_button()
        route_page.order_ice_cream()
        ice_cream_counter=route_page.ice_creams_counter()
        assert ice_cream_counter==2

    def test_car_search_model(self):
        self.driver.get(data.urban_routes_url)
        route_page=UrbanRoutesPage(self.driver)
        route_page.car_search_mmodel()
        assert self.driver.find_element(*self.UrbanRoutesPage.order_taxi_details).is_displayed()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
