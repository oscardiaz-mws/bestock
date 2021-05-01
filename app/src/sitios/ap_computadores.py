import requests
from bs4 import BeautifulSoup
from ..models.articulo import Articulo, Propiedad
from ..utilidades import demorarConsulta
from ..BestockDbContext import insertarArticulo

## Navegador
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class ApComputadores:
    def configure_driver(self):
        # Add additional Options to the webdriver
        chrome_options = Options()
        # add the argument and make the browser Headless.
        chrome_options.add_argument("--headless")
        # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
        driver = webdriver.Chrome(options = chrome_options)
        return driver
    
    def consultarArticulos(self, nombreArticulo):
        driver = self.configure_driver()
        urlBase = "https://www.apcomputadores.com"
        params = { 's': nombreArticulo, 'post_type': 'product' }
        rq = requests.get(urlBase, params = params )

        if rq.status_code == 200:
            soup = BeautifulSoup(rq.text, 'html.parser')
            articulosTags = soup.select('.product-item')

            for articuloTag in articulosTags:                
                nuevoArticulo = Articulo()

                infoPrincipalTag = articuloTag.select_one('.category-discription-grid')
                nombreTag = infoPrincipalTag.select_one('h4 > a')

                nuevoArticulo.nombre = nombreTag.text
                nuevoArticulo.precio = float(infoPrincipalTag.select_one('.woocommerce-Price-amount').text.replace('$', '').replace('.', ''))

                link = nombreTag['href']
                # link = link[link.find('/', 8): len(link) - 1]

                nuevoArticulo.url = link

                print('link: ' + link)

                demorarConsulta()

                driver.get(link)

                try:
                    WebDriverWait(driver, 5).until(lambda s: s.find_element_by_class_name("woocommerce-product-details__short-description").is_displayed())
                    soup2 = BeautifulSoup(driver.page_source, "html")

                    propiedadesTag = soup2.select('.woocommerce-product-details__short-description li')

                    for propiedadTag in propiedadesTag:
                        nuevaPropiedad = Propiedad()

                        textoPropiedad = propiedadTag.text

                        if textoPropiedad.find(":") > 0:
                            nuevaPropiedad.nombre = textoPropiedad[:textoPropiedad.find(":")]
                            nuevaPropiedad.descripcion = textoPropiedad[textoPropiedad.find(":") + 1:].strip()
                        else:
                            nuevaPropiedad.descripcion = textoPropiedad
                        
                        nuevoArticulo.propiedades.append(nuevaPropiedad)

                except TimeoutException:
                    print("TimeoutException: Element not found")

                driver.quit()

                insertarArticulo(nuevoArticulo)