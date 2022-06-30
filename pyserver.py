import socket
import threading
# socket通信できるかを確認する
# binder関数はサーバーからacceptしたら生成されるsocketインスタンスを通ってclientからデータを受信するとecho形で再送信するメソッド


def binder(client_socket, addr):
    # コネクションになれば接続アドレスを出力する。
    print('Connected by', addr)
    try:
        # 接続状況でクライアントからデータ受信を待つ
        while True:
            data = client_socket.recv(4096)  # 一度に受け取るデータのサイズを指定
            # print("received data:",data)

            msg = data.decode()
            # 受信されたメッセージを出力
            if (msg != ""):  # 空欄のmsgでターミナルが埋まり、見ずらい為
                print('Received from', addr, msg)
            # 受信されたメッセージの前に「echo:」という文字を付ける
            msg = "echo :" + msg
            # バイナリタイプに変換
            data = msg.encode('utf-8')
            # データ転送
            client_socket.sendall(data)
    except:
        print("except : ", addr)
    finally:
        client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ソケットを生成

# ソケットレベルとデータタイプを設定
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# ポートはPC内で空いているポートを使う
server_socket.bind(('172.21.65.74', 12345))

# server設定が完了すればlisten開始
server_socket.listen(5)

try:
    # クライアントからの接続待ち
    while True:
        client_socket, addr = server_socket.accept()
        th = threading.Thread(target=binder, args=(client_socket, addr))
        th.start()
except:
    print("server")
finally:
    server_socket.close()
