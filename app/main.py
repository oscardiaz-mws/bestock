from src.sitios.alkosto import Alkosto
from src.sitios.ap_computadores import ApComputadores
from src.utilidades import demorarConsulta
from src.BestockDbContext import limpiarDatos
import json

f = open("app\\articulos.json", "r")
jparsed = json.loads(f.read())

alk = Alkosto()
apComp = ApComputadores()

limpiarDatos()

for nombreArticulo in jparsed:
    print('Consultando artículo: ' + nombreArticulo)
    demorarConsulta()
    print('Buscando en Alkosto')
    alk.consultarArticulos(nombreArticulo)
    print('Termina de buscar en Alkosto')
    print('Buscando en AP Computadores')
    demorarConsulta()
    apComp.consultarArticulos(nombreArticulo)
    print('Termina de buscar en AP Computadores')

print('Terminado')