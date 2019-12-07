import unirest
import json

estudiantes = unirest.get("http://localhost:4567/rest/estudiantes/", headers={ "Accept": "application/json" })

print "Lista de Estudiantes: \n" + str(estudiantes.body)

matricula = 1
estudianteX = unirest.get("http://localhost:4567/rest/estudiantes/" + str(matricula), headers={ "Accept": "application/json" })

print "Estudiante #1 Consultado: \n" + str(estudianteX.body)

crearEstudiante = unirest.post("http://localhost:4567/rest/estudiantes/", headers={ "Accept": "application/json", "Content-Type": "application/json" },
                               params=json.dumps({ "nombre": "Jean y Roselin", "correo": "jeanyrose@rest.com", "carrera": "ISC" }))

print "Estudiante Nuevo Creado: \n" + str(crearEstudiante.body)