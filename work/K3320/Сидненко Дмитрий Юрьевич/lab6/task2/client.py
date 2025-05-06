import socket

# Создаём клиентский сокет
client_socket = socket.socket()
client_socket.connect(('localhost', 12345))

# Вводим коэффициенты
print("Введите коэффициенты a, b, c через пробел:")
a, b, c = input().split()


client_socket.send(f"{a} {b} {c}".encode())

# Получаем ответ
result = client_socket.recv(1024).decode()
print("Результат:", result)


client_socket.close()