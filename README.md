# 🌌 Alura Space

> Uma Galeria de Fotos Espaciais Desenvolvida com **Python e Django**

## 📝 Descrição do Projeto

O **Alura Space** é uma aplicação web full-stack desenvolvida em **Python** utilizando o framework **Django**. O projeto simula uma galeria de imagens inspiradas no espaço, com foco no aprendizado e implementação de uma arquitetura sólida de backend para gerenciamento de mídia e conteúdo.

Este projeto foi construído como parte do curso Formação: Django Rest Framework.

## ✨ Funcionalidades Principais

  * **Galeria de Fotos:** Exibição principal das imagens em um layout de fácil visualização.
  * **Sistema CRUD para Fotos:** Capacidade de Criar, Ler, Atualizar e Deletar (CRUD) imagens e seus metadados (título, descrição, categoria) através do painel de administração do Django.
  * **Filtro por Categorias:** Permite aos usuários categorizar e exibir fotos específicas (ex: Estrelas, Nebulosas, Lua).
  * **Upload de imagens:** Upload de imagens e processamento com Pillow.
  * **Login autenticado:** Criação de usuários e sistema de login/autenticação.

## 💻 Tecnologias Utilizadas

O desenvolvimento deste projeto utilizou o seguinte stack de tecnologias:

| Categoria | Tecnologia | Versão | Uso |
| :--- | :--- | :--- | :--- |
| **Framework Web** | `Django` | $5.1.6$ | Backend principal, rotas, views e templates. |
| **Linguagem** | `Python` | [Sua Versão] | Linguagem principal do projeto. |
| **Imagens** | `Pillow` | $11.1.0$ | Manipulação e processamento de imagens. |
| **Ambiente** | `python-dotenv` | $1.0.1$ | Gerenciamento seguro de variáveis de ambiente. |
| **Servidor** | `asgiref` | $3.8.1$ | Suporte para ASGI (servidores assíncronos). |

## 🚀 Como Rodar o Projeto

Para executar o projeto localmente, siga os passos abaixo.

### Pré-requisitos

Certifique-se de ter o **Python** e o **pip** instalados em sua máquina.

### 1\. Configuração do Ambiente

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/GiovannaBeathryce/alura_space.git
    ```
2.  **Acesse a Pasta do Projeto:**
    ```bash
    cd alura_space
    ```
3.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    # Cria o ambiente
    python -m venv venv
    # Ativa no Linux/macOS
    source venv/bin/activate
    # Ativa no Windows
    venv\Scripts\activate
    ```

### 2\. Instalação das Dependências

Instale todas as bibliotecas necessárias listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
# Ou, se preferir instalar manualmente
pip install Django Pillow python-dotenv
```

### 3\. Configuração do Banco de Dados

Aplique as migrações iniciais para configurar o banco de dados (SQLite, padrão do Django):

```bash
python manage.py migrate
```

### 4\. Execução do Servidor

Inicie o servidor de desenvolvimento do Django:

```bash
python manage.py runserver
```

A aplicação estará disponível em `http://localhost:8000/`

## 📌 Status do Projeto

 Em desenvolvimento

## 🤝 Contribuições

Contribuições são sempre bem-vindas\! Se você tiver sugestões de melhorias ou quiser reportar um bug, sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request*.

## 👩‍💻 Desenvolvedora

| Nome | GitHub |
| :--- | :--- |
| Giovanna Beathryce | [GiovannaBeathryce](https://www.google.com/search?q=https://github.com/GiovannaBeathryce) |
