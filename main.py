import socket  
"""
Biblioteca de red que permite comunicarse entre maquinas
utilizando protocolos de red TCP/IP
(crea conexiones de red y envia/recibe datos de un cliente y un servidor)
""" 
#Solicitud de ip o hostname
target = input("Ingresar ip o hostname a escanear: ")

#Convertir hostname a ip (solo si se ocupa)

def obtener_ip (target):
    try:
        ip_adress = socket.gethostbyname(target) #aqui se convierte hostname a ip
        return ip_adress
    except socket.gaierror:
        """
        En caso de no resolver el hostname se captura la excepcion
        y muestra mensaje de error
        (ejem: hostname incorrecto o o server DNS no encontrado)
        """
        print(f"Error:No se pudo resolver el hostname '{target}' ")
        return None
    
ip = obtener_ip(target)

if ip: #solo continua si se resuelve la ip
    print (f"Escaneando IP: {ip} (originalmente: {target})")

    #Rango de puertos
    start_port = int (input("Ingresar puerto de inicio: "))
    end_port = int (input("Ingresar puerto final: "))

    print(f"Escaneando desde el puerto {start_port} hasta {end_port}...")

    #Escanea Puertos
    
    """
    Este bucle recorre el rango de puertos y le añadimos un valor final al range
    escaneando puerto por puerto,verificando si esta abierto o cerrado
    """
    for port in range(start_port, end_port +1):
        #crea un TCP
        sock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        """
        AF_INET : utilizamos direcciones IPv4
        SOCK_STEAM : Utilizamos el protocolo TCP a la conexion
        """
        socket.setdefaulttimeout(1) #tiempo espera
        result = sock.connect_ex((ip, port)) # intenta conectarse al puerto
        if  result == 0: #0 = Puerto abierto
            print(f"Puerto {port}: OPEN")
        else:
            print(f"Puerto {port}: CLOSED")
            sock.close() #cerrar conexion para liberar recursos
else:
    print("No se escaneo debido a un error en la resolución del hostname")



