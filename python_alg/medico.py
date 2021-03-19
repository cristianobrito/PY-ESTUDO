import sqlite3
from sqlite3 import Error
import teste


class Medico:
    def __init__(self, nome, crm):
        self.nome_medico = nome
        self.crm_medico = crm

    def mostrar_medico(self):
        print(self.nome_medico, " ", self.crm_medico)


