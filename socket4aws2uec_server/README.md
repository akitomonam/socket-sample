# 疑似ソケット通信
外部からプライベートネットワーク（大学など）へソケット接続し通信を行うプログラムです。
## 実行方法(ローカルで実験)
クライアント側(フロントエンド)
```
nohup python3 server2server.py & > nohup_client.log &
```
サーバー側(バックエンド)
```
nohup python3 client_try_connect.py & > nohup_server.log &
```
クライアント側(フロントエンド)
```
python3 client.py
```
