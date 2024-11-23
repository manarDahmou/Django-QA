from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("browser", ['edge'])
def test_cross_browser(browser):
    driver = None
    # Configurer le WebDriver pour Edge
    if browser == 'edge':
        edge_service = EdgeService(executable_path=r"C:\Users\manar.dahmou\Downloads\crud_operations-main\Django Framework Python  Complete\crud\employee\edge\msedgedriver.exe")
        driver = webdriver.Edge(service=edge_service)

    try:
        # Ouvrir l'application ou l'URL que vous souhaitez tester
        driver.get("http://127.0.0.1:8000/show/")  # Remplacez par l'URL de votre application

        # Attendre que l'élément <h1> soit visible (attente explicite)
        wait = WebDriverWait(driver, 10)  # Attendre jusqu'à 10 secondes
        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3")))  # Assurez-vous que l'élément <h3> est visible
        print(element.text)

        # Attendre un peu pour visualiser l'action dans le navigateur (optionnel)
        time.sleep(3)

        # Vérifier le titre de la page ou tout autre test à faire
        assert "http://127.0.0.1:8000/show/" in driver.current_url

    finally:
        # Fermer le navigateur après le test
        driver.quit()
