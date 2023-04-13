
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import datetime

URL = "https://preinscripcion.utm.edu.ec/login"

# Ingresa aquí tu correo y tu contraseña
EMAIL = ""
PASSWORD = ""

# Definiendo variables generales

ID_USER = "txt_usuario"
ID_PASSWORD = "txt_password"
ID_SIDEBAR = "sidebar-menu"
ID_INSCRIPCION = "inscripcion"
ID_CARRERA = "cboescuelainscripcion"
ID_MALLA = "cbomallahorario"
ID_PERIODO = ""

CLASS_BUTTON = "ant-btn"

TIEMPO_DE_EJECUCION = datetime.time(10, 00, 00)
TIEMPO_DE_ESPERA = 0.1  # <------- Aquí puedes modificar el tiempo de espera entre los cambios realizados.

# Ingresa aquí tu Malla y tu Carrera correspondientes.
MALLA = "SISTEMAS DE INFORMACION 2017 (REDISEÑO 2019)"
CARRERA = "Ingenieria De Sistemas Informaticos"

def no_se_encuentra_opcion(nombre_opcion:str, segundos_de_espera:float = 0):
    """ Muestra un mensaje cuando un botón u opción no se encontró en la web. 

    * nombre_opcion: Nombre de la opción que no se encuentra.

    * segundos_de_espera: Por defecto 0. Indican una pausa luego de mostrar el mensaje.

    """
    print(f"No se encuentra la opción/boton [{nombre_opcion}]. Esperando {segundos_de_espera} segundos... ")
    time.sleep(segundos_de_espera)

def seleccionar_opcion_acordeon(driver:webdriver, id_opcion:str, opcion_visible:str):
    """ Selecciona alguna opción por medio de texto visible (Usar en caso de acordeones). 

    * id_opcion: Id del acordeón.

    * opcion_visible: Texto de la opción a seleccionar.
    """

    opcion = Select(driver.find_element(By.ID, ID_MALLA))
    opcion.select_by_visible_text("MAYO DEL 2023 HASTA SEPTIEMBRE DEL 2023")



# ----- Script en ejecución -----

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get(URL)

    user = driver.find_element(By.ID, ID_USER)
    password = driver.find_element(By.ID, ID_PASSWORD)
    button = driver.find_element(By.CLASS_NAME, CLASS_BUTTON)

    user.send_keys(EMAIL)
    password.send_keys(PASSWORD)
        

    while datetime.datetime.now().time() < TIEMPO_DE_EJECUCION:
        pass

    # Ingresa en las inscripciones
    button.click()

    while(True):
        try:
            time.sleep(TIEMPO_DE_ESPERA)
            # Selecciona la opción de inscripción
            inscripcion = driver.find_element(By.ID, ID_INSCRIPCION)
            inscripcion.click()
            break
        except:
            no_se_encuentra_opcion("Inscripcion", 5)
            driver.refresh() 

    time.sleep(TIEMPO_DE_ESPERA)


    # Selecciona la carrera 
    seleccionar_opcion_acordeon(driver, ID_CARRERA, CARRERA)
    time.sleep(TIEMPO_DE_ESPERA)

    # Selecciona la Malla 
    seleccionar_opcion_acordeon(driver, ID_MALLA, MALLA)
    time.sleep(TIEMPO_DE_ESPERA)

    # Selecciona el periodo 
    seleccionar_opcion_acordeon(driver, ID_PERIODO, CARRERA)
    time.sleep(TIEMPO_DE_ESPERA)

    while(True):
        pass




