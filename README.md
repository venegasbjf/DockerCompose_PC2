# DockerCompose_PC2
Actividad de Docker compose.

# Comandos para las pruebas

Para registrarse:
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"pass"}' http://localhost:8080/auth/signup

Reemplaze user1 y pass por el ususario y contraseña deseados.

Para iniciar sesión:
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"pass"}' http://localhost:8080/auth/login

Reemplaze user1 y pass por el ususario y contraseña utilizado al registrarse.

Para Crear una nota:
curl -X POST -H "Content-Type: application/json" -d '{"id":1,"idEstudiante":123,"notaEstudiante":95}' http://localhost:8080/notes

Reemplaze los contenidos de id, idEstudiante y notaEstudiante por los que usted desee.

Para obtener todas la notas:
curl -X GET http://localhost:8080/notes

Para obtener una nota especifica:
curl -X GET http://localhost:8080/notes/1

Reemplace el numero al final del comando con el id de la nota deseada

Para eliminar una nota:
curl -X DELETE http://localhost:8080/notes/1

Reemplace el numero al final del comando con el id de la nota deseada
