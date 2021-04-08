import requests
from bs4 import BeautifulSoup
from models.articulo import Articulo, Propiedad

class Alkosto:
    urlBase = "https://www.alkosto.com/salesperson/result/"
    
    def consultarArticulo(self, nombreArticulo):
        params = { 'q': nombreArticulo }
        rq = requests.get(self.urlBase, params = params )
        correcto = rq.status_code == 200

        if correcto:
            soup = BeautifulSoup(rq.text, 'html.parser')
            # articulosTags = soup.select('ul.products-grid > li')
            articulosTags = soup.select('ul.products-grid > li')[:3]

            for articuloTag in articulosTags:
                nuevoArticulo = Articulo()
                nuevoArticulo.nombre = articuloTag.h2.a.text
                nuevoArticulo.url = articuloTag.h2.a['href']
                nuevoArticulo.precio = float(articuloTag.select_one('span.price').text.strip()[2:].replace(".", ""))

                precioAntesTag = articulo.select_one('span.price-old')

                nuevoArticulo.tieneDescuento = precioAntesTag != None

                if nuevoArticulo.tieneDescuento:
                    precioAntes = float(precioAntesTag.text.strip()[2:].replace(".", ""))
                    diferencia = precioAntes - nuevoArticulo.precio
                    nuevoArticulo.descuento = diferencia / precioAntes

                rq2 = requests.get(nuevoArticulo.url)

                if rq2.status_code == 200:
                    soup2 = BeautifulSoup(rq2.text, 'html.parser')
                    propiedadesTags = soup2.select(".tab-container")[1].find_all("tr")

                    for propiedadTag in propiedadesTags:
                        nuevaPropiedad = Propiedad()
                        nuevaPropiedad.nombre = propiedadTag.find(class_="label").text
                        nuevaPropiedad.descripcion = propiedadTag.find(class_="data").text

                        nuevoArticulo.propiedades.append(nuevaPropiedad)
                
            # TODO: Guardar articulo en la BD

            print(nuevoArticulo)
        return correcto
