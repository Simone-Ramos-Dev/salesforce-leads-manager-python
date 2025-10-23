# 🚀 Gerenciador de Leads com Python e Salesforce API

Este projeto demonstra a integração entre **Python** e a **Salesforce REST API** para gerenciar registros de Leads de forma programática. É um portfólio prático para quem busca aplicar conhecimentos em Python para automatização e manipulação de dados em um CRM líder de mercado.

## 🎯 Objetivo do Projeto

Criar um script Python capaz de se autenticar no Salesforce e realizar as operações básicas de CRUD (Create, Read, Update e Delete - focado em Create e Read no exemplo) no objeto `Lead`.

## ✨ Funcionalidades

O script atual demonstra:

1.  **Conexão Segura:** Autenticação no Salesforce utilizando a biblioteca `simple-salesforce` (via Username/Password/Token de Segurança ou Connected App).
2.  **Criação de Leads (Create):** Inserção de novos Leads no Salesforce com dados gerados dinamicamente.
3.  **Consulta de Leads (Read):** Execução de consultas SOQL para buscar e exibir os Leads mais recentes da organização.
4.  **Gerenciamento de Erros:** Tratamento de exceções da API para falhas de conexão ou validação de dados.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **CRM:** Salesforce Developer Edition (ou Sandbox/Produção)
* **Biblioteca Principal:** `simple-salesforce` (Cliente REST API para Python)
* **Configuração:** `python-dotenv` (Para gerenciar credenciais de forma segura)

## ⚙️ Setup do Ambiente

### Pré-requisitos no Salesforce

Para se conectar à API, você precisará:

1.  Uma **Developer Org** do Salesforce (gratuita).
2.  Um **Usuário**, **Senha** e **Token de Segurança** válidos. *(Recomenda-se resetar o Token em `Configuração` -> `Redefinir meu token de segurança`).*
3.  **Permissão "API Enabled"** ativa no Perfil do usuário.

### Configuração Local

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```

2.  **Crie e Ative o Ambiente Virtual:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    .\.venv\Scripts\Activate.ps1  # Windows PowerShell
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Credenciais (CRUCIAL):**
    Crie um arquivo chamado **`.env`** na raiz do projeto (este arquivo é ignorado pelo Git por segurança) e preencha com suas credenciais:

    ```env
    # .env file
    SF_USERNAME=seu.email.salesforce@exemplo.com
    SF_PASSWORD=sua_senha
    SF_SECURITY_TOKEN=seu_token_de_seguranca_aqui
    SF_IS_SANDBOX=False 
    ```

## 🚀 Como Executar o Projeto

Com o ambiente virtual ativado, basta executar o script principal:

```bash
python main.py
