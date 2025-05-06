import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Подключаемся к серверу


client_socket.send("Hello, server".encode('utf-8'))


response = client_socket.recv(1024).decode('utf-8')
print(f"Получено от сервера: {response}")

# Закрываем соединение
client_socket.close()