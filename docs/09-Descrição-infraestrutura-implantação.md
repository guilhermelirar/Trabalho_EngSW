| **Backlog Manager** | **Responsável** |
| :------------------------------- | :-------------- |
| **Caderno de Arquitetura**         | Guilherme Lira Ribeiro - [231013538] |

# BACKLOG MANAGER

# Descrição da Infraestrutura de Implantação

## 1. Software Necessário a Implantação do Sistema de Software

Para a execução adequada do sistema em ambiente de desenvolvimento ou produção, são necessários os seguintes softwares e ambientes:

- **Sistema Operacional:** Compatível com distribuições Linux (ex: Arch Linux, Ubuntu), macOS ou Windows.
- **Ambiente de Execução:** Python (versão 3.10 ou superior).
- **Gerenciador de Dependências:** `pip` e módulo `venv` para isolamento do ambiente virtual.
- **Banco de Dados:** SQLite3 (nativo do Python para ambiente local/desenvolvimento) com suporte a migração para SGBDs relacionais em produção (como PostgreSQL ou MySQL via URI de conexão).
- **Navegador Web (Client-side):** Qualquer navegador moderno atualizado (Google Chrome, Mozilla Firefox, Chromium, Edge) com suporte a HTML5, CSS3 e JavaScript.

Os passos para a execução da aplicação no lado do servidor são descritos a seguir:

### 1. Criar e ativar um ambiente virtual:

```sh
# Linux
python -m venv venv
source venv/bin/activate
```

### 2. Instalar dependências:

Instalar as dependências listadas no arquivo `requirements.txt` no ambiente virtual
com o pip.

```sh
pip install -r requirements.txt
```

### 3. Rodar testes automatizados (`pytest`):

```sh
pytest
```

### 4. Subir a aplicação Flask:

```sh
flask --app app/app run
```

## 2. Hardware Necessário

Devido à arquitetura em camadas leve construída em Flask com persistência SQLite, a aplicação apresenta baixos requisitos de infraestrutura:

- **Processador (CPU):** 1 vCPU / 1 GHz ou superior (arquitetura x86_64 ou ARM).
- **Memória RAM:** Mínimo de 512 MB (1 GB recomendado para execução estável do servidor web de desenvolvimento).
- **Armazenamento:** Mínimo de 500 MB de espaço livre em disco (necessário para o código-fonte, ambiente virtual `venv` e arquivo de banco de dados SQLite).
- **Rede:** Interface de rede local com suporte à pilha TCP/IP e abertura da porta de comunicação HTTP (porta padrão `5000` em desenvolvimento).

## 3. Serviços Necessários

Para a execução, validação e acesso ao sistema **Backlog Manager**, são necessários os seguintes serviços de software e infraestrutura local:

### 3.1. Serviço de Servidor de Aplicação Web (Flask WSGI)

- Serviço embutido do framework Flask responsável por subir o servidor web local em ambiente de desenvolvimento, recebendo requisições HTTP e escutando na porta `5000`.

### 3.2. Serviço de Persistência e Acesso ao Banco de Dados (SQLite)

- Serviço de entrada e saída (E/S) em sistema de arquivos operado nativamente pelo Python via `Flask-SQLAlchemy`, responsável por garantir a consistência das transações relacionais diretamente no arquivo de banco de dados SQLite local.

### 3.3. Serviço de Testes Automatizados (Pytest)

- Framework e serviço de testes responsável pela execução da suíte de testes unitários e de integração (`pytest`), garantindo a validação contínua das regras de negócio e rotas da aplicação.

### 3.4. Serviço de Acesso Local e Interface HTTP

- Serviço de loopback e roteamento local (`localhost` / `127.0.0.1`) para renderização das páginas da interface web no navegador através das rotas:
  - **Ponto de Entrada de Autenticação:** `http://127.0.0.1:5000/login`
  - **Ponto de Entrada de Registro:** `http://127.0.0.1:5000/register`

### 3.5. Observação sobre o Escopo de Implantação (Protótipo)

O presente documento e o repositório do projeto descrevem a infraestrutura voltada ao **protótipo acadêmico funcional** do sistema Backlog Manager. Por essa razão:

- **Ambiente de Execução:** Utiliza-se o servidor de desenvolvimento nativo do Flask (`flask run`) e a interface de rede local (`localhost:5000`), dispensando para o escopo desta entrega a configuração de servidores WSGI de produção (como Gunicorn/uWSGI) ou servidores de proxy reverso (como Nginx/Apache).
- **Persistência de Dados:** Adota-se o banco relacional embarcado **SQLite3**, que opera diretamente sobre o sistema de arquivos local sem a necessidade de um serviço daemon de SGBD como PostgreSQL ou MySQL.
- **Serviços de Rede:** Não há dependência de serviços externos de DNS, roteamento avançado ou certificados SSL/TLS no ambiente local.

Em um cenário de implantação em ambiente corporativo/produção real, a arquitetura estipulada prevê a migração transparente da URI do SQLAlchemy para um SGBD relacional dedicado e a orquestração do Flask sob Gunicorn/Nginx com terminação HTTPS.
