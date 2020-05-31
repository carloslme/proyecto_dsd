CREATE DATABASE BaseServerP1;
USE BaseServerP1;

CREATE TABLE data(
	id   INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	idpartida INT NOT NULL,
	ip   VARCHAR(45) NOT NULL,
	mensaje VARCHAR(100) NOT NULL,
	horaClient VARCHAR(45) NOT NULL,
	horaServer VARCHAR(45) NOT NULL
)ENGINE=InnoDB;

CREATE TABLE resultados(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	ipganador VARCHAR(45) NOT NULL,
	jugador VARCHAR(45) NOT NULL,
	letra VARCHAR(100) NOT NULL,
	frase VARCHAR(100) NOT NULL,
	ganado BOOLEAN NOT NULL,
	horajugado VARCHAR(45) NOT NULL,
	horainicio VARCHAR(45) NOT NULL
)ENGINE=InnoDB;


CREATE TABLE frases(
	id   INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	pelicula   VARCHAR(45) NOT NULL NOT NULL,
	frase VARCHAR(100) NOT NULL
)ENGINE=InnoDB;

INSERT INTO frases (pelicula,frase) VALUES ("Star Wars","NO LO INTENTES HAZLO");
INSERT INTO frases (pelicula,frase) VALUES ("Rey leon",	"VETE Y NUNCA REGRESES");
INSERT INTO frases (pelicula,frase) VALUES ("Rey leon",	"HAKUNA MATATA");
INSERT INTO frases (pelicula,frase) VALUES ("Aladdin",	"CONFIAS EN MI");
INSERT INTO frases (pelicula,frase) VALUES ("Aladdin",	"UN MUNDO IDEAL");
INSERT INTO frases (pelicula,frase) VALUES ("Rey leon",	"EL PASADO PUEDE DOLER PERO PUEDES HUIR DE EL O APRENDER");
INSERT INTO frases (pelicula,frase) VALUES ("Ratatouille", "UN GRAN ARTISTA PUEDE PROVENIR DE CUALQUIER LUGAR" );
INSERT INTO frases (pelicula,frase) VALUES ("Frozen",	"Y SI HACEMOS UN MUNECO");
INSERT INTO frases (pelicula,frase) VALUES ("Hercules",	"A UN HEROE SE LE MIDE POR EL TAMANO DE SU CORAZON");
INSERT INTO frases (pelicula,frase) VALUES ("Aristogatos",	"TODOS QUIEREN SER YA GATOS JAZ");
INSERT INTO frases (pelicula,frase) VALUES ("Mulan",	"LA FLOR MAS HERMOSA ES LA QUE CRECE ENTRE LA ADVESIDAD");
INSERT INTO frases (pelicula,frase) VALUES ("Rey leon",	"ESTOY RODEADO DE TONTOS");
INSERT INTO frases (pelicula,frase) VALUES ("Tarzan",	"PON TU FE EN LO QUE TU MAS CREAS");
INSERT INTO frases (pelicula,frase) VALUES ("Tarzan",	"TU SIMPRE SERAS MI MADRE");
INSERT INTO frases (pelicula,frase) VALUES ("Tarzan",	"SOY TU MADRE LO SE TODO");
INSERT INTO frases (pelicula,frase) VALUES ("Monsters Inc",	"NO ORDENASTE TU PAPELEO ANOCHE");
INSERT INTO frases (pelicula,frase) VALUES ("Lilo y Stich",	"OHANA SIGNIFICA FAMILIA Y LA FAMILIA NUNCA TE ABANDONA");
INSERT INTO frases (pelicula,frase) VALUES ("Hercules",	"PERO SI SON AERODINAMICAS");
INSERT INTO frases (pelicula,frase) VALUES ("Hercules",	"Y USTEDES ESTAN USANDO SU MERCANCIA");
INSERT INTO frases (pelicula,frase) VALUES ("Monsters Inc",	"GATITO");
INSERT INTO frases (pelicula,frase) VALUES ("Alicia",	"FELIZ FELIZ  NO CUMPLEANOS");
INSERT INTO frases (pelicula,frase) VALUES ("El libro de la selva",	"BUSCA LO MAS VITAL");
INSERT INTO frases (pelicula,frase) VALUES ("Cenicienta",	"BIBIDI BABIDI BU");
INSERT INTO frases (pelicula,frase) VALUES ("Pocahontas",	"ALGUNAS VECES EL CAMINO CORRECTO NO ES EL MAS FACIL");
INSERT INTO frases (pelicula,frase) VALUES ("Aladdin",	"DEBO DEJAR DE PRETENDER SER ALGO QUE NO SOY");
INSERT INTO frases (pelicula,frase) VALUES ("Frozen",	"HAY PERSONAS POR LAS QUE VALE LA PENA DERRETIRSE");
INSERT INTO frases (pelicula,frase) VALUES ("La sirenita",	"NO ES POSIBLE QUE UN MUNDO QUE HACE TANTAS MARAVILLAS SEA TAN MALO");
INSERT INTO frases (pelicula,frase) VALUES ("La bella y la bestia",	"LA BELLEZA ESTA EN EL INTERIOR");
INSERT INTO frases (pelicula,frase) VALUES ("COCO",	"RECUERDAME");
INSERT INTO frases (pelicula,frase) VALUES ("Intensamente",	"LLORAR TRANQUILIZA LOS PROBLEMAS DE LA VIDA");
INSERT INTO frases (pelicula,frase) VALUES ("Peter pan",	"LA SEGUNDA ESTRELLA A LA DERECHA");
INSERT INTO frases (pelicula,frase) VALUES ("Nemo",	"SIGUE NADANDO SIGUE NADANDO");
INSERT INTO frases (pelicula,frase) VALUES ("Toy story",	"NOS HAS SALVADO ESTAMOS AGRADECIDOS");
INSERT INTO frases (pelicula,frase) VALUES ("Bichos",	"SOY UNA HERMOSA MARIPOSA");
INSERT INTO frases (pelicula,frase) VALUES ("Rey leon",	"RECUERDA QUIEN ERES");
INSERT INTO frases (pelicula,frase) VALUES ("Mulan",	"DESHORA SOBRE TU VACA");
INSERT INTO frases (pelicula,frase) VALUES ("Rey leon",	"BISCOSOS PERO SABROSOS");
INSERT INTO frases (pelicula,frase) VALUES ("Toy Story",	"HAY UNA SERPIENTE EN MI BOTA");
INSERT INTO frases (pelicula,frase) VALUES ("Star Wars",	"EL MIEDO ES EL CAMINO HACIA EL LADO OSCURO");
INSERT INTO frases (pelicula,frase) VALUES ("Shrek 1",	"ME JUZGAN SIN NI SIQUIERA CONOCERME");
INSERT INTO frases (pelicula,frase) VALUES ("Shrek 1",	"TAL VEZ NO FUNCIONA EN BURROS");
INSERT INTO frases (pelicula,frase) VALUES ("Shrek 1",	"POR TI BABY SERIA BATMAN");
INSERT INTO frases (pelicula,frase) VALUES ("Shrek 1",	"BROMEAS ES UN PAPUCHO");
INSERT INTO frases (pelicula,frase) VALUES ("Shrek 1",	"MEJOR AFUERA QUE ADENTRO");
INSERT INTO frases (pelicula,frase) VALUES ("La era de hielo",	"VAMOS A MORIR");
INSERT INTO frases (pelicula,frase) VALUES ("Una película de huevos",	"QUE EL COLESTEROL LOS ACOMPANE");
INSERT INTO frases (pelicula,frase) VALUES ("Una película de huevos",	"CONFETI ERES Y EN CONFETI TE CONVERTIRAS");
INSERT INTO frases (pelicula,frase) VALUES ("Una película de huevos",	"QUIEN A HUEVO MATA A HUEVO MUERE");
INSERT INTO frases (pelicula,frase) VALUES ("Las aventuras de Sherlock Holmes", "ELEMENTAL QUERIDO WATSON");
INSERT INTO frases (pelicula,frase) VALUES ("Terminator 2",	"HASTA LA VISTA BABY");
INSERT INTO frases (pelicula,frase) VALUES ("Vengadores 1",	"ESE ES MI SECRETO SIEMPRE ESTOY ENOJADO");
INSERT INTO frases (pelicula,frase) VALUES ("Vengadores 1",	"GENIO MILLONARIO PLAYBOY Y FILANTROPO");
INSERT INTO frases (pelicula,frase) VALUES ("Vengadores 1",	"NOSOTROS TENEMOS UN HULK");
INSERT INTO frases (pelicula,frase) VALUES ("Vengadores 1",	"YO SOY IRONMAN");
INSERT INTO frases (pelicula,frase) VALUES ("Vengadores 1",	"PODRIA HACER ESTO TODO EL DIA");
INSERT INTO frases (pelicula,frase) VALUES ("Batman VS Superman",	"LA IGNORANCIA NO ES LO MISMO QUE LA INOCENCIA");
INSERT INTO frases (pelicula,frase) VALUES ("Titanic",	"SOY EL REY DEL MUNDO");
INSERT INTO frases (pelicula,frase) VALUES ("Titanic",	"ICEBERG AL FRENTE");
INSERT INTO frases (pelicula,frase) VALUES ("Titanic",	"QUIERO QUE ME DIBUJES COMO UNA DE TUS CHICAS FRANCESAS");
INSERT INTO frases (pelicula,frase) VALUES ("Jurassic Park",	"BIENVENIDOS A JURASSIC PARK");
INSERT INTO frases (pelicula,frase) VALUES ("Jurassic Park",	"ODIO SIEMPRE TENER LA RAZON");
INSERT INTO frases (pelicula,frase) VALUES ("Avatar",	"SIGUE TUS PASIONES Y LA VIDA TE PREMIARA");
INSERT INTO frases (pelicula,frase) VALUES ("Avatar",	"UNA VIDA TERMINA Y OTRA COMIENZA");
INSERT INTO frases (pelicula,frase) VALUES ("Forrest Gump",	"TONTO ES EL QUE HACE TONTERIAS");
INSERT INTO frases (pelicula,frase) VALUES ("Forrest Gump",	"PUEDE QUE NO SEA MUY LISTO PERO SI SE LO QUE ES EL AMOR");
INSERT INTO frases (pelicula,frase) VALUES ("Forrest Gump",	"CORRE FORREST CORRE");
INSERT INTO frases (pelicula,frase) VALUES ("Volver al futuro",	"NO SEAS TAN CREDULO MCFLY");
INSERT INTO frases (pelicula,frase) VALUES ("Matrix",	"EN LA IGNORANCIA ESTA LA FELICIDAD");
INSERT INTO frases (pelicula,frase) VALUES ("Matrix",	"EL CUERPO NO PUEDE VIVIR SIN LA MENTE");
INSERT INTO frases (pelicula,frase) VALUES ("Matrix",	"LIBERA TU MENTE");
INSERT INTO frases (pelicula,frase) VALUES ("Matrix",	"BIENVENIDO AL MUNDO REAL");
INSERT INTO frases (pelicula,frase) VALUES ("Harry Potter y la Piedra Filosofal",	"ERES UN MAGO HARRY");
INSERT INTO frases (pelicula,frase) VALUES ("Gladiador",	"FUERZA Y HONOR");
INSERT INTO frases (pelicula,frase) VALUES ("Piratas del Caribe 1",	"NO TODOS LOS TESOROS SON PLATA Y ORO AMIGO");
INSERT INTO frases (pelicula,frase) VALUES ("Piratas del Caribe 1",	"NUNCA ME ARREPIENTO DE NADA JAMAS");
INSERT INTO frases (pelicula,frase) VALUES ("Piratas del Caribe 1",	"ESCONDE EL RON");
INSERT INTO frases (pelicula,frase) VALUES ("Batman El Caballero Oscuro",	"SI SE TE DA ALGO BIEN NUNCA LO HAGAS GRATIS");
INSERT INTO frases (pelicula,frase) VALUES ("Batman El Caballero Oscuro",	"SOY LO QUE GOTHAM NECESITA QUE SEA");
INSERT INTO frases (pelicula,frase) VALUES ("Batman El Caballero Oscuro",	"EL MIEDO TE HACE FRACASAR");
INSERT INTO frases (pelicula,frase) VALUES ("Star Wars",	"YO SOY TU PADRE");
INSERT INTO frases (pelicula,frase) VALUES ("El resplandor",	"AQUI ESTA JOHNNY");
INSERT INTO frases (pelicula,frase) VALUES ("Star Wars",	"QUE LA FUERZA TE ACOMPANE");
INSERT INTO frases (pelicula,frase) VALUES ("Star Wars",	"YO SOY EL SENADO");
INSERT INTO frases (pelicula,frase) VALUES ("It",	"TODOS FLOTAN");
INSERT INTO frases (pelicula,frase) VALUES ("500 dias con ella",	"SUMER DESEO QUE SEAS FELIZ");
INSERT INTO frases (pelicula,frase) VALUES ("Spiderman",	"UN GRAN PODER CONLLEVA UNA GRAN RESPONSABILIDAD");
INSERT INTO frases (pelicula,frase) VALUES ("Batman v Superman",	"ESTAS DEJANDO ASESINAR A MARTHA");
INSERT INTO frases (pelicula,frase) VALUES ("Misery",	"TE QUIERO TANTO");
INSERT INTO frases (pelicula,frase) VALUES ("La milla verde",	"LE DIRA QUE ESTABA HACIENDO SU TRABAJO");
INSERT INTO frases (pelicula,frase) VALUES ("Star Wars",	"PODER ILIMITADO");
INSERT INTO frases (pelicula,frase) VALUES ("Star Wars",	"TENGO UN MAL PRESENTIMIENTO ACERCA DE ESTO");
INSERT INTO frases (pelicula,frase) VALUES ("Batman",	"SOY BATMAN");
INSERT INTO frases (pelicula,frase) VALUES ("Ready Player One",	"PODRIA TRATAR DE UN HOMBRE DE MEDIANA EDAD LLAMADO CHUCK");
INSERT INTO frases (pelicula,frase) VALUES ("Star Wars",	"TE CONVERTISTE EN LO QUE JURASTE DESTRUIR");
INSERT INTO frases (pelicula,frase) VALUES ("Star Wars",	"CLARO QUE LO CONOZCO SOY YO");
INSERT INTO frases (pelicula,frase) VALUES ("Star Wars",	"CHEWEI AL FIN EN CASA");
INSERT INTO frases (pelicula,frase) VALUES ("La era del hielo",	"TARADO LO ASUSTAS");
INSERT INTO frases (pelicula,frase) VALUES ("Buscando a nemo",	"PAPI TE CUIDA");
INSERT INTO frases (pelicula,frase) VALUES ("Batman",	"CAEMOS BRUCE PARA VOLVER A LEVANTARNOS");
INSERT INTO frases (pelicula,frase) VALUES ("Buscando a nemo",	"NADAREMOS EN EL MAR");
INSERT INTO frases (pelicula,frase) VALUES ("El rey león",	"HAY QUE DEJAR EL PASADO ATRAS");
INSERT INTO frases (pelicula,frase) VALUES ("Toy Story",	"AL INFINITO Y MAS ALLA");
INSERT INTO frases (pelicula,frase) VALUES ("Monsters Inc",	"PON ESA COSA HORROROSA AHI O VERAS");
INSERT INTO frases (pelicula,frase) VALUES ("El exorcista",	"ES HORRIBLE HORRIBLE Y FASCINANTE");
INSERT INTO frases (pelicula,frase) VALUES ("E.T.",	"ET CASA LLAMA");
INSERT INTO frases (pelicula,frase) VALUES ("Buscando a nemo",	"SIGUE NADANDO");
INSERT INTO frases (pelicula,frase) VALUES ("Buscando a nemo",	"P SHERMAN CALLE WALLABY CUARENTA Y DOS SYDNEY");
INSERT INTO frases (pelicula,frase) VALUES ("El gran dictador",	"PENSAMOS DEMASIADO Y SENTIMOS MUY POCO");
INSERT INTO frases (pelicula,frase) VALUES ("El sexto sentido",	"VEO GENTE MUERTA");
INSERT INTO frases (pelicula,frase) VALUES ("El aro",	"SIETE DIAS");
INSERT INTO frases (pelicula,frase) VALUES ("Poltergeist",	"ELLOS ESTAN AQUI");
INSERT INTO frases (pelicula,frase) VALUES ("Shrek 2",	"YA MERITO LLEGAMOS");
INSERT INTO frases (pelicula,frase) VALUES ("Misery" ,	"SOY TU ADMIRADORA NUMERO UNO");
INSERT INTO frases (pelicula,frase) VALUES ("Hercules",	"EL OLIMPO ESTA POR ALLA");
INSERT INTO frases (pelicula,frase) VALUES ("Hercules",	"AL DEL CABALLO");
INSERT INTO frases (pelicula,frase) VALUES ("Cuestión de tiempo",	"ASI QUE BRINDO POR EL HOMBRE CON EL PEOR CORTE DE PELO Y LA MEJOR NOVIA");
INSERT INTO frases (pelicula,frase) VALUES ("Forest Gump",	"DEMONIOS GUMP ERES UN MALDITO GENIO");
INSERT INTO frases (pelicula,frase) VALUES ("Winnie Pooh",	"ES HORA DE ALGO DULCE");
INSERT INTO frases (pelicula,frase) VALUES ("Harry Potter",	"WINGARDIUM LEVIOSA");
INSERT INTO frases (pelicula,frase) VALUES ("La teoria del todo",	"LA CONDICION DE FRONTERA DEL UNIVERSO ES QUE NO TIENE FRONTERA");
INSERT INTO frases (pelicula,frase) VALUES ("Volver al futuro",	"NADIE ME LLAMA GALLINA");
INSERT INTO frases (pelicula,frase) VALUES ("Volver al futuro",	"TENGA CUIDADO DOC NO LE VAYA A CAER UN RAYO");
INSERT INTO frases (pelicula,frase) VALUES ("Volver al futuro",	"SI TE LO PROPONES PUEDES HACER LO QUE QUIERAS");
INSERT INTO frases (pelicula,frase) VALUES ("El infierno",	"EN ESTE PAIS NO HACE SLO QUE QUIERES HACES LO QUE PUEDES");
INSERT INTO frases (pelicula,frase) VALUES ("El infierno",	"DEJATE DE TONTERIAS HUASTECO");
INSERT INTO frases (pelicula,frase) VALUES ("¿Dónde están las rubias?",	"DIABLOS SENIORITA");
INSERT INTO frases (pelicula,frase) VALUES ("Tizoc",	"CUANDO EL TECOLOTE CANTA EL INDIO MUERE");
INSERT INTO frases (pelicula,frase) VALUES ("Las 7 cucas",	"DEJAE SER UN ERROR DE TU VIDA");
INSERT INTO frases (pelicula,frase) VALUES ("Extraña cita",	"EL FASTIDIO ABRE EL APETITO");
INSERT INTO frases (pelicula,frase) VALUES ("Amarte duele", 	"EN TUS OJOS ME IMAGINO EL MAR AUNQUE NUNCA HAYA IDO");
INSERT INTO frases (pelicula,frase) VALUES ("Tal para cual",	"YO SOY COMO TU UN TIPO DESPRECIABLE PERO FELIZ");
INSERT INTO frases (pelicula,frase) VALUES ("En busca de la felicidad",	"NUNCA DEJES QUE NADIE TE DIGA QUE PUEDES HACER ALGO");
INSERT INTO frases (pelicula,frase) VALUES ("Black hawk derribado",	"ES LO QUE HACES AHORA LO QUE PUEDE MARCAR UNA GRAN DIFERENCIA");
INSERT INTO frases (pelicula,frase) VALUES ("Spider man",	"SOMOS LO QUE ELGIMOS SER");
INSERT INTO frases (pelicula,frase) VALUES ("Harry Potter",	"EXPELLIARMUS");
INSERT INTO frases (pelicula,frase) VALUES ("El padrino",	"LOS GRANDES HOMBRES NO NACES SE HACEN");
INSERT INTO frases (pelicula,frase) VALUES ("Alicia en el pais de las maravillas",	"NO PUEDES VIVIR TU VIDA PARA COMPLACER A OTROS LA ELECCION DEBE SER TUYA");
INSERT INTO frases (pelicula,frase) VALUES ("Braveheart",	"TODOS LOS HOMBRES MUEREN PERO NO TODOS HAN VIVIDO");
INSERT INTO frases (pelicula,frase) VALUES ("Lawrence de Arabia",	"LAS ILUSIONES PUEDEN SER MUY PODEROSAS");
INSERT INTO frases (pelicula,frase) VALUES ("Memento",	"NO ME ACUERDO DE OLVIDARTE");
INSERT INTO frases (pelicula,frase) VALUES ("Mejor...imposible",	"ME HACER QUERER SER UN HOMBRE MEJOR");
INSERT INTO frases (pelicula,frase) VALUES ("El imperio contraataca",	"HAZLO O NO LO HAGAS PERO NO LO INTENTES");
INSERT INTO frases (pelicula,frase) VALUES ("Braveheart",	"PODRAN QUITARNOS LA VIDA PERO NUNCA PODRANA RREBATARNOS LA LIBERTAD");
INSERT INTO frases (pelicula,frase) VALUES ("Con faldas y a lo loco",	"NADIE ES PERFECTO");
INSERT INTO frases (pelicula,frase) VALUES ("El padrino 2",	"DE QUE SIRVE CONFESARME SI NO ME ARREPIENTO");
INSERT INTO frases (pelicula,frase) VALUES ("Cinderella man",	"CON CADA COMBATE TE HACES MAS FUERTE");
INSERT INTO frases (pelicula,frase) VALUES ("Karate kid",	"DAR CERA PULIR CERA");
INSERT INTO frases (pelicula,frase) VALUES ("Avengers",	"SOY INEVITABLE");
INSERT INTO frases (pelicula,frase) VALUES ("Avengers",	"VENGADORES UNIDOS");
INSERT INTO frases (pelicula,frase) VALUES ("Avengers",	"TE QUIERO TRES MIL");
INSERT INTO frases (pelicula,frase) VALUES ("La vida es bella",	"BUENOS DIAS PRINCESA");
INSERT INTO frases (pelicula,frase) VALUES ("Casablanca",	"SIEMPRE NOS QUEDARA PARIS");
INSERT INTO frases (pelicula,frase) VALUES ("Tiburón",	"VAMOS A NECESITAR UN BARCO MAS GRANDE");
INSERT INTO frases (pelicula,frase) VALUES ("Psicosis",	"EL MEJOR AMIGO DE UN CHICO ES SU MADRE");
INSERT INTO frases (pelicula,frase) VALUES ("Lo que el viento se llevó",	"FRANCAMENTE QUERIDA ESO NO IMPORTA");
INSERT INTO frases (pelicula,frase) VALUES ("El padrino",	"LE HARE UNA OFERTA QUE NO PODRA RECHAZAR");
INSERT INTO frases (pelicula,frase) VALUES ("300",	"ESTA NOCHE CENAREMOS EN EL INFIERNO");
INSERT INTO frases (pelicula,frase) VALUES ("Taxi Driver",	"ME ESTAS HABLANDO A MI");
INSERT INTO frases (pelicula,frase) VALUES ("2001: Una Odiseo en el espacio", "TENGO MIEDO DAVE");
INSERT INTO frases (pelicula,frase) VALUES ("Siete Almas",	"TE MENTI PIENSO EN LA MUERTE TODOS LOS DIAS");
INSERT INTO frases (pelicula,frase) VALUES ("Alicia en el pais de las maravillas",	"MI REALIDAD ES DIFERENTE A LA TUYA");
INSERT INTO frases (pelicula,frase) VALUES ("Siete Almas",	"SIEMPRE PENSE QUE ESTE LUGAR PODIA SANAR EL ALMA");
INSERT INTO frases (pelicula,frase) VALUES ("Siete Almas",	"DIJO QUE ERA LA CRIATURA MAS MORTIFERA EN LA TIERRA");
INSERT INTO frases (pelicula,frase) VALUES ("Mujercitas",	"TODOS LLEVAMOS CARGAS TENEMOS UN CAMINO POR RECORRER");
INSERT INTO frases (pelicula,frase) VALUES ("Mujercitas",	"LA VANIDAD ECHA A PERDER LAS MEJORES CUALIDADES");
INSERT INTO frases (pelicula,frase) VALUES ("Mujercitas",	"EL TALENTO Y LA BONDAD NUNCA PASAN INADVERTIDOS");
INSERT INTO frases (pelicula,frase) VALUES ("Mujercitas",	"LAS VIRTUDES QUEDAN ENSALZADAS POR LA MODESTIA");
INSERT INTO frases (pelicula,frase) VALUES ("Mujercitas",	"NO DEJAR QUE LA IRA SE LLEVE LO MEJOR DE MI");
INSERT INTO frases (pelicula,frase) VALUES ("Mujercitas",	"NO ME DIGA QUE EL MATRIMONIO NO ES UN ACUERDO ECONOMICO");
INSERT INTO frases (pelicula,frase) VALUES ("Mujercitas",	"SOY FELIZ CONMIGO MISMA Y MI LIBERTAD");
INSERT INTO frases (pelicula,frase) VALUES ("Mujercitas",	"NO DEJES QUE LA NOCHE TE SORPRENDA ENFADADA");
INSERT INTO frases (pelicula,frase) VALUES ("El diablo viste a la moda",	"ESTOY A UNA DIARREA DE MI PESO IDEAL");
INSERT INTO frases (pelicula,frase) VALUES ("Yo antes de ti",	"VIVE CON ATREVIMIENTO");
INSERT INTO frases (pelicula,frase) VALUES ("Yo antes de ti",	"ESFUERZATE AL MAXIMO");
INSERT INTO frases (pelicula,frase) VALUES ("Yo antes de ti",	"NO TE CONFORMES");
INSERT INTO frases (pelicula,frase) VALUES ("El juego de Ender",	"CUANTO MAS OBEDECES MAS PODER TIENEN SOBRE TI");
INSERT INTO frases (pelicula,frase) VALUES ("El juego de Ender",	"ALGUNAS VECES LAS MENTIRAS ERAN MAS DE FIAR QUE LAS VERDADES");
INSERT INTO frases (pelicula,frase) VALUES ("El juego de Ender",	"NADIE CONTROLA SU PROPIA VIDA ENDER");
INSERT INTO frases (pelicula,frase) VALUES ("El juego de Ender",	"LA HUMANIDAD NO NOS PIDE QUE SEAMOS FELICES");
INSERT INTO frases (pelicula,frase) VALUES ("El diablo viste a la moda",	"ABURRE A ALGUIEN MAS CON TUS PREGUNTAS");
INSERT INTO frases (pelicula,frase) VALUES ("El juego de Ender",	"NO PERMITIRE QUE ME DERROTES JUGANDO SUCIO");
INSERT INTO frases (pelicula,frase) VALUES ("El juego de Ender",	"HE VIVIDO DEMASIADO TIEMPO CON EL DOLOR");
INSERT INTO frases (pelicula,frase) VALUES ("El juego de Ender",	"YO NO LUCHE CON HONOR LUCHE PARA VENCER");
INSERT INTO frases (pelicula,frase) VALUES ("El juego de Ender",	"SI LO INTENTAS Y PIERDES NO SERA CULPA TUYA");
INSERT INTO frases (pelicula,frase) VALUES ("El juego de Ender",	"SOY MAS INUTIL QUE UN ESTORNUDO EN UN TRAJE ESPACIAL");
INSERT INTO frases (pelicula,frase) VALUES ("Warcraft",	"NUESTRO MUNDO AGONIZA");
INSERT INTO frases (pelicula,frase) VALUES ("Warcraft",	"LO QUE TENGAS PLANEADO HACER HAZLO YA");
INSERT INTO frases (pelicula,frase) VALUES ("Dr Strange",	"APEGARSE A LO MATERIAL ES DESAPEGARSE A LO ESPIRITUAL");
INSERT INTO frases (pelicula,frase) VALUES ("Dr Strange",	"THANOS YA VIENE");
INSERT INTO frases (pelicula,frase) VALUES ("Dr Strange",	"EL VERDADERO ENEMIGO ES EL TIEMPO");
INSERT INTO frases (pelicula,frase) VALUES ("Dr Strange",	"EL TIEMPO LO MATA TODO");
INSERT INTO frases (pelicula,frase) VALUES ("Dr Strange",	"OLVIDA TODO LO QUE CREES SABER");
INSERT INTO frases (pelicula,frase) VALUES ("12 años de esclavitud",	"NO QUIERO SOBREVIVIR QUIERO VIVIR");
INSERT INTO frases (pelicula,frase) VALUES ("Jojo Rabbit",	"SIEMPRE HAY TIEMPO PARA EL ROMANCE");
INSERT INTO frases (pelicula,frase) VALUES ("Jojo Rabbit",	"EL BAILE ES PARA LA GENTE QUE ES LIBRE");
INSERT INTO frases (pelicula,frase) VALUES ("Aves de presa",	"A NADIE LE IMPORTAMOS");
INSERT INTO frases (pelicula,frase) VALUES ("Aves de presa",	"YO SOY LA MALDITA HARLEY QUINN");
INSERT INTO frases (pelicula,frase) VALUES ("Alicia en el pais de las maravillas",	"NO PUEDES VIVIR COMPLACIENDO A OTROS");
INSERT INTO frases (pelicula,frase) VALUES ("Corazón Valiente","TODOS MORIMOS LO QUE IMPORTA ES EL COMO Y EL CUANDO");