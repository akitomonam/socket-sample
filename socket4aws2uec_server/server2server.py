import socket
import time
# EC2側のソケットプログラム（大学サーバーのインバウンド通信の設定で大学サーバーはクライアントでなければならないため）


def server2server():
    while True:
        print("start connecting...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.bind(('172.21.65.74', 12345))    # 指定したホスト(IP)とポートをソケットに設定
        s.bind(('127.0.0.1', 12340))    # 指定したホスト(IP)とポートをソケットに設定
        s.listen(1)                     # 1つの接続要求を待つ
        soc, addr = s.accept()          # 要求が来るまでブロック
        print("Connected by" + str(addr))  # サーバ側の合図

        # 大学サーバーと通信するようのソケットサーバー
        s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s2.bind(('172.21.65.74', 12345))    # 指定したホスト(IP)とポートをソケットに設定
        s2.bind(('127.0.0.1', 12341))    # 指定したホスト(IP)とポートをソケットに設定
        s2.listen(1)                     # 1つの接続要求を待つ
        soc2, addr2 = s2.accept()          # 要求が来るまでブロック
        print("Connected by" + str(addr2))  # サーバ側の合図

        while True:
            try:
                # websocket(client)からデータ受信
                data = soc.recv(4096)       # データを受信（1024バイトまで）
                data = data.decode()
                print("Server(1):", data)       # websocketから受け取ったデータを表示

                # data = input("Server>")  # 入力待機(サーバー側)
                data = data + ":a:"
                data = data.encode('utf-8')
                soc2.send(data)              # 大学サーバにデータを送信

                # 大学サーバーからデータの受信
                data = soc2.recv(4096)       # データを受信（1024バイトまで）
                data = data.decode()
                print("Server(2):", data)       # サーバー側の書き込みを表示

                # websocket(client)へデータを送信
                data = data + ":b:"
                data = data.encode('utf-8')
                soc.send(data)              # websocket(client)にデータを送信

                if "/end" in str(data):             # /endが押されたら終了
                    soc.close()
                    soc2.close()
                    break
            except:
                print("Error occurs")
                soc.close()
                soc2.close()
                time.sleep(3)
                break


if __name__ == "__main__":
    server2server()
