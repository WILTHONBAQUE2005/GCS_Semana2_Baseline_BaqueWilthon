@echo off
echo Ejecutando pruebas del sistema de turnos...
echo.

python -m unittest discover -s tests -p "test_*.py"

if errorlevel 1 (
    echo.
    echo Las pruebas presentaron errores.
    exit /b 1
)

echo.
echo Todas las pruebas finalizaron correctamente.