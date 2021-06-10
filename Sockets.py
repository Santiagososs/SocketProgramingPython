import socket
import sys
import threading

HOST = 'localhost'
PORT = 8888

def conn_em_espera(conn, addr):
    print('Nova Conexão: ', addr)

def browser(server_tcp, client_tcp):
    while True:
        conn, addr = server_tcp.accept()
        reqst = conn.recv(4026)
        result = reqst.split()[1]
        result = str(result)
        result2 = result.split("'")[1]
        result2 = str(result2)
        print("aaaaaaaaaaaaaa",result2)
        resultfinal = result2.split("/")[1]
        retorn_result = str(resultfinal)
        retorn_result = retorn_result.strip("")
        seila = ('GET / HTTP/1.1\r\nHost: '+retorn_result+'\r\n\r\n') #mudar seila quando desocobrir o nome certo
        client_tcp.sendall(seila.encode())
        #print(reqst)
        pag = str(client_tcp.recv(4096), 'utf-8')

        conn.send(pag.encode())
        #print(pag)
        print("Valor Informado: ", retorn_result)
        thread = threading.Thread(target=conn_em_espera, args=(conn,addr))
        thread.start()
        print(f"Conexão Recebida: ", {threading.active_count() - 1})
        print("\n")


def main():
    server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_tcp.bind((HOST, PORT))
    server_tcp.listen(3)
    print(f"Escutando: {HOST} \n Porta: {PORT}")
    client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_tcp.connect(("www.example.org", 80))
    browser(server_tcp, client_tcp)
    

if __name__ == "__main__":
    main()

