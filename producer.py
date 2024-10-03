import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='product_queue')

def enviar_producto(nombre_producto, cantidad):
    mensaje = f"Producto: {nombre_producto}, Cantidad: {cantidad}"
    channel.basic_publish(exchange='', routing_key='product_queue', body=mensaje)
    print(f"[x] Enviado {mensaje}")


enviar_producto("Pan Integral", 50)
enviar_producto("Chocolitas x 10", 10)

connection.close()
