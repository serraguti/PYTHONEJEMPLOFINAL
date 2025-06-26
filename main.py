import services.ServiceDepartamentos as service
from models.departamento import Departamento

print("Ejemplo completo fin Python basico")
id: int = int(input("Id del departamento: "))
nombre: str = input("Nombre del departamento: ")
localidad: str = input("Localidad: ")
departamento: Departamento = Departamento()
departamento.id = id
departamento.nombre = nombre
departamento.localidad = localidad
status = service.insertDepartamento(departamento)
print(f"Status insert: {status}")
#Probamos la llamada al servicio
departamentos:list[Departamento] = service.getDepartamentos()
for dept in departamentos:
    print(f"Id: {dept.id}, {dept.nombre}, {dept.localidad}")
print("Fin de programa")
