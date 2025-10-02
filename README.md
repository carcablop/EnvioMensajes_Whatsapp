# 🤖 WhatsApp Masivo con Python y Selenium

Script de Python para enviar mensajes masivos a una lista de contactos usando WhatsApp Web, Selenium y un archivo CSV, que contiene la lista de contactos con dos columnas "nombre" y "numero"

## 🌟 Características
* Automatización del envío de mensajes a través de WhatsApp Web.
* Lectura de contactos desde un archivo CSV.
* Ejecución simple desde la línea de comandos con argumentos. El archivo csv que contiene los contactos debe agregarse al mismo espacio de trabajo, o en el argumento especificar la ruta.

## ⚙️ Requisitos
1. **Crar entorno virtual venv**
2.  **Python 3.x**
3.  **Google Chrome** instalado. Para este paso guiarse con el siguiente tutorial: https://www.youtube.com/watch?v=Nf5vkkzlpzA&t=62s, https://www.youtube.com/watch?v=WQ1-0salQ4o. 
    Instalar Chromedriver. Y agregar a la variable path del sistema. 
4.  **Librerías de Python** (especificadas en `requirements.txt`).


## 🚀 Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/carcablop/EnvioMensajes_Whatsapp.git
cd ENVIAMENSAJES_WHATSAPP_COMUNIDAD
```
### 2. Crear y activar entorno virtual env 

```bash
python -m venv venv 
```
#### Activar el entorno
#### En Windows (CMD):
```bash
venv\Scripts\activate
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Preparar el archivo csv

nombre: El nombre de la persona.

numero: El número de teléfono. DEBE incluir el código de país (ej. 57300... para Colombia). El script intentará añadir 57 si no lo tiene, ¡pero es mejor que sea correcto desde el origen!


### 5. Ejecuccion del script

Ejecuta el script mensajero_whatsapp.py pasando como argumentos la ruta del CSV y el mensaje (entre comillas).
```bash
python mensajero_whatsapp.py "ruta/a/tu/archivo.csv" "Hola {nombre}, te recordamos que tu evento es mañana."
```

⚠️ Advertencias de Uso

 El script usa selectores de WhatsApp Web, los cuales pueden cambiar con las actualizaciones de WhatsApp. Si deja de funcionar, revisa los selectores de By.XPATH en mensajero_whatsapp.py.

El envío masivo puede ser detectado por WhatsApp y tu cuenta podría ser bloqueada. Usa esta herramienta con responsabilidad y con números de contactos que esperan tu mensaje.
