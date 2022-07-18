import socket
import time


def client_try_connect():
    # soc.connect(('3.115.24.93', 12345))
    # soc.connect(('172.21.65.74', 12345))
    while True:
        try:
            print("try connecting...")
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            soc.connect(('127.0.0.1', 12341))
            print(soc)
            while True:
                try:
                    data = soc.recv(4096)
                    data = data.decode()
                    print("Server:", data)  # サーバー側の書き込みを表示

                    # data = input("Client>")  # 入力待機
                    data += ":c:"
                    data = data.encode('utf-8')
                    soc.send(data)  # ソケットに入力したデータを送信

                    if data == "/end":  # /endが押されたら終了
                        soc.close()
                        break
                except:
                    print("error socket network")
                    soc.close()
                    time.sleep(3)
                    break

        except ConnectionRefusedError:  # ec2でsocketサーバーが建っていなかったとき接続を再度試みる
            print("ConnectionRefusedError")
            time.sleep(5)


if __name__ == "__main__":
    client_try_connect()
