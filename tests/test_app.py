"""Pruebas unitarias del sistema básico de turnos."""

import sys
import unittest
from pathlib import Path


SRC_DIRECTORY = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIRECTORY))

import app


class TestTurnManager(unittest.TestCase):
    """Pruebas para la gestión básica de turnos."""

    def setUp(self) -> None:
        app.limpiar_turnos()

    def test_crear_turno(self) -> None:
        turno = app.crear_turno("Ana")

        self.assertEqual(turno["id"], 1)
        self.assertEqual(turno["nombre"], "Ana")
        self.assertEqual(turno["estado"], "pendiente")

    def test_ids_consecutivos(self) -> None:
        primer_turno = app.crear_turno("Ana")
        segundo_turno = app.crear_turno("Carlos")

        self.assertEqual(primer_turno["id"], 1)
        self.assertEqual(segundo_turno["id"], 2)

    def test_listar_turnos(self) -> None:
        app.crear_turno("Ana")
        app.crear_turno("Carlos")

        resultado = app.listar_turnos()

        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0]["nombre"], "Ana")
        self.assertEqual(resultado[1]["nombre"], "Carlos")

    def test_rechazar_nombre_vacio(self) -> None:
        with self.assertRaises(ValueError):
            app.crear_turno("   ")


if __name__ == "__main__":
    unittest.main()