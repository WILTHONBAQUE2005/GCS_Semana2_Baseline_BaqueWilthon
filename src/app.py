from typing import Dict, List


Turno = Dict[str, object]
turnos: List[Turno] = []


def crear_turno(nombre: str) -> Turno:
    """Registra un turno utilizando un nombre válido."""

    if not isinstance(nombre, str):
        raise TypeError("El nombre debe ser texto.")

    nombre_limpio = nombre.strip()

    if not nombre_limpio:
        raise ValueError("El nombre no puede estar vacío.")

    turno: Turno = {
        "id": len(turnos) + 1,
        "nombre": nombre_limpio,
        "estado": "pendiente",
    }

    turnos.append(turno)
    return turno


def listar_turnos() -> List[Turno]:
    """Devuelve una copia de los turnos registrados."""

    return turnos.copy()


def limpiar_turnos() -> None:
    """Elimina todos los turnos almacenados en memoria."""

    turnos.clear()


def main() -> None:
    """Ejecuta una demostración básica."""

    print("Sistema básico de turnos - Baseline v1.0")

    turno = crear_turno("Usuario demo")

    print("Turno registrado:")
    print(turno)

    print("Lista de turnos:")
    print(listar_turnos())


if __name__ == "__main__":
    main()