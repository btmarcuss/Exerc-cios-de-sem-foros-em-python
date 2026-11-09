import multiprocessing
import time
import random

def carro(id_carro, sentido_carro, cruzamento, sentido_compartilhado):
    print(f"Carro {id_carro} ({sentido_carro}) chegou ao cruzamento e aguarda...")

    with cruzamento:
        sentido_bytes = sentido_carro.encode('utf-8')
        sentido_compartilhado[:len(sentido_bytes)] = sentido_bytes
        sentido_compartilhado[len(sentido_bytes):] = b'\x00' * (len(sentido_compartilhado) - len(sentido_bytes))

        sentido_atual = sentido_compartilhado.value.decode('utf-8').rstrip('\x00')
        print(f"==> Carro {id_carro} está PASSANDO pelo cruzamento no sentido: [{sentido_atual}]")
        
        time.sleep(random.uniform(1.0, 2.0))
        
        print(f"<-- Carro {id_carro} TERMINOU de atravessar e liberou o cruzamento.\n")

if __name__ == '__main__':
    cruzamento = multiprocessing.Semaphore(1)
    sentido_compartilhado = multiprocessing.Array('c', 50)

    lista_carros = [
        (1, "Norte -> Sul"),
        (2, "Leste -> Oeste"),
        (3, "Sul -> Norte"),
        (4, "Oeste -> Leste"),
        (5, "Norte -> Sul"),
    ]

    processos = []

    for id_c, sentido in lista_carros:
        p = multiprocessing.Process(
            target=carro, 
            args=(id_c, sentido, cruzamento, sentido_compartilhado)
        )
        processos.append(p)
        p.start()

    for p in processos:
        p.join()

    print("Todos os carros atravessaram com segurança!")