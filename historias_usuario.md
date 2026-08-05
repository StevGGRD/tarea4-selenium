# Historias de usuario - Tarea 4 (copiar y pegar cada una como una incidencia en Jira)

---

## 1. Login
**Titulo:** Como usuario quiero iniciar sesion para acceder a mis tareas

**Criterios de aceptacion:**
- El usuario ingresa usuario y clave correctos y entra a /tareas
- Si la clave es incorrecta se muestra un mensaje de error
- Si los campos estan vacios no se permite el acceso

**Criterios de rechazo:**
- No debe permitir entrar con credenciales invalidas
- No debe dejar pasar campos vacios sin mostrar error

---

## 2. Crear tarea
**Titulo:** Como usuario quiero crear tareas para organizarme

**Criterios de aceptacion:**
- Al escribir un titulo y darle a "Agregar" la tarea aparece en la lista
- Si el titulo esta vacio se muestra un error y no se crea nada
- Si el titulo tiene mas de 100 caracteres se muestra un error

**Criterios de rechazo:**
- No debe crear tareas con titulo vacio
- No debe aceptar titulos mayores a 100 caracteres

---

## 3. Listar tareas
**Titulo:** Como usuario quiero ver mis tareas para saber que tengo pendiente

**Criterios de aceptacion:**
- Al entrar a /tareas se muestran todas las tareas creadas
- Si no hay ninguna tarea se muestra el mensaje "no hay tareas todavia"
- Sin iniciar sesion no se puede ver la lista (redirige a /login)

**Criterios de rechazo:**
- No debe mostrar la lista a usuarios sin sesion iniciada

---

## 4. Actualizar tarea
**Titulo:** Como usuario quiero editar una tarea para corregir el titulo

**Criterios de aceptacion:**
- Al editar una tarea existente y guardar, el nuevo titulo se refleja en la lista
- Si se intenta editar una tarea con un id que no existe, se muestra "tarea no encontrada"
- Si se guarda con el campo vacio, el titulo original no cambia

**Criterios de rechazo:**
- No debe permitir guardar un titulo vacio como cambio valido
- No debe editar tareas que no existen

---

## 5. Eliminar tarea
**Titulo:** Como usuario quiero eliminar tareas que ya no necesito

**Criterios de aceptacion:**
- Al darle a "eliminar" la tarea desaparece de la lista
- Si se eliminan todas las tareas, se muestra "no hay tareas todavia"
- Intentar eliminar sin sesion iniciada redirige a /login

**Criterios de rechazo:**
- No debe permitir eliminar tareas sin haber iniciado sesion
