import socket

def read_json_file(json_file_path: str)->list:
    data = json.load(open(
        json_file_path, 'r'))
    return data

def main():
    config_path = "./config.json"
    data = read_json_file(config_path)
    ip_addr = data["server_ip"]
    port_num = data["port"]
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((ip_addr, port_num))

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
