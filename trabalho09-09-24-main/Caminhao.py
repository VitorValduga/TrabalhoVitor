from os import rename
from Veiculo import Veiculo
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano,Cap_carga):
        super().__init__(marca, modelo, placa, ano)
        self.__Cap_Carga = Cap_carga
    def __str__(self):
        ret = super().__str__()
        return f'''{ret}
    - Cap. Carga:{self.__Cap_Carga}'''
