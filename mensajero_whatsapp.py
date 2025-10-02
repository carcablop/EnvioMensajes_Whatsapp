import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, urllib.parse
import argparse
import os


SESSION_DIR = os.path.join(os.getcwd(), "whatsapp_session")
def enviar_mensajes(csv_file, mensaje):
    options = webdriver.ChromeOptions()

    os.makedirs(SESSION_DIR, exist_ok=True)
    options.add_argument(f"user-data-dir={SESSION_DIR}")

    #options.add_argument("user-data-dir=C:/Users/usuario/Documents/projects/chrome_selenium")  
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com/")
    wait = WebDriverWait(driver, 80)

    contactos = pd.read_csv(csv_file, sep=";")
    contactos.columns=contactos.columns.str.strip().str.lower()

    for idx, row in contactos.iterrows():
        nombre= row['nombre']
        numero= str(row['numero']).strip() 
        if not numero.startswith("57"):
            numero= "57" + numero
        texto = mensaje.format(nombre=nombre)
        texto_encoded = urllib.parse.quote(texto)
        try:
            print(f"Enviando a {nombre} ({numero})")
            link = f"https://web.whatsapp.com/send?phone={numero}&text={texto_encoded}"
            driver.get(link)

            input_box = wait.until(
                EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]'))
        )

            input_box.send_keys(Keys.ENTER)
            print(f"Mensaje enviado a {numero}")
            time.sleep(5)

        except Exception as e:
            print(f"Error con {numero}: {e}")
    print("Mensajes procesados.")
    driver.quit()       

def main():

    parser= argparse.ArgumentParser(description= "Envia mensajes masivos por whatsapp web usando un archivo csv")
    parser.add_argument("csv_file", help="Ruta al archivo CSV con la lista de contactos (debe tener columnas 'nombre' y 'numero').")
    parser.add_argument("mensaje", help= "mensaje a enviar a cada persona")
    args= parser.parse_args()
    enviar_mensajes(args.csv_file, args.mensaje)

if __name__ == "__main__":

    main() 