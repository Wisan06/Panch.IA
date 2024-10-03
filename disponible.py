import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='disponible')

def actualizar_disponibilidad(producto, disponible):
    mensaje = f"Producto: {producto}, Disponible: {disponible}"
    channel.basic_publish(exchange='', routing_key='availability_queue', body=mensaje)
    print(f"[x] Enviado: {mensaje}")

# Ejemplo
actualizar_disponibilidad("Pan Común", False)

connection.close()
