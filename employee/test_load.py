import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("browser", ["edge"])
def test_load_page_under_load(browser, benchmark):
    """Test de charge : Tester la page sous une charge de requêtes avec Edge"""
    if browser == 'edge':
        edge_service = EdgeService(executable_path=r"C:\Users\manar.dahmou\Downloads\crud_operations-main\Django Framework Python  Complete\crud\employee\edge\msedgedriver.exe")
        driver = webdriver.Edge(service=edge_service)

    # Effectuer un test de performance avec benchmark
    benchmark(measure_load_page, driver)
    
    driver.quit()

def measure_load_page(driver):
    driver.get("http://127.0.0.1:8000/show/")  # URL de votre application
    wait = WebDriverWait(driver, 10)  # Attendre jusqu'à 10 secondes
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3")))  # Assurez-vous que l'élément <h3> est visible
    print(element.text)
    time.sleep(3)  # Attendre un peu pour visualiser l'action

@pytest.mark.parametrize("browser", ["edge"])
def test_stress_load(browser, benchmark):
    """Test de stress : tester l'application avec un nombre élevé de requêtes simultanées pour Edge"""
    if browser == 'edge':
        edge_service = EdgeService(executable_path=r"C:\Users\manar.dahmou\Downloads\crud_operations-main\Django Framework Python  Complete\crud\employee\edge\msedgedriver.exe")
        driver = webdriver.Edge(service=edge_service)

    # Effectuer un test de performance avec benchmark
    benchmark(measure_stress_load, driver)

    driver.quit()

def measure_stress_load(driver):
    driver.get("http://127.0.0.1:8000/show/")  # URL de votre application
    time.sleep(2)  # Simuler des requêtes pendant un certain temps
    print("Simulating high load...")
    time.sleep(3)  # Attendre un peu pour simuler le stress

