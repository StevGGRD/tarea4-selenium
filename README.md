# Tarea 4 - Pruebas Automatizadas con Selenium

App de tareas con login, hecha en Flask, con pruebas automatizadas en Selenium + pytest.

## Como correrlo

1. Instalar dependencias:
```
pip install -r requirements.txt
```

2. En una terminal, levantar la app:
```
python app.py
```

3. En otra terminal, correr las pruebas y generar el reporte:
```
cd tests
pytest --html=../reporte.html --self-contained-html
```

Esto va a:
- Abrir Chrome en modo headless y correr los 15 casos de prueba (5 historias de usuario x 3 tipos: camino feliz, negativo, limite)
- Guardar capturas de pantalla automaticas en `tests/screenshots/`
- Generar `reporte.html` con el resultado de cada prueba y su captura

## Usuario de prueba
- usuario: `admin`
- clave: `1234`

## Historias de usuario
1. Como usuario quiero iniciar sesion para acceder a mis tareas
2. Como usuario quiero crear tareas para organizarme
3. Como usuario quiero ver mis tareas para saber que tengo pendiente
4. Como usuario quiero editar una tarea para corregir el titulo
5. Como usuario quiero eliminar tareas que ya no necesito
