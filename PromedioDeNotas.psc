Algoritmo PromedioDeNotas
	//definimos las variables.
	Definir numero_1,numero_2,numero_3, resultado Como Real;
	//Aqui introducimos las notas.
	Escribir "introdusca su primera nota";
	Leer numero_1;
	Escribir "intrusca su segunda nota";
	Leer numero_2;
	Escribir "introdusca su tercera nota";
	Leer numero_3;
		//Aqui se realiza la operacion.
	resultado = (numero_1+numero_2+numero_3)/3;
	si resultado >= 40 Entonces
		//aqui se muestra las variables entre el aprobar y reprobar.
		Escribir "aprobaste";
	SiNo
		Escribir "reprobaste";
	FinSi
	
	
	
	
	
FinAlgoritmo
