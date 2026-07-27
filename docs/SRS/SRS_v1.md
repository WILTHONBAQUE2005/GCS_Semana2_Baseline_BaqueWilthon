# Especificación de Requisitos de Software

## Sistema básico de turnos

| Campo | Información |
|---|---|
| Documento | SRS |
| Versión | 1.0 |
| Estado | Candidato para línea base |
| Autor | Baque Wilthon |
| Proyecto | Sistema básico de turnos |

## 1. Objetivo

Definir los requisitos de una aplicación sencilla para registrar y consultar turnos. La aplicación se utiliza como ejemplo para aplicar gestión de configuración, versionado y establecimiento de una línea base.

## 2. Alcance

La versión inicial permite registrar turnos en memoria, asignar identificadores consecutivos, consultar los turnos creados y validar los datos de entrada.

La versión 1.0 no incluye base de datos, autenticación ni interfaz gráfica.

## 3. Requisitos funcionales

| ID | Requisito | Descripción | Criterio de aceptación |
|---|---|---|---|
| REQ-001 | Registrar turno | El sistema deberá permitir registrar un turno utilizando el nombre de una persona. | Al ingresar un nombre válido, el sistema crea y devuelve el turno. |
| REQ-002 | Asignar identificador | El sistema deberá asignar un identificador numérico consecutivo a cada turno. | El primer turno recibe el ID 1 y los siguientes aumentan de uno en uno. |
| REQ-003 | Consultar turnos | El sistema deberá permitir consultar todos los turnos registrados durante la ejecución. | La consulta devuelve una lista con los turnos creados. |
| REQ-004 | Validar nombre | El sistema deberá impedir el registro de nombres vacíos o formados únicamente por espacios. | El sistema presenta un error y no registra el turno. |

## 4. Requisitos no funcionales

| ID | Requisito | Descripción | Criterio de aceptación |
|---|---|---|---|
| REQ-005 | Rendimiento | Las operaciones deberán responder en menos de dos segundos con un máximo de 100 turnos. | El registro y la consulta se realizan sin retrasos visibles. |
| REQ-006 | Mantenibilidad y seguridad | El código deberá organizarse en funciones y no deberá almacenar contraseñas, tokens ni datos sensibles. | La aplicación utiliza funciones separadas y solamente incluye una configuración de ejemplo. |

## 5. Restricciones

- La aplicación se desarrollará con Python 3.
- Los turnos se almacenarán únicamente en memoria.
- No se almacenarán credenciales reales en el repositorio.
- La documentación, el código y la configuración estarán controlados mediante Git.
- La línea base se identificará con el tag `v1.0`.

## 6. Matriz de trazabilidad

| Requisito | Componente relacionado | Evidencia |
|---|---|---|
| REQ-001 | `crear_turno()` | `test_crear_turno()` |
| REQ-002 | `crear_turno()` | `test_ids_consecutivos()` |
| REQ-003 | `listar_turnos()` | `test_listar_turnos()` |
| REQ-004 | `crear_turno()` | `test_rechazar_nombre_vacio()` |
| REQ-005 | Aplicación completa | Revisión de ejecución |
| REQ-006 | Código y configuración | Revisión del repositorio |

## 7. Criterio de aprobación

Los requisitos REQ-001 a REQ-006 podrán formar parte de la línea base v1.0 después de revisar la documentación, ejecutar la aplicación y comprobar las pruebas.