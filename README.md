**Contexto
El equipo de Seguridad Informática de MiProgramita.co, se encarga de hacer las reválidas anuales del proceso de clasificación de la información. Sabemos por el feedback del año pasado, que generar reuniones presenciales para validar esto, es un poco molesto para el usuario, más aún cuando las bases no son muy críticas. 
Por eso y dado que estamos cerca de la fecha de reválida de bases de datos, este año queremos hacerlo de manera automática. Pensamos pedirle a los managers de las bases más críticas que nos den el OK por mail.


**Instrucciones y requerimientos
> Docker Desktop

1. Descargar todo
2. Entrar al folder (app)
3. Ejecutar lo siguiente (Compose hara el resto)

docker-compose up 

4. entrar a http://localhost:5000
5. Subir los archivos
6. Conexion a la db db://localhost:3306 user:root password:root_password (Obviamente esto no es seguro. Esto es un proceso academico)


**Explicacion Ficheros
db_emptyfields.json > con datos faltantes
db.json > con datos completos
user_info.csv > informacion de los usuarios