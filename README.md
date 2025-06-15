# 🍔 Lucas na Chapa

Um sistema web simples para gerenciamento e visualização do cardápio de uma lanchonete. Este projeto foi desenvolvido para a disciplina de Programação para Engenharias.

## 📝 Descrição do Projeto

O "Lucas na Chapa" é uma aplicação web desenvolvida em Python com o framework Flask. O sistema apresenta o cardápio completo da lanchonete de forma dinâmica, carregando as informações diretamente do código-fonte e exibindo-as em uma página web amigável. O objetivo é simular o funcionamento básico de um sistema de pedidos, começando pela visualização do menu.

## ✨ Funcionalidades

* **Visualização Dinâmica do Cardápio:** O cardápio é carregado a partir de um dicionário Python e exibido na página principal, garantindo que qualquer alteração nos itens ou preços seja refletida instantaneamente na interface web.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python
* **Framework Web:** Flask
* **Frontend:** HTML, CSS

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:
* [Python 3](https://www.python.org/downloads/)
* pip (geralmente já vem com o Python)

### Instalação e Configuração

1.  **Clone o repositório** (ou baixe os arquivos para uma pasta no seu computador).

2.  **Crie um ambiente virtual (Virtual Environment):** É uma boa prática isolar as dependências do seu projeto. No terminal, dentro da pasta do projeto, execute:
    ```bash
    # Cria o ambiente virtual
    python -m venv venv
    ```

3.  **Ative o ambiente virtual:**
    * **No Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **No macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as dependências do projeto:** Com o ambiente ativado, execute o seguinte comando para instalar o Flask.
    ```bash
    pip install Flask
    ```

### Executando o Servidor

1.  Com o ambiente virtual ativado e as dependências instaladas, execute o arquivo principal para iniciar o servidor Flask:
    ```bash
    python main.py
    ```
2.  O terminal exibirá uma mensagem indicando que o servidor está rodando, algo como:
    ```
    * Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
    ```
3.  Abra seu navegador e acesse a URL: **http://127.0.0.1:5000**

## 📂 Estrutura de Pastas

A estrutura de arquivos do projeto está organizada da seguinte forma para que o Flask funcione corretamente:

```
Lucas_na_Chapa/
|
|-- main.py             # Arquivo principal que inicia a aplicação Flask.
|-- README.md           # Este arquivo com a documentação.
|-- venv/               # Pasta do ambiente virtual (gerada).
|
|-- src/
|   |-- cardapio.py     # Módulo Python que contém o dicionário do cardápio.
|
|-- templates/          # Pasta para os arquivos HTML.
|   |-- index.html      # Template da página principal.
|
|-- static/             # Pasta para arquivos estáticos (CSS, imagens, etc).
    |-- css/
    |   |-- style.css   # Folha de estilos da aplicação.
    |-- assets/
        |-- ...         # Local para logos e outras imagens.
```

## 👨‍💻 Autores

Este projeto foi desenvolvido por:

* Erik da Silveira de Freitas
* João Carlos Pais
* Lucas Fernandes Rovaris
