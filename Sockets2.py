import socket
import sys
import threading

HOST = 'localhost'
PORT = 8888

def conn_em_espera(conn, addr):
    print('Nova Conexão: ', addr)

def main():
    server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_tcp.bind((HOST, PORT))
    server_tcp.listen(5)
    print(f"Escutando: {HOST} \nPorta: {PORT}")
    
    client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        conn, addr = server_tcp.accept()
        reqst = conn.recv(500000)  
        favicon = reqst.split()
        testepau = reqst.split()[0:2]
        testepau = str(testepau)
        testepau1 = testepau.split("/")
        varifx = testepau1[1]   
        testepau2 = testepau1[2:]
        result = reqst.split()[1]
        result = str(result)
        result2 = result.split("'")[1]
        result2 = str(result2)
        resultfinal = result2.split("/")[1]
        retorn_result = str(resultfinal)
        retorn_result = retorn_result.strip("")

        if(resultfinal == "favicon.ico"):
            for cont in favicon:
                if len(cont) > 5:
                    if((cont[3:]).decode() == 'p://localhost:7777/www.example.org'):
                        valorseila = (cont[3:]).decode()
                        splitseila = valorseila.split('/')
                        eunaosei = splitseila[3]
                        stringdominio = eunaosei
                        client_tcp.connect((stringdominio, 80)) 
        else:
            try:
                client_tcp.connect((retorn_result, 80))     
            except:
                pass
        tamanho = (len(testepau2))
        print(tamanho)
        
        if tamanho != 0: 
            for cont in range (len(testepau2)-1):
                varif = testepau2[cont] + "/" + testepau2[cont+1] 
                varif = str(varif)
                varif2 = varif.split("'")[0]
                seila = ('GET /'+varif2+' HTTP/1.1\r\nHost:'+retorn_result+'\r\n\r\n')
                #client_tcp.send(seila.encode())
        else:
            
            seila = ('GET / HTTP/1.1\r\nHost:'+retorn_result+'\r\n\r\n')
            #client_tcp.send(seila.encode())
            
        #send para o servidor
        client_tcp.sendall(seila.encode())
        pag = client_tcp.recv(500000)
        #print(pag)

        conn.sendall(pag)
        print("Valor Informado: ", retorn_result)
        thread = threading.Thread(target=conn_em_espera, args=(conn,addr))
        thread.start()
        print(f"Conexão Recebida: ", {threading.active_count() - 1})
        #print("\n")
        #conn.close()
        #client_tcp.close()
        

if __name__ == "__main__":
    main()