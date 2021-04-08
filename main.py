from src.sitios.alkosto import Alkosto
from src.utilidades import demorarConsulta
import json

articuloBuscar = "portátil"
# demorarConsulta()
# alk = Alkosto().consultarArticulos(articuloBuscar)

f = open("./articulos.JSON", "r")
jparsed = json.loads(f.read())
print(jparsed[2])