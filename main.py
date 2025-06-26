import services.ServiceDepartamentos as service
from models.departamento import Departamento

print("Ejemplo completo fin Python basico")
#Probamos la llamada al servicio
departamentos:list[Departamento] = service.getDepartamentos()
for dept in departamentos:
    print(f"Id: {dept.id}, {dept.nombre}, {dept.localidad}")
print("Fin de programa")
