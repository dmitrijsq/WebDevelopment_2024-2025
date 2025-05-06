import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Сервер запущен. Ожидание подключения...")


client_socket, client_address = server_socket.accept()
print(f"Подключен клиент: {client_address}")

# Получаем сообщение от клиента
data = client_socket.recv(1024).decode('utf-8')
print(f"Получено от клиента: {data}")


client_socket.send("Hello, client".encode('utf-8'))


client_socket.close()
server_socket.close()