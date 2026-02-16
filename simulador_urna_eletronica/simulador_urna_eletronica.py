import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_candidatos(candidatos):
    print("\n--- CANDIDATOS DISPONÍVEIS ---")
    for numero, nome in candidatos.items():
        print(f"[{numero}] - {nome}")
    print("[0] - Voto em Branco")
    print("-" * 30)

def simulador_urna():
    # Estrutura de dados: Número -> Nome
    candidatos = {
        "15": "Isaac Newton",
        "22": "Leonhard Euler",
        "35": "Ada Lovelace",
        "44": "Alan Turing"
    }
    
    # Dicionário de contagem: Iniciando todos com zero
    votos = {numero: 0 for numero in candidatos.keys()}
    votos["Branco"] = 0
    votos["Nulo"] = 0

    while True:
        limpar_tela()
        print("======= 🗳️ URNA ELETRÔNICA EDUCACIONAL =======")
        exibir_candidatos(candidatos)
        
        voto = input("Digite o número do candidato (ou 'FIM' para encerrar): ").strip().upper()

        if voto == 'FIM':
            break
        
        if voto == '0':
            votos["Branco"] += 1
            print("\n✅ Voto em BRANCO registrado!")
        elif voto in candidatos:
            votos[voto] += 1
            print(f"\n✅ Voto para {candidatos[voto]} registrado!")
        else:
            confirmar_nulo = input("⚠️ Número inválido. Confirmar como NULO? (s/n): ").lower()
            if confirmar_nulo == 's':
                votos["Nulo"] += 1
                print("\n✅ Voto NULO registrado!")
            else:
                continue
        
        input("\nPressione Enter para o próximo eleitor...")

    # Processamento dos Resultados
    total_votos = sum(votos.values())
    
    limpar_tela()
    print("======= 📊 RESULTADO DA APURAÇÃO =======")
    print(f"Total de Votos: {total_votos}\n")

    # Ordenar candidatos por número de votos (do maior para o menor)
    ranking = sorted(votos.items(), key=lambda x: x[1], reverse=True)

    for chave, qtd in ranking:
        percentual = (qtd / total_votos * 100) if total_votos > 0 else 0
        nome_exibicao = candidatos.get(chave, chave) # Busca o nome ou mantém 'Branco/Nulo'
        print(f"{nome_exibicao:<15}: {qtd} votos ({percentual:.1f}%)")
    
    print("=========================================")

def gerar_boletim_urna(ranking, total_votos):
    """Gera um arquivo TXT com o resultado oficial da apuração."""
    with open("boletim_urna.txt", "w", encoding="utf-8") as f:
        f.write("=== TRIBUNAL ACADÊMICO DE MATEMÁTICA ===\n")
        f.write("--- RELATÓRIO OFICIAL DE APURAÇÃO ---\n\n")
        f.write(f"Total de Votos Computados: {total_votos}\n")
        f.write("-" * 40 + "\n")
        for nome, qtd in ranking:
            perc = (qtd / total_votos * 100) if total_votos > 0 else 0
            f.write(f"{nome:<20}: {qtd} votos ({perc:.1f}%)\n")
        f.write("-" * 40 + "\n")
        f.write("Fim da Apuração Oficial.")
    print("\n💾 Boletim de Urna gerado com sucesso: 'boletim_urna.txt'")
    
if __name__ == "__main__":
    simulador_urna()