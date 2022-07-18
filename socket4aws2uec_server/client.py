import socket


def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # soc.connect(('3.115.24.93', 12345))
    # soc.connect(('172.21.65.74', 12345))
    soc.connect(('127.0.0.1', 12340))

    while(1):
        data = input("Client>")  # 入力待機
        data = data.encode('utf-8')
        soc.send(data)  # ソケットに入力したデータを送信

        data = soc.recv(4096)
        data = data.decode()
        print("Server:", data)  # サーバー側の書き込みを表示

        if data == "/end":  # /endが押されたら終了
            soc.close()
            break


main()
