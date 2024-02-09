# innovationlab


## Antes de empezar con la configuración e instalación debes tener instalado Python v3.x.x
URL de descarga: https://www.python.org/downloads/


## Configuración de Instalación
Sigue estos pasos para configurar el proyecto en tu entorno local:

1. Clona el repositorio desde GitHub:
```bash
git clone https://github.com/MarceloLoGuz/innovationlab.git

    1.1.- Navega al directorio del proyecto:
    ```bash
    cd innovationlab


    1.2- Una vez estando dentro del directorio del proyecto, instala, crea y activa un entorno virtual:
        1.2.1- Instala el entorno virtual
        ```bash
        pip install virtualenv

        1.2.2- Crear el entorno virtual
            ```bash
            python -m venv env

        1.2.3- Activar el entorno virtual (Es un poco diferente en Linux y Windows)
            -  En linux
                ```bash
                source env/bin/activate
                

            - En Windows
                ```bash
                source ./env/Scripts/activate    



NOTA: Antes de ir al siguiente paso, ya debes de estar dentro del directorio 'innovationlab' y tener activado el entorno virtual, explicado en el paso  1.2.3


2.- Instala las dependencias del proyecto
```bash
pip install -r requirements.txt


3.- Realiza las migraciones de la base de datos:
```bash
python manage.py makemigrations
python manage.py migrate


4.- Ejecutar el proyecto:
```bash
python manage.py runserver