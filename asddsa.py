import os 
#comenzamos creando una funcion que recibe 3 parametros, categoria dia y hora, y comenzamos con un monto base con condicionales.
def calcular_importe_cobrar(categoria, dia, horario):
    importe_base = 0
    
    if categoria == "moto":
        importe_base = 5
    elif categoria == "auto":
        importe_base = 10
    elif categoria == "camioneta":
        importe_base = 15
    elif categoria == "camion":
        importe_base = 20
    
    if dia >= 1 and dia <= 5:  #si es mayor o igual a 1 y menor o igual a 5 seria de L a V, considerando numericamente los dias de la semana 
        if horario == "a": 
            importe_base *= 1.2
        else: 
            importe_base *= 0.8
    else:  
        importe_base *= 0.8
    
    return importe_base

def calcular_vuelto(importe_cobrar, importe_entregado):
    vuelto = importe_entregado - importe_cobrar
    return vuelto

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_resultados(importe_cobrar, vuelto):
    limpiar_pantalla()
    print("Importe a cobrar:", importe_cobrar)
    print("Vuelto a entregar:", vuelto)

def main():
    ventas_auto_pico = 0
    total_pases = 0
    total_recaudado = 0
    
    continuar_ventas = True
    while continuar_ventas:
        limpiar_pantalla()
        
        categoria = input("Ingrese la categoría del vehículo (moto/auto/camioneta/camión): ")
        dia = int(input("Ingrese el día de la semana (1-7): "))
        horario = input("Ingrese el horario (a/b): ")
        importe_entregado = float(input("Ingrese el importe entregado por el conductor: "))
        
        importe_cobrar = calcular_importe_cobrar(categoria, dia, horario)
        vuelto = calcular_vuelto(importe_cobrar, importe_entregado)
        
        mostrar_resultados(importe_cobrar, vuelto)
        
        if categoria == "auto" and horario == "a":
            ventas_auto_pico += 1
        
        total_pases += 1
        total_recaudado += importe_cobrar
        
        respuesta = input("¿Desea continuar vendiendo? (s/n): ")
        if respuesta.lower() != "s":
            continuar_ventas = False
    
    limpiar_pantalla()
    print("Cantidad de ventas de categoría auto en horario pico:", ventas_auto_pico)
    print("Total de pases vendidos:", total_pases)
    print("Total recaudado:", total_recaudado)

main()
