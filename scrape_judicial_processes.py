import requests
from bs4 import BeautifulSoup
import csv
import json
import threading
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Punto 1: Web Scraping


def scrape_judicial_processes(id_number, person_type):
    """
    Función para realizar el web scraping de los procesos judiciales.

    Args:
        id_number (str): Número de identificación (CI o RUC)
        person_type (str): Tipo de persona ('natural' o 'juridica')

    Returns:
        list: Lista de diccionarios con la información de los procesos judiciales.
    """
    # Inicializar el controlador del navegador (en este caso, Chrome)
    driver = webdriver.Chrome()

    # Abrir la página de búsqueda
    url = "https://procesosjudiciales.funcionjudicial.gob.ec/busqueda-filtros"
    driver.get(url)

    # Esperar hasta que el campo de entrada esté disponible
    search_input_actor_xpath = "/html/body/app-root/app-expel-filtros-busqueda/expel-sidenav/mat-sidenav-container/mat-sidenav-content/section/form/div[2]/mat-form-field[1]/div[1]/div/div[2]/input"
    wait = WebDriverWait(driver, 3)
    search_input = wait.until(
        EC.presence_of_element_located((By.XPATH, search_input_actor_xpath))
    )

    # Insertar el número de identificación en el campo de búsqueda
    search_input.send_keys(id_number)

    # Enviar el formulario para realizar la búsqueda
    submit_button_xpath = "/html/body/app-root/app-expel-filtros-busqueda/expel-sidenav/mat-sidenav-container/mat-sidenav-content/section/form/div[6]/button[1]"
    submit_button = wait.until(
        EC.presence_of_element_located((By.XPATH, submit_button_xpath))
    )
    submit_button.click()

    # Crear una lista para almacenar los resultados
    resultados = []

    while True:
        # Esperar hasta que se carguen los resultados de la página actual
        results_xpath = "//div[@class='cuerpo']"
        wait.until(EC.presence_of_element_located((By.XPATH, results_xpath)))

        # Obtener el contenido HTML de la página actual
        html_content = driver.page_source

        # Parsear el HTML con BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Encontrar todos los elementos causa-individual
        causas = soup.find_all("div", class_="causa-individual ng-star-inserted")

        # Iterar sobre los elementos causa-individual y extraer la información
        for causa in causas:
            numero = causa.find(class_="id").text.strip()
            fecha = causa.find(class_="fecha").text.strip()
            numero_proceso = causa.find(class_="numero-proceso").text.strip()
            accion_infraccion = causa.find(class_="accion-infraccion").text.strip()
            detalle = causa.find(class_="detalle").text.strip()

            # Agregar la información a la lista de resultados
            resultados.append(
                {
                    "No.": numero,
                    "Fecha de ingreso": fecha,
                    "No. proceso": numero_proceso,
                    "Acción / Infracción": accion_infraccion,
                    "Detalle": detalle,
                }
            )
            print("Numero: ", numero)
            print("Fecha: ", fecha)
            print("Numero proceso: ", numero_proceso)
            print("Accion: ", accion_infraccion)
            print("Detalle: ", detalle)
            print("-------------------------------------------------")

        # Verificar si hay un botón para ir a la siguiente página
        next_button = "/html/body/app-root/app-expel-listado-juicios/expel-sidenav/mat-sidenav-container/mat-sidenav-content/section/footer/mat-paginator/div/div/div[2]/button[3]"
        next_button = wait.until(
            EC.presence_of_element_located((By.XPATH, next_button))
        )
        if (
            "mat-mdc-button-disabled mat-mdc-tooltip-disabled"
            in next_button.get_attribute("class")
        ):
            # Si el botón de siguiente página está deshabilitado, salimos del bucle
            break

        # Hacer clic en el botón de siguiente página
        next_button.click()

    # Cerrar el controlador del navegador
    driver.quit()
    save_data(resultados, "csv")

    return resultados


def save_data(data, name):
    """
    Función para guardar los datos en un archivo o base de datos.

    Args:
        data (dict): Diccionario con la información de los procesos judiciales.
        file_format (str): Formato del archivo ('csv' o 'json')
    """
    df = pd.DataFrame(data)
    df.to_csv("judicial_processes.csv", index=False, header=True)
    # save file


def test_parallel_requests():  # noqa: E999
    """
    Función para probar el web scraping con múltiples solicitudes paralelas.
    """
    # Lista de datos de prueba
    test_data = [
        ("0968599020001", "natural"),
        ("1791251237001", "juridica"),
        ("0992339411001", "natural"),
        ("0968599020001", "natural"),
        # Agrega más datos de prueba aquí
    ]

    threads = []

    for data in test_data:
        thread = threading.Thread(target=scrape_judicial_processes, args=data)
        threads.append(thread)
        thread.start()
        time.sleep(
            0.1
        )  # Agrega un pequeño retraso para evitar sobrecargar el sitio web

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    # Ejecutar prueba de solicitudes paralelas
    test_parallel_requests()
