import pytest
from app.citas import CitaService, HorarioNoDisponible


class RepoMemoria:
    def __init__(self):
        self.datos = []

    def existe(self, prof, bloque):
        return any(
            c["profesional"] == prof and c["bloque"] == bloque
            for c in self.datos
        )

    def guardar(self, cita):
        self.datos.append(cita)


def test_reserva_exitosa():
    svc = CitaService(RepoMemoria())
    assert svc.reservar(1, 10, "2026-12-01T09:00")["paciente"] == 99


def test_doble_reserva_falla():
    svc = CitaService(RepoMemoria())
    svc.reservar(1, 10, "2026-12-01T09:00")
    with pytest.raises(HorarioNoDisponible):
        svc.reservar(2, 10, "2026-12-01T09:00")
