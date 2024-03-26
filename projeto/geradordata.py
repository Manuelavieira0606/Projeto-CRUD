import random

nomes_times = ["Time 1", "Time 2", "Time 3", "Time 4", "Time 5", "Time 6", "Time 7", "Time 8"]
cidades = ["Barretos", "Maceió", "Santos", "Orlândia", "Rio Preto", "Florianópolis", "Delfinópolis", "Piracicaba"]

times = []
jogadores = []

def gerar_idade():
    return random.randint(18, 40)

for i in range(8):
    time = {"id": i + 1, "nome": nomes_times[i], "cidade": random.choice(cidades), "pontos": 0, "jogos_jogados": 0}
    times.append(time)

for time in times:
    for j in range(11):
        jogador = {
            "id": len(jogadores) + 1,
            "idade": gerar_idade(),
            "posicao": random.choice(["Atacante", "Meio-campista", "Zagueiro"]),
            "data_nascimento": f"{random.randint(1, 28)}-{random.randint(1, 12)}-{random.randint(1983, 2005)}",
            "idTime": time["id"]
        }
        jogadores.append(jogador)

print("Times:")
for time in times:
    print(time)
print("\nJogadores:")
for jogador in jogadores:
    print(jogador)