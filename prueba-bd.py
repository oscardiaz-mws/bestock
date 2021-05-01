from app.src.models.articulo import Articulo, Propiedad
from app.src.BestockDbContext import insertarArticulo


articulo = Articulo()

articulo.nombre = 'Articulo 1'
articulo.precio = 123456.789
articulo.url = 'internet.com'

prop1 = Propiedad()
prop2 = Propiedad()
prop3 = Propiedad()

prop1.nombre = 'prop 1'
prop1.descripcion = 'valor 1'
prop2.nombre = 'prop 2'
prop2.descripcion = 'valor 2'
prop3.nombre = 'prop 3'
prop3.descripcion = 'valor 3'

articulo.propiedades.append(prop1)
articulo.propiedades.append(prop2)
articulo.propiedades.append(prop3)

insertarArticulo(articulo)
