import pyodbc

class BestockDbContext:
  server = 'localhost,1433'
  database = 'bestock'
  username = 'sa'
  password = 'Lechediaz.7'

  def __init__(self):
    self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
  
  def desconectar(self):
    self.cnxn.close()

def limpiarDatos():
  print('Limpiando datos')
  db = BestockDbContext()
  cursor = db.cnxn.cursor()
  cursor.execute('DELETE from Propiedad')
  cursor.execute('DELETE from Articulo')
  cursor.commit()
  db.desconectar()
  print('Termina de limpiar datos')

def insertarArticulo(articulo):
  print('Insertando artículo ' + articulo.nombre)
  db = BestockDbContext()
  cursor = db.cnxn.cursor()

  #Sample insert query
  cursor.execute("""INSERT INTO Articulo (nombre, precio, url, tieneDescuento, descuento) 
  VALUES (?,?,?,?,?)""",
  articulo.nombre, articulo.precio, articulo.url, articulo.tieneDescuento, articulo.descuento)
  cursor.commit()
  cursor.execute("SELECT @@IDENTITY AS ID;")
  
  articuloId = cursor.fetchone()[0]

  for prop in articulo.propiedades:
    cursor.execute("""INSERT INTO Propiedad (nombre, descripcion, articuloId) 
    VALUES (?,?,?)""",
    prop.nombre, prop.descripcion, articuloId)
    cursor.commit()
  
  db.desconectar()
  print('Artìculo insertado')
