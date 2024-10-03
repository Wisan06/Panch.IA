import pika

# Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar la cola
channel.queue_declare(queue='ventas_cola')

def enviar_venta(cliente, producto, cantidad, precio):
    mensaje = f"Cliente: {cliente}, Producto: {producto}, Cantidad: {cantidad}, Precio Total: {cantidad * precio} COP"
    channel.basic_publish(exchange='', routing_key='sales_queue', body=mensaje)
    print(f"[x] Venta registrada: {mensaje}")

# Ejemplo de venta
enviar_venta("Juan Perez", "Pan Normal", 3, 5000)

# Cerrar la conexión
connection.close()
