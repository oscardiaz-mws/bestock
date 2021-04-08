import pyodbc

class BestockDB:
  server = '.\SQLEXPRESS' 
  database = 'bestock' 
  username = '.\administrador' 
  password = 'AJ426073' 
  
  def conectar(self):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
    return cnxn.cursor()