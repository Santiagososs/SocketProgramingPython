from ServerRedes import HOST
import socket
import threading

host =  'localhost'
port = 8888

def new_conn(conexao):
    print('Nova Conexão', conexao)


def main ():
    #Socket Inicial
    servidor_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_TCP.bind((host,port))
    servidor_TCP.listen(5)

    #Socket Client
    client_TCP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('[*]Aguardando Conexão[*]')
    cont = 1


    while True:
        conexao, addr = servidor_TCP.accept()
        request = conexao.recv(8192)

        #Favicon tratamento
        favicon_tratament = request.split()
        

        #URL Tratamento
        tratamento_url = request.split()
        tratamento_url_STR = str(tratamento_url)
        tratamento_url_aspas = tratamento_url_STR.split("'")[1]
        tratamento_url_aspasSTR = str(tratamento_url_aspas)
        tratamento_url_barras = tratamento_url_aspasSTR.split('/')
        tratamento_barras = tratamento_url_barras.split("/")[1]
        tratamento_final = str(tratamento_barras)
        print(tratamento_final)
        
        if (tratamento_final == "favicon.ico"):
            for i in favicon_tratament:
                if len(i) > 5:
                    if((i[3:]).decode() == "p://localhost:7777/www.example.org"):
                        valor_save =  (i[3:]).decode()
                        valor_split = valor_save.split("/")
                        valor_final = valor_split[3]
                        tratamento_final = valor_final
                        servidor_TCP.connect((tratamento_final, 80))
        else:
            try:
                servidor_TCP.connect((tratamento_final, 80))       
            except:
                    pass         


        conexao.sendall(str.encode("HTTP/1.0 200 OK\n",'iso-8859-1'))
        conexao.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
        conexao.sendall(str.encode('\r\n'))
        conexao.sendall(str.encode("Hello World"))
        new_conn(conexao)
        conexao.shutdown(1)



main()