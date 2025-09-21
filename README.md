# Estudos de APIs em Python

## Descrição
Este repositório contém estudos de consumo de APIs em Python, com foco em aprendizado e demonstração prática. Durante este estudo, explorei a biblioteca **Requests** para fazer requisições HTTP, manipular respostas e trabalhar com dados de APIs externas.

Além disso, organizei **mini projetos** que mostram diferentes formas de interação com APIs e o uso de **Pandas** para manipulação de dados e **Streamlit** para visualização interativa.

## Projeto Principal: Frequência de Nomes - IBGE
Este projeto utiliza a **API do IBGE** para obter a frequência histórica de um nome no Brasil por década.

**Funcionalidades:**
- Recebe um nome digitado pelo usuário
- Consulta a API do IBGE usando Requests
- Organiza os dados com Pandas
- Exibe tabela e gráfico interativo usando Streamlit

**Exemplo de uso:**
- Digitar "Maria" no app
- Visualizar quantas pessoas com esse nome nasceram em cada década

## Outros exemplos
Além do projeto principal, este repositório contém **scripts menores** que demonstram o consumo de outras APIs públicas, incluindo:  
- Obtenção de dados em JSON  
- Processamento de dados com Pandas  
- Visualização simples em console ou com gráficos  

---

## Observações

- Este repositório é voltado para estudo e prática; use os scripts com responsabilidade.

- Alguns scripts podem exigir conexão com a internet e permissões do sistema.

- Explore os outros arquivos para ver diferentes exemplos de consumo de APIs.

## Como usar
1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repo.git

Instale as dependências:

pip install requests pandas streamlit


Execute o projeto principal:

streamlit run nome_do_arquivo_principal.py

