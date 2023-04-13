
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import datetime

# options = webdriver.ChromeOptions()
# options.binary_location = r"C:\Usuarios\Det-Pc\AppData\Local\Programs\Opera GX\launcher.exe" # Ruta de instalación del navegador de Opera

URL = "https://preinscripcion.utm.edu.ec/login"

ID_USER = "txt_usuario"
ID_PASSWORD = "txt_password"
ID_SIDEBAR = "sidebar-menu"
ID_INSCRIPCION = "inscripcion"
ID_CARRERA = "cboescuelainscripcion"
ID_MALLA = "cbomallahorario"
ID_PERIODO = ""

CLASS_BUTTON = "ant-btn"

MALLA = "SISTEMAS DE INFORMACION 2017 (REDISEÑO 2019)"
CARRERA = "Ingenieria De Sistemas Informaticos"

def no_se_encuentra_opcion(nombre_opcion:str, segundos_de_espera:float = 0):
    """ Muestra un mensaje cuando un botón u opción no se encontró en la web. 

    * nombre_opcion: Nombre de la opción que no se encuentra.

    * segundos_de_espera: Por defecto 0. Indican una pausa luego de mostrar el mensaje.

    """
    print(f"No se encuentra la opción/boton [{nombre_opcion}]. Esperando {segundos_de_espera} segundos... ")
    time.sleep(segundos_de_espera)

driver = webdriver.Chrome()
driver.get(URL)

# ten_am = datetime.time(10, 00, 00)

user = driver.find_element(By.ID, ID_USER)
password = driver.find_element(By.ID, ID_PASSWORD)
button = driver.find_element(By.CLASS_NAME, CLASS_BUTTON)

time.sleep(0.1)
user.send_keys("jcedeno7718@utm.edu.ec")
time.sleep(0.1)
password.send_keys("Pochita14")

# while datetime.datetime.now().time() < ten_am:
#     pass

# Ingresa en las inscripciones
button.click()

while(True):
    try:
        time.sleep(0.1)
        # Selecciona la opción de inscripción
        inscripcion = driver.find_element(By.ID, ID_INSCRIPCION)
        inscripcion.click()
        break
    except:
        no_se_encuentra_opcion("Inscripcion", 5)
        driver.refresh() 


time.sleep(0.1)
# Selecciona la carrera 
carrera = Select(driver.find_element(By.ID, ID_CARRERA))
carrera.select_by_visible_text(CARRERA)

# time.sleep(0.2)
# # Selecciona la Malla 
# malla = Select(driver.find_element(By.ID, ID_MALLA))
# malla.select_by_visible_text("SISTEMAS DE INFORMACION 2017 (REDISEÑO 2019)")

# time.sleep(0.2)
# # Selecciona el periodo 
# periodo = Select(driver.find_element(By.ID, ID_MALLA))
# periodo.select_by_visible_text("MAYO DEL 2023 HASTA SEPTIEMBRE DEL 2023")

while(True):
    pass




