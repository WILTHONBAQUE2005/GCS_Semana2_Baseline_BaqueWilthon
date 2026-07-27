# Documento de Diseño de Software

## Sistema básico de turnos

| Campo | Información |
|---|---|
| Documento | SDD |
| Versión | 1.0 |
| Estado | Candidato para línea base |
| Autor | Baque Wilthon |

1. Objetivo

Describir la arquitectura, los componentes y las decisiones técnicas de la implementación mínima del sistema básico de turnos.

2. Arquitectura

El sistema utiliza una arquitectura simple dividida en cuatro elementos:

1. Aplicación principal.
2. Lógica de gestión de turnos.
3. Configuración controlada.
4. Pruebas unitarias.

La información se almacena en memoria durante la ejecución.

3. Diagrama simple

```text
Usuario
   |
   v
Aplicación principal
   |
   v
Gestor de turnos
   |
   v
Lista temporal en memoria

4. Componentes
4.1 Aplicación principal

Archivo:

src/app.py

Responsabilidades:

Mostrar información de ejecución.
Crear un turno de demostración.
Consultar los turnos registrados.
4.2 Gestor de turnos

Funciones:

crear_turno(nombre): valida y registra un turno.
listar_turnos(): devuelve los turnos registrados.
limpiar_turnos(): elimina los datos temporales para las pruebas.
4.3 Configuración

Archivo:

config/config.example

Contiene únicamente valores de ejemplo. No contiene contraseñas ni tokens reales.

4.4 Pruebas

Archivo:

tests/test_app.py

Verifica:

Registro correcto de un turno.
Asignación de identificadores consecutivos.
Consulta de turnos.
Rechazo de nombres vacíos.
5. Modelo de datos

Cada turno contiene:

Campo	Tipo	Descripción
id	Entero	Identificador consecutivo.
nombre	Texto	Nombre de la persona.
estado	Texto	Estado actual del turno.

Ejemplo:

{
  "id": 1,
  "nombre": "Usuario demo",
  "estado": "pendiente"
}
6. Flujo de registro
La aplicación recibe un nombre.
El sistema elimina espacios al inicio y al final.
El sistema comprueba que el nombre no esté vacío.
El sistema calcula el siguiente identificador.
El sistema crea el turno con estado pendiente.
El turno se almacena en una lista.
El sistema devuelve el turno creado.
7. Decisiones técnicas
Se utiliza Python 3 por su facilidad de ejecución y lectura.
Se utiliza unittest porque está incluido en Python.
No se utiliza base de datos en la primera versión.
La configuración real no se almacena en Git.
Se utiliza un tag anotado para identificar la línea base.
Los cambios posteriores se realizan en ramas independientes.
8. Limitaciones
Los datos se pierden al cerrar la aplicación.
No existe autenticación.
No existe interfaz gráfica.
No existe persistencia en una base de datos.
La versión inicial no permite cancelar turnos.