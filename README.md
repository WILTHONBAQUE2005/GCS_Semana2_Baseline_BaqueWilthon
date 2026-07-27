# Sistema básico de turnos

Repositorio académico desarrollado para aplicar conceptos de Gestión de Configuración de Software, trazabilidad, versionado y establecimiento de una línea base.

## Objetivo

Organizar un repositorio como depósito de elementos de configuración y establecer la línea base `v1.0`.

La línea base contiene requisitos, diseño, código fuente, configuración de ejemplo, pruebas, scripts e instrucciones de ejecución.

## Alcance

La aplicación permite:

- Registrar un turno.
- Asignar un identificador consecutivo.
- Consultar los turnos registrados.
- Validar nombres vacíos.
- Ejecutar pruebas unitarias.

Los datos se almacenan únicamente durante la ejecución del programa.

## Estructura del repositorio

```text
GCS_Semana2_Baseline_BaqueWilthon
│
├── config
│   └── config.example
├── docs
│   ├── SDD
│   │   └── SDD_v1.md
│   └── SRS
│       └── SRS_v1.md
├── scripts
│   └── run_tests.bat
├── src
│   └── app.py
├── tests
│   └── test_app.py
├── .gitignore
├── CHANGELOG.md
└── README.md
```

## Requisitos

- Git.
- Python 3.
- CMD o una terminal compatible.

## Ejecutar la aplicación

Desde la carpeta principal:

```cmd
py src\app.py
```

También puede utilizarse:

```cmd
python src\app.py
```

## Ejecutar las pruebas

```cmd
scripts\run_tests.bat
```

También pueden ejecutarse directamente:

```cmd
py -m unittest discover -s tests -p "test_*.py"
```

## Elementos de configuración

Los elementos controlados son:

| Elemento | Propósito |
|---|---|
| `README.md` | Instrucciones generales del proyecto. |
| `CHANGELOG.md` | Registro de cambios. |
| `docs/SRS/SRS_v1.md` | Requisitos del sistema. |
| `docs/SDD/SDD_v1.md` | Diseño técnico. |
| `src/app.py` | Código fuente. |
| `tests/test_app.py` | Pruebas unitarias. |
| `config/config.example` | Configuración de ejemplo. |
| `scripts/run_tests.bat` | Ejecución automatizada de pruebas. |

## Crear la línea base

Antes de crear la línea base se debe confirmar que:

1. La rama activa sea `main`.
2. No existan cambios pendientes.
3. La aplicación funcione.
4. Las pruebas terminen correctamente.
5. El SRS y el SDD estén completos.

Comandos:

```cmd
git checkout main
git status
py src\app.py
scripts\run_tests.bat
git tag -a v1.0 -m "Baseline v1.0: SRS, SDD, source, tests and configuration approved"
git push origin v1.0
```

## Verificar la línea base

```cmd
git show v1.0
git log --oneline --decorate
```

También puede reconstruirse la versión exacta:

```cmd
git checkout v1.0
py src\app.py
scripts\run_tests.bat
git checkout main
```

## Control de cambios

Los cambios posteriores a la línea base deben realizarse en una rama independiente.

Ejemplo:

```cmd
git checkout -b change/REQ-007
```

Después del cambio se debe crear un commit claro y una Pull Request hacia `main`.

## Autor

Baque Wilthon