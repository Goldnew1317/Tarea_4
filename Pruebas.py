import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import HtmlTestRunner
from time import sleep


def Pausa(int):
    sleep(int)

class OrbiSearch(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(chrome_options=options)

    #fallo en el inicio de sesion
    def test_Orbi_login_fail(self):
        driver = self.driver
        driver.get("https://orbi.edu.do/orbi/")
        self.assertIn("Orbi", driver.title)
        elem = driver.find_element(By.NAME, "txtNombreUsuario")
        elem.send_keys("newdermed84@gmail.com")
        elem1 = driver.find_element(By.NAME, "txtContrasena")
        elem1.send_keys("123456789")
        elem1.send_keys(Keys.RETURN)
        Pausa(3)
        driver.save_screenshot("capturas/Login_fail.png")
        self.assertNotIn("No results found.", driver.page_source)

    #inicio de sesion satisfactorio
    def test_Orbi_login_success(self):
        driver = self.driver
        driver.get("https://orbi.edu.do/orbi/")
        assert "Orbi" in driver.title

        elem = driver.find_element(By.NAME, "txtNombreUsuario")
        elem.clear()
        elem.send_keys("newdermed84@gmail.com")

        elem1 = driver.find_element(By.NAME, "txtContrasena")
        elem1.clear()
        elem1.send_keys("G123456789")
        driver.save_screenshot("capturas/Login_1.png")
        elem1.send_keys(Keys.RETURN)

        Pausa(3)
        driver.save_screenshot("capturas/Login_2.png")

    #Inicio y Cerrado de sesion
    def test_Orbi_signUp_signOut(self):
        driver = self.driver
        driver.get("https://orbi.edu.do/orbi/")
        assert "Orbi" in driver.title

        elem = driver.find_element(By.NAME, "txtNombreUsuario")
        elem.clear()
        elem.send_keys("newdermed84@gmail.com")

        elem1 = driver.find_element(By.NAME, "txtContrasena")
        elem1.clear()
        elem1.send_keys("G123456789")
        elem1.send_keys(Keys.RETURN)

        Pausa(3)

        elem = driver.find_element(By.CLASS_NAME, "btn btn-block btn-lg btn-primary".replace(' ','.'))
        elem.send_keys(Keys.RETURN)
        driver.save_screenshot("capturas/SignUp_SignOut_1.png")

        Pausa(10)

        elem = driver.find_element(By.ID, "cerrar-sesion")
        elem.send_keys(Keys.RETURN)

        Pausa(3)

        elem = driver.find_element(By.CLASS_NAME, "fast_confirm_proceed")
        Pausa(3)
        driver.save_screenshot("capturas/SignUp_SignOut_2.png")
        elem.send_keys(Keys.RETURN)

        Pausa(2)
        driver.save_screenshot("capturas/SignUp_SignOut_3.png")

    #Accediendo al tutorial de orbi
    def test_Orbi_tutorial(self):
        driver = self.driver
        driver.get("https://orbi.edu.do/orbi/")
        assert "Orbi" in driver.title

        elem = driver.find_element(By.NAME, "txtNombreUsuario")
        elem.clear()
        elem.send_keys("newdermed84@gmail.com")

        elem1 = driver.find_element(By.NAME, "txtContrasena")
        elem1.clear()
        elem1.send_keys("G123456789")
        elem1.send_keys(Keys.RETURN)

        Pausa(3)

        elem = driver.find_element(By.CLASS_NAME, "btn btn-block btn-lg btn-primary".replace(' ','.'))
        elem.send_keys(Keys.RETURN)
        driver.save_screenshot("capturas/Orbi_Tutorial_1.png")

        Pausa(10)

        elem = driver.find_element(By.CLASS_NAME, "fs14 subInfo azulito".replace(' ','.'))
        elem.send_keys(Keys.RETURN)
        driver.save_screenshot("capturas/Orbi_Tutorial_2.png")
        driver.switch_to.window(driver.window_handles[2]) 

        Pausa(10)
        driver.save_screenshot("capturas/Orbi_Tutorial_3.png")

    #Accediendo al chat del itla dentro del orbi
    def test_orbi_itla_chat(self):
        driver = self.driver
        driver.get("https://orbi.edu.do/orbi/")
        assert "Orbi" in driver.title

        elem = driver.find_element(By.NAME, "txtNombreUsuario")
        elem.clear()
        elem.send_keys("newdermed84@gmail.com")

        elem1 = driver.find_element(By.NAME, "txtContrasena")
        elem1.clear()
        elem1.send_keys("G123456789")
        elem1.send_keys(Keys.RETURN)

        Pausa(3)

        elem = driver.find_element(By.CLASS_NAME, "btn btn-block btn-lg btn-primary".replace(' ','.'))
        elem.send_keys(Keys.RETURN)
        

        Pausa(10)
        driver.save_screenshot("capturas/Orbi_Chat_1.png")
        elem = driver.find_element(By.CLASS_NAME, "hBSummary svelte-1nuz0j2".replace(' ','.'))
        elem.send_keys(Keys.RETURN)

        Pausa(5)
        driver.save_screenshot("capturas/Orbi_Chat_2.png")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reportes'))