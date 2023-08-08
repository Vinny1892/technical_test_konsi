import logging
import time

from decouple import config
from selenium import webdriver
from selenium.webdriver.common.by import By

from crawler_benefit.contract.steps.etl_contract import EtlContract
from crawler_benefit.exceptions.steps.etl_exception import EtlException

logger = logging.getLogger(__file__)

class Extract:
    def __init__(self, data):
        self.data = data

    def extract(self) -> EtlContract:
        try:
            data = self._scrap()
            return EtlContract(data, "Extract", data["time_function_duration"])
        except:
            message = "error when running extract data in etl"
            raise EtlException(stage="Extract", data=self.data, message=message)

    def _login(self, driver):
        input_user = driver.find_element(By.ID, "user")
        input_user.send_keys(self.data["login"])

        input_password = driver.find_element(By.ID, "pass")
        input_password.send_keys(self.data["password"])

        button_submit = driver.find_element(By.ID, "botao")
        button_submit.click()

    def _close_modal_and_sidebar(self, driver):
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "ion-button[title=Fechar]").click()  # button_modal_close.click()

        menu_items = driver.find_element(By.TAG_NAME, "ion-list").find_elements(By.TAG_NAME, "ion-item")
        for menu_item in menu_items:
            if menu_item.text == "Extratos":
                menu_item.click()
        time.sleep(5)

    def _scroll_page(self, driver):
        command = (
            "document.querySelector('app-extrato ion-content').shadowRoot.querySelector('main').scrollTo(0, "
            "document.body.scrollHeight);"
        )
        driver.execute_script(command)

    def _get_data_modal(self, driver):
        driver.find_element(By.CSS_SELECTOR, "ion-card ion-item ion-input input").send_keys(self.data["cpf"])
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "ion-button.configverde").click()
        time.sleep(5)

    def _scrap(self):
        logger.debug("iniciando scrapy")
        init = time.time()
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-gpu")
        selenium_host = config("SELENIUM_HOST", cast=str)
        selenium_port = config("SELENIUM_PORT", cast=int)
        driver = webdriver.Remote(command_executor=f"{selenium_host}:{selenium_port}", options=options)
        try:
            logger.debug("iniciando scrapy")
            url = "http://extratoclube.com.br/"
            driver.get(url)
            frame_tag = driver.find_element(By.TAG_NAME, "frame")
            url_frame = frame_tag.get_attribute("src")
            driver.get(url_frame)
            # LOGIN
            self._login(driver=driver)
            # DASHBOARD
            # MODAL
            logger.debug("login feito")

            self._close_modal_and_sidebar(driver=driver)
            # ITEMS
            self._scroll_page(driver=driver)
            list_of_buttons = driver.find_elements(By.CSS_SELECTOR, "ion-button[expand=full][color=medium]")
            time.sleep(5)
            for button in list_of_buttons:
                if button.text == "ENCONTRAR BENEFÍCIOS DE UM CPF":
                    button.click()

            self._scroll_page(driver=driver)
            # CARD GOAL
            self._get_data_modal(driver=driver)
            self._scroll_page(driver=driver)

            benefit_number = driver.find_element(By.CSS_SELECTOR, "ion-item ion-label").text
            final = time.time()
            time_function_duration = final - init
            data = {
                "benefit_number": benefit_number,
                "time_function_duration": time_function_duration,
                "cpf": self.data["cpf"],
            }
            if benefit_number == "Matrícula não encontrada!":
                data["benefit_number"] = None
            return data

        finally:
            driver.quit()
