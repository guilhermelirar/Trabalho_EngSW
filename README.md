# Trabalho_EngSW

Trabalho Prático de Engenharia de Software (UnB 2026/2), que consiste em
artefatos derivados do processo de desenvolvimetno de um software de suporte
a gestão de requisitos por meio de histórias de usuário.

---

## Conteúdo do repositório

- `/docs`: arquivos Markdown (`.md`) para documentos de: 
  - descrição do processo de gerenciamento (Kanban) (`01-gerenciamento.md`)
  - visão de escopo (`02-visao.md`)
  - especificação de requisitos não funcionais (`03-reqs-nao-funcionais.md`)
  - especificação de requisitos funcionais por casos de uso 
    (`04-historias-de-usuario.md`)
  - descrição de arquitetura de software (`05-caderno-de-arquitetura.md`)
  - projeto de interface do usuário (`06-proj-de-interface.md`)
  - projeto físico de banco de dados (`07-proj-banco-de-dados.md`)
  - descrição da infraestrutura de implantação (`08-infraestutura.md`)
  - (+ diagramas UML ou diversos)

- `/app`: estrutura da aplicação Flask
  - `models/`: representação dos modelos do banco de dados em classes
  - `services/`: módulos da lógica de negócios da aplicação
  - `routes/`: lógica de comunicação (HTTP request/response) e recebimento de dados do usuário
  - `templates/`: arquivos .html e templates Jinja2 para páginas da aplicação (interface de usuário)
  - `static/`: arquivos estáticos (imagens e css que podem ser usadas no site)

- `/tests`: diretório dos testes automatizados (`pytest`) e arquivo de configuração de testes `conftest.py` 
 
- `requirements.txt`: arquivo com dependências necessárias para executar a aplicação

--- 

## Como executar a aplicação

**Requer:** Python 3.1+

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

Após subir a aplicação, a rota de login é `/login`, e de registro de usuário é `/register` 
