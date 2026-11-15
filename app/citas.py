class HorarioNoDisponible(Exception):
    pass


class CitaService:
    def __init__(self, repo):
        self.repo = repo

    def reservar(self, paciente_id, profesional_id, bloque):
        if self.repo.existe(profesional_id, bloque):
            raise HorarioNoDisponible("El bloque ya está reservado")
        cita = {
            "paciente": paciente_id,
            "profesional": profesional_id,
            "bloque": bloque,
        }
        self.repo.guardar(cita)
        return cita
    