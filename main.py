
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import datetime

URL = "https://preinscripcion.utm.edu.ec/login"

# Ingresa aquí tu correo y tu contraseña
EMAIL = "jcedeno7718@utm.edu.ec"
PASSWORD = "Pochita14"

# Definiendo variables generales

ID_USER = "txt_usuario"
ID_PASSWORD = "txt_password"
ID_SIDEBAR = "sidebar-menu"
ID_INSCRIPCION = "inscripcion"
ID_CARRERA = "cboescuelainscripcion"
ID_MALLA = "cbomallahorario"
ID_PERIODO = ""

# Testeando @Día de inscripcion
ID_DIAINSCRIPCION = "diainscripcion"
ID_ESCUELA = "cboescuela"

# Testeando @Suficiencia
ID_SUFICIENCIA = "inscripcionsuf"
NAME_CARRERA_TEST = "cmb_escuela"
NAME_MALLA_TEST = "cmd_malla_est"
NAME_PERIODO_TEST = "cmb_periodo"
NAME_SUFICIENCIA = "cmb_malla"
MALLA_TEST = "INGLÉS"

CARRERA_TEST = "INGENIERIA DE SISTEMAS INFORMATICOS"
MALLA = "SISTEMAS DE INFORMACION 2017 (REDISEÑO 2019)"
PERIODO = "MAYO DEL 2023 HASTA SEPTIEMBRE DEL 2023"

CLASS_BUTTON = "ant-btn"

# TIEMPO_DE_EJECUCION = datetime.time(10, 00, 00)
TIEMPO_DE_ESPERA = 0.1  # <------- Aquí puedes modificar el tiempo de espera entre los cambios realizados.

# Ingresa aquí tu Malla y tu Carrera correspondientes.
PERIODO = "MAYO DEL 2023 HASTA SEPTIEMBRE DEL 2023"
MALLA = "SISTEMAS DE INFORMACION 2017 (REDISEÑO 2019)"
CARRERA = "Ingenieria De Sistemas Informaticos"

def no_se_encuentra_opcion(nombre_opcion:str, segundos_de_espera:float = 0):
    """ Muestra un mensaje cuando un botón u opción no se encontró en la web. 

    * nombre_opcion: Nombre de la opción que no se encuentra.

    * segundos_de_espera: Por defecto 0. Indican una pausa luego de mostrar el mensaje.

    """
    print(f"No se encuentra la opción/boton [{nombre_opcion}]. Esperando {segundos_de_espera} segundos... ")
    time.sleep(segundos_de_espera)

def seleccionar_opcion_acordeon(driver:webdriver, criterio_busqueda:By, variable_acordeon:str, opcion_visible:str):
    """ Selecciona alguna opción por medio de texto visible (Usar en caso de acordeones). 

    * criterio_busqueda: Objeto de clase By para seleccionar al acordeón. 
    Puede ser: By.NAME, By.CLASS_NAME, By.ID, By.CSS_SELECTOR, etc
    * variable_acordeon: El nombre, id o clase del elemento acordeón.
    * opcion_visible: Texto de la opción a seleccionar.
    """

    opcion = Select(driver.find_element(criterio_busqueda, variable_acordeon))
    opcion.select_by_visible_text(opcion_visible)



# ----- Script en ejecución -----

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get(URL)

    user = driver.find_element(By.ID, ID_USER)
    password = driver.find_element(By.ID, ID_PASSWORD)
    button = driver.find_element(By.CLASS_NAME, CLASS_BUTTON)

    user.send_keys(EMAIL)
    password.send_keys(PASSWORD)
        

    # while datetime.datetime.now().time() < TIEMPO_DE_EJECUCION:
    #     pass

    # Ingresa en las inscripciones
    button.click()

    # Selección de la opción escogida
    while(True):
        try:
            time.sleep(TIEMPO_DE_ESPERA)
            # Selecciona la opción de inscripción
            inscripcion = driver.find_element(By.ID, ID_SUFICIENCIA)
            inscripcion.click()
            break
        except:
            no_se_encuentra_opcion("Inscripcion", 5)
            driver.refresh() 

    time.sleep(TIEMPO_DE_ESPERA)

    input("")
    # Selecciona la carrera 
    seleccionar_opcion_acordeon(driver, By.NAME, NAME_CARRERA_TEST, CARRERA_TEST)
    time.sleep(TIEMPO_DE_ESPERA)

    # Selecciona la Malla 
    seleccionar_opcion_acordeon(driver, By.NAME, NAME_MALLA_TEST, MALLA)
    time.sleep(TIEMPO_DE_ESPERA)

    # Selecciona el periodo 
    seleccionar_opcion_acordeon(driver, By.NAME, NAME_PERIODO_TEST, PERIODO)
    time.sleep(TIEMPO_DE_ESPERA)

    # Selecciona el periodo 
    seleccionar_opcion_acordeon(driver, By.NAME, NAME_SUFICIENCIA, MALLA_TEST)
    time.sleep(TIEMPO_DE_ESPERA)

    while(True):
        pass




