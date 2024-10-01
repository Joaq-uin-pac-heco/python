Algoritmo compra_y_venta
	// crear un diafragma de flujo que realice lo siguiente
	// ingrese nombre del comprador
	// ingrese producto
	// ingrese precio
	// ingrese cantidad
	// finalizar productos hasta ingresar el producto
	// ingrese uno de los vendedores o cajeros
	// (que atendio al cliente)
	// calcular el total a pagar
	compra <- precio+calidad
	total_c <- total_c+compra
	// nombre
	Escribir 'ingrese nombre del comprador: '
	Leer nom
	// producto
	Escribir 'ingrese producto: '
	Leer pro
	Mientras pro<>'x' Hacer
		// precio
		Repetir
			Escribir 'ingrese precio: '
			Leer pre
		Hasta Que pre>=1
		Repetir
			Escribir 'ingrese cantidad: '
			Leer can
		Hasta Que can>=1
		compra <- precio*cantidad
		total_c <- total_c+compra
		Escribir "ingrese producto: "
		Leer pro
	FinMientras
	// cantidad
	// vendedores o cajeros
	Repetir
		Escribir 'ingrese vendedor: '
		Escribir '1: mike maquina del mal'
		Escribir '2: davooxeneizer'
		Escribir '3: betito4k'
		// ingrese uno de los vendedores
		Leer ven
	Hasta Que ven=='1' O ven=='2' O ven=='3'
	Si ven=='1' Entonces
	FinSi
	Si ven=='2' Entonces
	FinSi
	Si ven=='3' Entonces
	FinSi
FinAlgoritmo

