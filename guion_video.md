# Guion para el video demostrativo (Tarea 4)

Duracion aproximada: 4-5 minutos. Graba tu pantalla completa (OBS, o el grabador de Windows con Win+G).

---

## 1. Intro (15-20 seg)
**Que mostrar:** tu cara o solo pantalla con el README abierto.
**Que decir:**
"Hola, soy Steven Monsanto, matricula 202010448. Esta es la tarea 4 de Programacion III,
pruebas automatizadas con Selenium sobre una app de tareas con login."

## 2. Mostrar la app funcionando a mano (40-60 seg)
**Que mostrar:** abre el navegador en http://localhost:5000, entra con admin/1234,
crea una tarea, editala, borrala.
**Que decir:**
"Esta es la aplicacion base, hecha en Flask. Tiene login y un CRUD de tareas:
crear, listar, editar y eliminar. Sobre esto corren las pruebas automatizadas."

## 3. Mostrar el codigo de las pruebas (40-60 seg)
**Que mostrar:** abre la carpeta tests/ en el editor, muestra brevemente
test_login.py y test_crear.py (scrollea, no leas todo).
**Que decir:**
"Tengo 5 historias de usuario: login, crear, listar, actualizar y eliminar tareas.
Por cada una hice 3 pruebas: camino feliz, un caso negativo y un caso limite,
en total 15 casos de prueba usando Selenium con Python."

## 4. Mostrar Jira (30-40 seg)
**Que mostrar:** tu tablero de Jira con las 5 historias creadas.
**Que decir:**
"Aqui estan las 5 historias documentadas en Jira, cada una con sus
criterios de aceptacion y rechazo."

## 5. Correr las pruebas en vivo (60-90 seg) -- LO MAS IMPORTANTE
**Que mostrar:** terminal. Primero `python app.py` en una terminal.
Luego en otra: `cd tests` y `pytest --html=../reporte.html --self-contained-html`
Deja que corra y se vean los resultados en la terminal (PASSED en verde).
**Que decir:**
"Ahora corro las pruebas en vivo. Primero levanto el servidor de la app,
y despues ejecuto pytest, que abre Chrome en segundo plano y corre
los 15 casos automaticamente."
(Mientras corre, puedes quedarte callado o narrar lo que va pasando)

## 6. Mostrar el reporte HTML (30-40 seg)
**Que mostrar:** abre reporte.html en el navegador despues de que termine.
Muestra que los 15 casos pasaron, y abre una captura de pantalla de ejemplo.
**Que decir:**
"Aqui esta el reporte generado automaticamente, con cada prueba y su captura
de pantalla correspondiente. Los 15 casos pasaron correctamente."

## 7. Cierre (10-15 seg)
**Que decir:**
"Eso fue todo, gracias."

---

## Antes de grabar, revisa:
- [ ] `pip install -r requirements.txt` ya corrido
- [ ] Tener Chrome instalado (Selenium lo necesita)
- [ ] Probar una vez SIN grabar para asegurarte que los 15 casos pasan
- [ ] Cerrar pestañas/apps que no quieras mostrar
