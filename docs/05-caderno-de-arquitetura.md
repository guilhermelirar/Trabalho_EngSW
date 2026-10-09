| Backlog Manager            |                 |
| :------------------------- | :-------------- |
| **Caderno de Arquitetura** | Data: 8/10/2026 |

# Backlog Manager

# Caderno de Arquitetura

## 1. Propósito

Este documento descreve a filosofia, decisões, restrições, justificativas
elementos significativos e outros aspectos relevantes para o design e implementação
do sistema.

## 2. Objetivos e filosofia da arquitetura

A arquitetura deverá fornecer suporte ao desenvolvimento de um **sistema para gerenciamento de requisitos baseado em histórias de usuário**.

O sistema será desenvolvido como uma **aplicação web**, disponibilizando uma interface gráfica (site) para acesso às suas funcionalidades.

A arquitetura deverá permitir o desenvolvimento das funcionalidades relacionadas ao gerenciamento de:

- Projetos;
- Product Backlogs;
- Sprint Backlogs;
- Histórias de usuário;
- Épicos;
- Critérios de aceitação;
- Story Points;
- MoSCoW;
- RICE score.

A divisão inicial do trabalho considera responsabilidades específicas para arquitetura/backend, banco de dados e interface/frontend, mantendo a possibilidade de colaboração entre os integrantes.

<!-- Questões que conduzirão arq. como preocupações de deployment, performance,
     robustez para manutenção; objetivos (goals) que a arquitetura precisa ter
     na estrutura e comportamento, e se deve funcionar bem em condições não usuais -->

## 3. Suposições e dependências

As seguintes definições foram estabelecidas inicialmente pelo grupo:

- O sistema será desenvolvido como um **site**.
- O sistema utilizará uma **interface gráfica**.
- O usuário deverá criar uma conta para acessar os serviços disponibilizados.
- O usuário deverá se autenticar para acessar os serviços.
- As funcionalidades do sistema serão organizadas a partir das histórias de usuário definidas pelo grupo.
- O sistema deverá trabalhar com projetos, Product Backlogs, Sprint Backlogs, histórias de usuário, épicos, critérios de aceitação, Story Points, MoSCoW e RICE.
- O projeto contará com integração entre a interface, o backend e o banco de dados.
- Usuários autenticados não serão separados por tipo, com todos tendo acesso igual as funcionalidades do sistema

Para cumprir os objetivos, será adotada a linguagem de programação Python 3, bem como frameworks para aplicação web
por ela suportados, nomeadamente o Flask para o desenvolvimento da aplicação (backend), por ser uma framework que se
destaca pela leveza, simplicidade e alto poder de customização. Além disso possui vasta documentação e é adotado por
grandes empresas. Este framework é ideal para protótipos e microsserviços, e também possui uma série de extensões como
suporte a motores de template HTML (Jinja2), ferramentas de utilidade e segurança, como Werkzeug, e de banco de dados,
como o Flask-SQLAlchemy. Essas extensões também são consideradas dependências desta arquitetura.

<!-- premissas sobre o comportamento, consistencia de dados, performance;
    limites antecipados, experiencia da equipe -->
<!-- sistema externos como APIs, bancos de dados compartilhados (nao aplicavel);
    blocos de software ou bibliotecas; -->

## 4. Requisitos significativos para arquitetura

Os principais requisitos funcionais que possuem impacto sobre a arquitetura são:

- Disponibilizar uma interface gráfica para utilização do sistema.
- Permitir criação de conta.
- Permitir autenticação do usuário.
- Permitir acesso aos serviços após autenticação.
- Permitir gerenciamento de projetos.
- Permitir gerenciamento de Product Backlogs.
- Restringir cada projeto a no máximo um Product Backlog.
- Permitir gerenciamento de vários Sprint Backlogs por projeto.
- Permitir movimentação de histórias entre backlogs.
- Permitir gerenciamento de histórias de usuário.
- Associar inicialmente uma história de usuário a um Product Backlog.
- Permitir gerenciamento e vínculo de épicos e histórias de usuário.
- Permitir gerenciamento de critérios de aceitação.
- Permitir atribuição de Story Points.
- Permitir classificação por MoSCoW.
- Permitir utilização e cálculo de RICE.

Esses requisitos deverão ser considerados na definição da estrutura do sistema, da persistência dos dados e da comunicação entre as partes da aplicação.

<!-- referencia ou lik para requisitos que devem ser implementados para
    realizar a arquitetura -->

## 5. Decisões, restrições e justificativas

### 5.1 Decisões

- O produto será desenvolvido como um **site**.
- Será utilizada uma **interface gráfica**.
- O sistema terá criação de conta e autenticação.
- As funcionalidades serão organizadas de acordo com as histórias de usuário definidas pelo grupo.
- O desenvolvimento terá divisão de responsabilidades entre arquitetura/backend, banco de dados e interface/frontend.
- A arquitetura de backend será dividida em três camadas: rotas, serviços e modelos, com cada camada podendo ter módulos (ex: autenticação, projetos, história de usuário, épicos)

### 5.2 Restrições

- Cada projeto poderá possuir no máximo um Product Backlog.
- Um projeto poderá possuir vários Sprint Backlogs.
- Uma história de usuário deverá ser inicialmente associada a um Product Backlog.
- Os Story Points deverão utilizar somente os valores definidos no projeto.
- Os critérios de MoSCoW deverão utilizar somente os valores definidos no projeto.
- Os critérios de RICE deverão seguir os valores definidos para Reach, Impact, Confidence e Effort.
- O cálculo do RICE deverá utilizar a fórmula definida no projeto.

### 5.3 Justificativas

- **Desenvolvimento de aplicação web (site)**: justificado pela facilidade
  de acesso dos usuários a um navegador, sem necessidade de instalação de
  software local, além de simplificar a implantação e manutenção do sistema por meio de um servidor centralizado.
- **Uso do Flask:** por ser leve, flexível e ter baixa curva de aprendizado, além de documentação extensa, é ideal para a equipe de desenvolvedores e permite estruturar a arquitetura de forma modular sem complexidade desnecessária de frameworks mais pesados.
- **Backend em camadas**: a modularização favorece a separação de responsabilidades e facilita a manutenção e teste do sistema. Também desacopla a lógica de acesso (interfaces HTML) da lógica de negócios e banco de dados.

<!-- decisoes a respeito de abordagens de arquiteutra e as restrições colocadas;
     decisao/constraint e justificativa em bullet points; pode ter lista de dos
     e donts-->

## 6. Mecanismos de arquitetura

Com base nas funcionalidades definidas, deverão ser considerados mecanismos relacionados a:

- **Autenticação do usuário**: senhas devem ser comparadas e armazenadas por meio de hash, utilizando a ferramenta werkzeug.security para tal, a fim de garantir a segurança de informações críticas.
- **Persistência das informações**: será utilizada uma abstração do banco de dados relacional com a extensão Flask-SQLAlchemy (ORM) e execução via SQLite na fase de desenvolvimento.
- **Tratamento de erros e exceções:** camada centralizada de exceções personalizadas (`ServiceError`) para captura global no servidor e tornar implementação das rotas mais simples (focadas no caso de sucesso). Usará mecanismo nativo do Flask para tal (`@app.errorhandler`)
- **Comunicação entre a interface e o backend**;
- **Gerenciamento dos dados dos projetos**;
- **Gerenciamento dos diferentes tipos de backlog**;
- **Gerenciamento das histórias de usuário**;
- **Cálculo da pontuação RICE**.

## 7. Abstrações relativas à arquitetura

As principais abstrações identificadas a partir das funcionalidades definidas são:

- **Usuário**;
- **Projeto**;
- **Product Backlog**;
- **Sprint Backlog**;
- **História de Usuário**;
- **Épico**;
- **Critério de Aceitação**;
- **Story Points**;
- **MoSCoW**;
- **RICE**.

Essas abstrações correspondem aos principais elementos funcionais identificados na reunião e deverão ser consideradas durante a definição do modelo de dados e da implementação do sistema.

## 8. Arquitetura segundo perspectivas

### Perspectiva funcional

O sistema será organizado em torno do gerenciamento de requisitos por meio de histórias de usuário, incluindo projetos, backlogs, histórias, épicos, critérios de aceitação e mecanismos de estimativa e priorização.

### Perspectiva de interface

O sistema será disponibilizado como um site com uma interface gráfica.

### Perspectiva de dados

O sistema deverá armazenar as informações necessárias ao gerenciamento dos projetos e dos elementos relacionados às histórias de usuário.

A estrutura lógica e física dos dados é mapeada declarativamente via
classes Python (`models/`) gerenciadas pelo SQLAlchemy, utilizando o banco
SQLite em ambiente de desenvolvimento local com suporte a migração para
SGBD relacional (como MySQL/PostgreSQL) em produção.

### Perspectiva de backend

O backend será responsável pela implementação das regras de negócio e dos serviços necessários para o funcionamento do sistema. Isso será feito por
meio de três camadas:

- **Camada de Apresentação (`routes/`):** responsável por lidar com requisições HTTP, extrair dados de requisição para chamar funções específicas da camada anterior, e fornecer dados ou recursos de resposta, como renderização de páginas HTML.
- **Camada de Lógica de Negócios (`services/`)**: responsável por concentrar e executar as regras de negócio da aplicação (como o cálculo do RICE score, validações de formato e tratamento de exceções de domínio). Recebe os dados já extraídos da camada de apresentação, processa as operações necessárias e orquestra a persistência de dados com a camada de modelos, garantindo o isolamento da regra de negócio independente da interface.
- **Camada de Acesso a Dados (`models/`)** responsável por fornecer classes equivalentes às entidades e domínios dos sistema, que persistem em banco de dados. Permite que a camada superior trabalhe com princípios de orientação a objetos, abstraídas as peculiaridades do banco de dados relacional configurado com o SQLAlchemy.

### Perspectiva de integração

Deverá existir integração entre a interface, o backend e o banco de dados para permitir o funcionamento das funcionalidades do sistema. O SQLAlchemy permite trabalhar com tabelas e registros no banco de dados como se fossem objetos, segundo a abordagem de Mapeamento Objeto-Relacional (ORM). Como exposto na perspectiva de backend, este acesso é feito na camada de lógica de negócios usando as classes providas pela camada de acesso a dados.

## 9. Impacto de frameworks na arquitetura

### 9.1. Impacto do Framework Flask

Por ser um micro-framework não opinativo, o Flask não impõe arquitetura de pastas padrão. O impacto direto foi a necessidade de a equipe definir e disciplinar a separação em camadas (`routes`, `services`. `models`). Além disso, a camada de apresentação fica acoplada a estrutura do Flask por meio de objetos globais como `request`, `g`, e `session`.

### 9.2. Impacto da opção de Object-Relational Mapping com SQLAlchemy

Ao ultilizar SQLAlchemy, foi assumido o compromisso da inversão
no fluxo da criação de tabelas, que passam a ter sua estrutura
definida por meio de objetos Python. Para isso, é necessário escolher
os tipos de dados do SQLAlchemy correspondentes aos tipos de tabela no SQL. Isso isola o backend de códigos SQL específicos, permitindo
portabilidade de independência de sistema de gerenciamento de banco de dados.

A utilização do ORM SQLAlchemy exige também atenção na estratégia de
carregamento das relações (eager vs. lazy loading). O impacto
arquitetural é a necessidade de otimizar consultas específicas na camada
de Services para evitar o problema de múltiplas consultas redundantes ao
banco na renderização de painéis complexos e listagens do backlog.
Dessa forma, não elimina a possibilidade de ser necessário escrever queries SQL personalizadas, para atender a requisitos de performance.
