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
    server_tcp.listen(3)
    print(f"Escutando: {HOST} \nPorta: {PORT}")
    client_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn, addr = server_tcp.accept()
    

    while True:
        reqst = conn.recv(8192)  
        testepau = reqst.split()[0:2]
        testepau = str(testepau)
        testepau1 = testepau.split("/")    
        testepau2 = testepau1[2:]
        result = reqst.split()[1]
        result = str(result)
        print("pintocubostamijo",result)
        result2 = result.split("'")[1]
        result2 = str(result2)
        print("pinguin",result2)
        resultfinal = result2.split("/")[1]
        retorn_result = str(resultfinal)
        retorn_result = retorn_result.strip("")
        print("aaaaaaaaaaaaaa",testepau2)
        try:
            client_tcp.connect((retorn_result, 80))        
        except:
            pass
        tamanho = (len(testepau2))
        print(tamanho)
        
        if tamanho != 0: 
            for cont in range (len(testepau2)-1):
                print("entrei no fi")
                varif = testepau2[cont] + "/" + testepau2[cont+1] 
                print("bbbbbbbbbbbbb",varif)
                varif = str(varif)
                varif2 = varif.split("'")[0]
                print("cccccccccccccccc",varif2)
                seila = ('GET /'+varif2+' HTTP/1.1\r\nHost:'+retorn_result+'\r\n\r\n')
                #client_tcp.send(seila.encode())
        else:
            print("entrei no ofo")
            seila = ('GET / HTTP/1.1\r\nHost:'+retorn_result+'\r\n\r\n')
            #client_tcp.send(seila.encode())
            
        #send para o servidor
        client_tcp.sendall(seila.encode())
        pag = client_tcp.recv(8192)
        #print(pag)

        conn.sendall(pag)
        print("Valor Informado: ", retorn_result)
        thread = threading.Thread(target=conn_em_espera, args=(conn,addr))
        thread.start()
        #print(f"Conexão Recebida: ", {threading.active_count() - 1})
        #print("\n")
        client_tcp.close()


if __name__ == "__main__":
    main()
