#Trabajaremos con minutos
Triaje=["Rojo","Verde","Azul","Amarillo","Naranja"]
Rojo=[0]
Verde=[110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,128,129,130]
Azul=[230,231,232,233,234,235,236,237,238,239,240,240,241,242,243,244,245,246,247,248,249,250]
Naranja=[10,11,12,13,14,15,16,17,19,20]
Amarillo=[50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70]
archivo=open("NombresMujeres", "r", encoding="utf8")#encodig->utf8 es un comando para que admita las tildes
archivo2=open("NombresHombres","r",encoding="utf8")
Genero=["Hombre","Mujer"]
NombresMujeres=archivo.read().split("\n")#con el .read->vamos a leer el archivo y con el putno split vamso a convertirlo en una lista donde el corte va ser \n
NombreHombres=archivo2.read().split("\n")#creamos una lista con el nombre de todos los hombres
Apellidos=['Garcia', 'Rodriguez', 'Gonzalez', 'Fernandez', 'Lopez', 'Martinez', 'Sanchez', 'Perez', 'Gomez', 'Martin',
           'Jimenez', 'Hernandez', 'Ruiz', 'Diaz', 'Moreno', 'Muñoz', 'Alvarez', 'Romero', 'Gutierrez', 'Alonso', 'Navarro',
           'Torres', 'Dominguez', 'Ramos', 'Vazquez', 'Ramirez', 'Gil', 'Serrano', 'Morales', 'Molina', 'Blanco', 'Suarez',
           'Castro', 'Ortega', 'Delgado', 'Ortiz', 'Marin', 'Rubio', 'Nuñez', 'Sanz', 'Medina', 'Iglesias', 'Castillo', 'Cortes',
           'Garrido', 'Santos', 'Guerrero', 'Lozano', 'Cano', 'Mendez', 'Cruz', 'Prieto', 'Flores', 'Herrera', 'Peña', 'Leon',
           'Marquez', 'Cabrera', 'Gallego', 'Calvo', 'Vidal', 'Campos', 'Reyes', 'Vega', 'Fuentes', 'Carrasco', 'Diez', 'Aguilar',
           'Caballero', 'Nieto', 'Santana', 'Pascual', 'Herrero', 'Vargas', 'Gimenez', 'Montero', 'Hidalgo', 'Lorenzo', 'Santiago',
           'Ibañez', 'Duran', 'Benitez', 'Ferrer', 'Arias', 'Mora', 'Carmona', 'Vicente', 'Rojas', 'Soto', 'Crespo', 'Roman', 'Pastor',
           'Velasco', 'Parra', 'Saez', 'Moya', 'Bravo', 'Soler', 'Gallardo', 'Rivera']
