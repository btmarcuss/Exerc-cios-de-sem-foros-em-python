import multiprocessing
import time
import random

def pessoa(id_pessoa, porta):
    distancia_total = 200
    distancia_percorrida = 0
    
    velocidade = random.uniform(4.0, 6.0)
    print(f"Pessoa {id_pessoa} iniciou a caminhada no seu corredor (Velocidade: {velocidade:.2f} m/s).")
    
    while distancia_percorrida < distancia_total:
        time.sleep(0.5)
        distancia_percorrida += velocidade * 0.5
        if distancia_percorrida > distancia_total:
            distancia_percorrida = distancia_total
            
    print(f"--> Pessoa {id_pessoa} CHEGOU à porta e aguarda na fila...")
    
    with porta:
        tempo_abrir_porta = random.uniform(1.0, 2.0)
        print(f"==> Pessoa {id_pessoa} está ABRINDO E CRUZANDO a porta (tempo estimado: {tempo_abrir_porta:.2f}s)...")
        time.sleep(tempo_abrir_porta)
        print(f"<-- Pessoa {id_pessoa} PASSOU pela porta com sucesso!\n")

if __name__ == '__main__':
    porta = multiprocessing.Semaphore(1)
    processos = []

    for i in range(1, 5):
        p = multiprocessing.Process(target=pessoa, args=(i, porta))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()

    print("Todas as 4 pessoas cruzaram a porta!")