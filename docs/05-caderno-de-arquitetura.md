| Backlog Manager |                  |
| :--------------------------- | :--------------- |
| **Caderno de Arquitetura**   | Data: dd/mm/2026 |

#BACKLOG MANAGER

# Caderno de Arquitetura

## 1. Propósito

Este documetno descreve a filosofia, decisões, restrições, justificativas
elementos significativos e outros aspectos relevantes para o design e implementação
do sistema.

## 2. Objetivos e filosofia da arquitetura

A arquitetura deverá fornecer suporte ao desenvolvimento de um **sistema para gerenciamento de requisitos baseado em histórias de usuário**.

O sistema será desenvolvido como um **site**, disponibilizando uma interface gráfica para acesso às suas funcionalidades.

A arquitetura deverá permitir o desenvolvimento das funcionalidades relacionadas ao gerenciamento de:

* Projetos;
* Product Backlogs;
* Sprint Backlogs;
* Histórias de usuário;
* Épicos;
* Critérios de aceitação;
* Story Points;
* MoSCoW;
* RICE.

A divisão inicial do trabalho considera responsabilidades específicas para arquitetura/backend, banco de dados e interface/frontend, mantendo a possibilidade de colaboração entre os integrantes.

<!-- Questões que conduzirão arq. como preocupações de deployment, performance, 
     robustez para manutenção; objetivos (goals) que a arquitetura precisa ter 
     na estrutura e comportamento, e se deve funcionar bem em condições não usuais -->

## 3. Suposições e dependências

As seguintes definições foram estabelecidas inicialmente pelo grupo:

* O sistema será desenvolvido como um **site**.
* O sistema utilizará uma **interface gráfica**.
* O usuário deverá criar uma conta para acessar os serviços disponibilizados.
* O usuário deverá se autenticar para acessar os serviços.
* As funcionalidades do sistema serão organizadas a partir das histórias de usuário definidas pelo grupo.
* O sistema deverá trabalhar com projetos, Product Backlogs, Sprint Backlogs, histórias de usuário, épicos, critérios de aceitação, Story Points, MoSCoW e RICE.
* O projeto contará com integração entre a interface, o backend e o banco de dados.

Pretendemos trabalhar com **usuário único, sem diferenciar as pessoas**.

<!-- premissas sobre o comportamento, consistencia de dados, performance;
    limites antecipados, experiencia da equipe -->
<!-- sistema externos como APIs, bancos de dados compartilhados (nao aplicavel);
    blocos de software ou bibliotecas; -->

## 4. Requisitos significativos para arquitetura

Os principais requisitos funcionais que possuem impacto sobre a arquitetura são:

* Disponibilizar uma interface gráfica para utilização do sistema.
* Permitir criação de conta.
* Permitir autenticação do usuário.
* Permitir acesso aos serviços após autenticação.
* Permitir gerenciamento de projetos.
* Permitir gerenciamento de Product Backlogs.
* Restringir cada projeto a no máximo um Product Backlog.
* Permitir gerenciamento de vários Sprint Backlogs por projeto.
* Permitir movimentação de histórias entre backlogs.
* Permitir gerenciamento de histórias de usuário.
* Associar inicialmente uma história de usuário a um Product Backlog.
* Permitir gerenciamento e vínculo de épicos e histórias de usuário.
* Permitir gerenciamento de critérios de aceitação.
* Permitir atribuição de Story Points.
* Permitir classificação por MoSCoW.
* Permitir utilização e cálculo de RICE.
  Esses requisitos deverão ser considerados na definição da estrutura do sistema, da persistência dos dados e da comunicação entre as partes da aplicação.
  
<!-- referencia ou lik para requisitos que devem ser implementados para 
    realizar a arquitetura -->

## 5. Decisões, restrições e justificativas

### 5.1 Decisões

* O produto será desenvolvido como um **site**.
* Será utilizada uma **interface gráfica**.
* O sistema terá criação de conta e autenticação.
* As funcionalidades serão organizadas de acordo com as histórias de usuário definidas pelo grupo.
* O desenvolvimento terá divisão de responsabilidades entre arquitetura/backend, banco de dados e interface/frontend.

### 5.2 Restrições

* Cada projeto poderá possuir no máximo um Product Backlog.
* Um projeto poderá possuir vários Sprint Backlogs.
* Uma história de usuário deverá ser inicialmente associada a um Product Backlog.
* Os Story Points deverão utilizar somente os valores definidos no projeto.
* Os critérios de MoSCoW deverão utilizar somente os valores definidos no projeto.
* Os critérios de RICE deverão seguir os valores definidos para Reach, Impact, Confidence e Effort.
* O cálculo do RICE deverá utilizar a fórmula definida no projeto.

### 5.3 Justificativas

A escolha por desenvolver o produto como um site foi registrada pelo grupo devido à maior facilidade de encontrar informações e realizar o desenvolvimento dessa forma.

As demais decisões arquiteturais específicas, como tecnologias, frameworks, bibliotecas, padrões arquiteturais e estrutura interna da aplicação, ainda serão definidas pelo grupo.

<!-- decisoes a respeito de abordagens de arquiteutra e as restrições colocadas;
     decisao/constraint e justificativa em bullet points; pode ter lista de dos 
     e donts-->

## 6. Mecanismos de arquitetura

Neste momento, os mecanismos de arquitetura ainda estão **em definição**.

Com base nas funcionalidades já definidas, deverão ser considerados mecanismos relacionados a:

* Autenticação do usuário;
* Persistência das informações;
* Comunicação entre a interface e o backend;
* Gerenciamento dos dados dos projetos;
* Gerenciamento dos diferentes tipos de backlog;
* Gerenciamento das histórias de usuário;
* Cálculo da pontuação RICE.

As tecnologias e mecanismos específicos a serem utilizados ainda não foram definidos na reunião.

### 6.1 Ferramentas usadas

Para o desenvolvimento do backend do sistema, foram definidas inicialmente as seguintes dependências Python:

* **Flask 3.1.3:** microframework web utilizado para o desenvolvimento do backend da aplicação.
* **Flask-SQLAlchemy 3.1.1:** extensão que integra o Flask ao SQLAlchemy, facilitando a utilização do ORM e o gerenciamento da camada de persistência.
* **SQLAlchemy 2.0.54:** toolkit de banco de dados para Python, permitindo trabalhar com os dados por meio de consultas SQL ou utilizando orientação a objetos. A biblioteca também permite que a aplicação seja configurada para diferentes sistemas de banco de dados por meio da definição da URI de conexão.
* **Werkzeug 3.1.8:** biblioteca utilizada pelo Flask que fornece funcionalidades relacionadas à segurança, incluindo recursos para geração e verificação de hashes de senhas.

A configuração do banco de dados poderá ser definida posteriormente de acordo com a escolha do sistema de gerenciamento de banco de dados. Dessa forma, a aplicação poderá utilizar diferentes bancos de dados alterando sua configuração de conexão.

A configuração do ambiente de testes também poderá utilizar um banco de dados separado do banco principal, permitindo a realização dos testes sem interferir nos dados da aplicação.

> **Observação:** as versões e dependências apresentadas correspondem à proposta inicial discutida pelo grupo e poderão ser ajustadas durante o desenvolvimento do projeto.


## 7. Abstrações relativas à arquitetura

As principais abstrações identificadas a partir das funcionalidades definidas são:

* **Usuário**;
* **Projeto**;
* **Product Backlog**;
* **Sprint Backlog**;
* **História de Usuário**;
* **Épico**;
* **Critério de Aceitação**;
* **Story Points**;
* **MoSCoW**;
* **RICE**.

Essas abstrações correspondem aos principais elementos funcionais identificados na reunião e deverão ser consideradas durante a definição do modelo de dados e da implementação do sistema.

## 8. Arquitetura segundo perspectivas

### Perspectiva funcional

O sistema será organizado em torno do gerenciamento de requisitos por meio de histórias de usuário, incluindo projetos, backlogs, histórias, épicos, critérios de aceitação e mecanismos de estimativa e priorização.

### Perspectiva de interface

O sistema será disponibilizado como um site com uma interface gráfica.

### Perspectiva de dados

O sistema deverá armazenar as informações necessárias ao gerenciamento dos projetos e dos elementos relacionados às histórias de usuário.

A estrutura física do banco de dados ainda será definida.

### Perspectiva de backend

O backend será responsável pela implementação das regras de negócio e dos serviços necessários para o funcionamento do sistema.

A arquitetura interna e as tecnologias do backend ainda serão definidas.

### Perspectiva de integração

Deverá existir integração entre a interface, o backend e o banco de dados para permitir o funcionamento das funcionalidades do sistema.

## 9. Impacto de frameworks na arquitetura

Para o desenvolvimento do sistema, foram definidas inicialmente ferramentas e bibliotecas Python para a implementação do backend. Essas tecnologias influenciam principalmente a estrutura do backend, a camada de persistência e o tratamento de funcionalidades relacionadas à segurança.

### Flask

O **Flask 3.1.3** será utilizado como microframework web para o desenvolvimento do backend da aplicação. Sua utilização estabelece o Flask como base para a implementação dos serviços web do sistema.

### Flask-SQLAlchemy

O **Flask-SQLAlchemy 3.1.1** será utilizado para integrar o Flask ao SQLAlchemy, facilitando o gerenciamento da camada de persistência e a utilização do ORM na aplicação.

### SQLAlchemy

O **SQLAlchemy 2.0.54** será utilizado como toolkit de banco de dados para Python. A biblioteca permite trabalhar com o banco de dados por meio de consultas SQL ou utilizando orientação a objetos.

Sua utilização também permite que a aplicação seja configurada para diferentes sistemas de gerenciamento de banco de dados por meio da definição da configuração de conexão. Dessa forma, a escolha definitiva do banco de dados poderá ser realizada posteriormente sem que a camada de acesso aos dados precise ser completamente modificada.

Além disso, a possibilidade de utilizar uma configuração específica para testes permite que o sistema utilize um banco de dados separado durante a execução dos testes.

### Werkzeug

O **Werkzeug 3.1.8** será utilizado como biblioteca relacionada ao Flask e fornece funcionalidades de segurança que podem ser utilizadas pelo sistema, incluindo recursos para geração e comparação de hashes de senhas.

### Impacto geral na arquitetura

A utilização dessas ferramentas estabelece inicialmente uma arquitetura de backend baseada em **Flask**, com o gerenciamento da persistência realizado por meio de **Flask-SQLAlchemy e SQLAlchemy**.

A escolha dessas tecnologias também permite manter a camada de acesso aos dados relativamente independente do sistema de banco de dados utilizado, enquanto o Werkzeug fornece recursos que podem ser utilizados nas funcionalidades relacionadas à autenticação e segurança.

As versões das dependências correspondem à definição inicial apresentada pelo grupo e poderão ser atualizadas durante o desenvolvimento caso seja necessário.
