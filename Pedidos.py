import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='pedido_cola')

def enviar_pedido(cliente, producto, cantidad):
    mensaje = f"Pedido de {cliente}: {producto} x {cantidad}"
    channel.basic_publish(exchange='', routing_key='order_queue', body=mensaje)
    print(f"[x] Pedido enviado: {mensaje}")

# Ejemplo
enviar_pedido("Juanito Paez", "Pan tajado", 10)
enviar_pedido("Juanito Paez", "Pan tajado", 10)
enviar_pedido("Juanito Paez", "Pan tajado", 10)
enviar_pedido("Juanito Paez", "Pan tajado", 10)

connection.close()
