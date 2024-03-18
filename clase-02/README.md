# Clase 02 - Servicios web
Este código muestra un ejemplo de servicio web en Python con [Flask](https://flask.palletsprojects.com/en/3.0.x/).

## Inicializar ambiente
En primer lugar, inicializar ambiente virtual de Python, para tener un ambiente aislado de otras ejecuciones de Python.

Para crear el ambiente virtual (virtualenv o venv):
```bash
python -m venv .venv 
```

Ejecutar ambiente virtual:
```bash
. ./.venv/bin/activate
```


## Instalar dependencias
Para instalar [Flask](https://flask.palletsprojects.com/en/3.0.x/):
```bash
pip install Flask
```

Para guardar dependencias en archivo `requirements.txt`:
```bash
pip freeze > requirements.txt
```

Para instalar desde archivo de dependencias:
```bash
pip install -r requirements.txt
```

Más sobre el uso de virtualenvs y la instalación de Flask [aquí](https://flask.palletsprojects.com/en/3.0.x/installation/).

