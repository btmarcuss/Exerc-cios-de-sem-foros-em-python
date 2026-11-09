import multiprocessing
import time
import random

DISTANCIA_MAXIMA = 50
PULO_MAXIMO = 5

def sapo(id_sapo, podio_lock, posicao_chegada):
    distancia_percorrida = 0
    
    while distancia_percorrida < DISTANCIA_MAXIMA:
        salto = random.randint(0, PULO_MAXIMO)
        distancia_percorrida += salto
        
        if distancia_percorrida > DISTANCIA_MAXIMA:
            distancia_percorrida = DISTANCIA_MAXIMA
            
        print(f"Sapo {id_sapo} pulou {salto} cm | Percurso total: {distancia_percorrida}/{DISTANCIA_MAXIMA} cm")
        time.sleep(random.uniform(0.1, 0.3))
    
    with podio_lock:
        posicao_chegada.value += 1
        posicao_final = posicao_chegada.value
        
    print(f"\n CHEGADA! O Sapo {id_sapo} cruzou a linha de chegada em {posicao_final}º LUGAR!\n")

if __name__ == '__main__':
    podio_lock = multiprocessing.Lock()
    posicao_chegada = multiprocessing.Value('i', 0)
    processos = []

    print(f"=== INÍCIO DA CORRIDA DE SAPOS (Meta: {DISTANCIA_MAXIMA} cm) ===\n")

    for i in range(1, 6):
        p = multiprocessing.Process(target=sapo, args=(i, podio_lock, posicao_chegada))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()

    print("=== FIM DA CORRIDA DE SAPOS ===")