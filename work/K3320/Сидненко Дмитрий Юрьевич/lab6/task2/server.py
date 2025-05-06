import socket
import math


server_socket = socket.socket()
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Сервер запущен. Ждём подключения...")


conn, addr = server_socket.accept()
print("Клиент подключен:", addr)


data = conn.recv(1024).decode()
a, b, c = map(float, data.split())

# Решаем уравнение
discriminant = b**2 - 4*a*c
if discriminant < 0:
    result = "Нет корней"
elif discriminant == 0:
    x = -b / (2*a)
    result = f"Один корень: {x}"
else:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    result = f"Два корня: {x1} и {x2}"


conn.send(result.encode())


conn.close()
server_socket.close()