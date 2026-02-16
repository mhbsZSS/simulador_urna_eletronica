# 🗳️ Simulador de Urna Eletrônica Educacional

Este projeto simula o funcionamento de uma urna eletrônica para votações escolares ou acadêmicas. Desenvolvido em **Python**, o sistema foca em integridade de dados e clareza na apuração.

## 🚀 Funcionalidades
- **Interface de Votação:** Menu interativo via CLI que simula o fluxo de uma urna real.
- **Gestão de Candidatos:** Utiliza estruturas de dicionário (`Key-Value`) para mapear números e nomes.
- **Tratamento de Votos:** Suporte para votos nominais, brancos e nulos (com confirmação).
- **Relatório Estatístico:** Apuração em tempo real com cálculo de porcentagem sobre o total de votos.
- **Boletim de Urna:** Exportação automática dos resultados para um arquivo `.txt`.

## 🧠 Conceitos Aplicados
- **Dicionários (Maps):** Para armazenamento de contagem de votos e nomes de candidatos.
- **Tratamento de Strings:** Normalização de entradas (letras maiúsculas/minúsculas) e remoção de espaços.
- **Ordenação de Dados:** Uso de `sorted()` com funções `lambda` para ranqueamento dos resultados.

## 📊 Como Testar
1. Execute o script `simulador_urna.py`.
2. Digite o número do candidato (ex: 15, 22).
3. Para encerrar a votação e ver o resultado, digite `FIM`.