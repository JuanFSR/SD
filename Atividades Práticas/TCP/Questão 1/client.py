import socket 
import time

ip = "127.0.0.1"
port = 7000

addr = (ip, port) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.connect(addr)

def main():
    while True:
        comando = input("comando: ")
        entrada = ''

        # formatacao do primeiro comando para maiusculo
        if len(comando.split()) > 1:
            for index, comandos in enumerate(comando.split()):
                if index == 0:
                    entrada = comandos.upper()
                else:
                    entrada = entrada + ' ' + comandos
        else:
            entrada = comando.upper()

        # Envia mensagem
        client_socket.send(entrada.encode("utf-8"))
        
        # Lista os comandos
        if(entrada == "HELP"):
            comandos = client_socket.recv(1024).decode('utf-8')
            for comandos in comandos.split(';'):
                print(comandos)

        # Envia a mensagem e fecha a conexão
        if(entrada == "EXIT"):
            client_socket.close()
            break

        # Retorna o horario do sistema
        if(entrada == "TIME"):
            print(client_socket.recv(1024).decode("utf-8"))
        
        # Retorna a data do sistema
        if(entrada == "DATE"):
            print(client_socket.recv(1024).decode('utf-8'))

        # Recebe os arquivos da pasta padrão
        if(entrada == "FILES"):
            files = client_socket.recv(1024).decode('utf-8')
            print('Numero de arquivos encontrados: ', files)

            while 1:
                arquivoNomes = client_socket.recv(1024).decode('utf-8')
                if(arquivoNomes != "Alisson"):
                    print('   -', arquivoNomes)

        # Faz o download de um arquivo
        if((entrada.split())[0] == 'DOWN'):
            bytes = client_socket.recv(1024).decode('utf-8')  
            print('Total de bytes: ', bytes)
            
            # Verifica se foi encontrado um arquivo
            if int(bytes) > 0:
                nomeArquivo = entrada.split()[1]
                arquivo = b''

                # Recebo os bytes do servidor
                for i in range(int(bytes)):
                    fileBytes = client_socket.recv(1024)
                    arquivo += fileBytes

                # Salvo em um novo arquivo
                with open('./client_files/' + nomeArquivo, 'wb') as file:
                    file.write(arquivo)

            elif int(bytes) < 1:
                print('Arquivo não foi encontrado')
        
main()