import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture(scope="class")
def setup_class(request):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--headless")  # ลบหรือคอมเมนต์ออกเพื่อให้แสดง UI

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    driver.set_window_size(1280, 900)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()


# group Navbar Before login
@pytest.mark.usefixtures("setup_class")
class TestNavbarBeforelogin:
    def test_open_login_page(self):
        """ทดสอบการเปิดหน้าเว็บ"""
        self.driver.get("https://voice.botnoi.ai/")
        x_btn = self.driver.find_element(By.XPATH, "//mat-icon[@svgicon='close']")
        x_btn.click()
        studio_btn = self.driver.find_element(
            By.XPATH, "//div[@class='button-area']//span[contains(text(),'สตูดิโอ')]"
        )
        studio_btn.click()
        time.sleep(1)
        result = self.driver.find_element(By.XPATH, "//h1[@class='gradient']")
        assert result.text == "เข้าสู่ระบบ"

    def test_voice_page(self):
        """กดเมนู เสียงพากย์"""
        self.driver.get("https://voice.botnoi.ai/")
        x_btn = self.driver.find_element(By.XPATH, "//mat-icon[@svgicon='close']")
        x_btn.click()
        voice_btn = self.driver.find_element(
            By.XPATH,
            "//div[contains(@class, 'button-area') and contains(., 'เสียงพากย์')]",
        )
        voice_btn.click()
        time.sleep(1)
        result = self.driver.find_element(
            By.XPATH, "//h1[@class='hero-header ng-tns-c1245363871-3']"
        )
        assert result.text == "เสียงพากย์ AI"


# group B
@pytest.mark.usefixtures("setup_class")
class TestB:  # ชื่อต้องขึ้นต้น Test ก่อนเท่านั้นไม่งั้น pytest จับไม่เจอ
    pass


if __name__ == "__main__":
    pytest.main(["-v", "--html=test_report.html", "--self-contained-html", "main.py"])
