import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('172.21.65.74', 12345))    # 指定したホスト(IP)とポートをソケットに設定
    s.listen(1)                     # 1つの接続要求を待つ
    soc, addr = s.accept()          # 要求が来るまでブロック
    print("Connected by" + str(addr))  # サーバ側の合図

    while (1):
        data = soc.recv(4096)       # データを受信（1024バイトまで）
        data = data.decode()
        print("Client:", data)       # サーバー側の書き込みを表示

        data = input("Server>")  # 入力待機(サーバー側)
        data = data.encode('utf-8')
        soc.send(data)              # ソケットにデータを送信

        if data == "/end":             # /endが押されたら終了
            soc.close()
            break


main()
