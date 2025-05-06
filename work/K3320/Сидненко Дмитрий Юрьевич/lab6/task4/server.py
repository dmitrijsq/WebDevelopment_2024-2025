import socket
import threading

clients = []


def handle_client(client_socket, address):
    print(f"Новое подключение: {address}")
    clients.append(client_socket)

    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{address}: {message}")
            broadcast(message, client_socket)
    except:
        print(f"Клиент {address} отключился")
    finally:
        clients.remove(client_socket)
        client_socket.close()


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("Сервер чата запущен. Ожидание подключений...")

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()


if __name__ == "__main__":
    start_server()