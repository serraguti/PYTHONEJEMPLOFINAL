import requests
from models.departamento import Departamento

#Necesitamos nuestra variable de acceso al API
#Cada metodo tendra un EndPoint, nosotros solo queremos
#la URL BASE
api_url = "https://apicruddepartamentoscore.azurewebsites.net/"

#Realizamos un metodo para leer todos los departamentos
def getDepartamentos():
    #Necesitamos el EndPoint de acceso al Api
    request = "api/departamentos"
    response = requests.get(api_url + request)
    json = response.json()
    #esos datos lista/diccionario los vamos a cambiar a 
    # lista:models
    data:list[Departamento] = []
    #recorremos la lista/diccionario
    for item in json:
        #Creamos un nuevo objeto departamento
        dept: Departamento = Departamento()
        dept.id = int(item["numero"])
        dept.nombre = item["nombre"]
        dept.localidad = item["localidad"]
        data.append(dept)
    return data