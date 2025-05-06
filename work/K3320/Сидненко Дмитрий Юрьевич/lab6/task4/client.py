import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Соединение разорвано!")
            client_socket.close()
            break

def start_client():
    nickname = input("Введите ваш никнейм: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        if message.lower() == 'exit':
            break
        full_message = f"{nickname}: {message}"
        client_socket.send(full_message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    start_client()