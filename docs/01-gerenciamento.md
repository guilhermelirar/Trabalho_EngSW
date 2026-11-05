| Informação | Descrição |
|---|---|
| **Projeto** | Backlog Manager |
| **Documento** | Gerenciamento do Projeto |
| **Primeira reunião oficial** | 25/09/2026 |
| **Segunda reunião oficial** | 03/10/2026 |
| **Terceira reunião oficial** | 10/10/2026 |
| **Quarta reunião oficial** | 17/10/2026 |
| **Quinta reunião oficial** | 25/10/2026 |

...

# BACKLOG MANAGER

## Gerenciamento

## 1. Metodologia de gerenciamento

O projeto Backlog Manager será desenvolvido utilizando uma abordagem **iterativa e incremental**. Dessa forma, o sistema será construído gradualmente, por meio de etapas de desenvolvimento, permitindo que suas funcionalidades e seus artefatos sejam elaborados, revisados e aprimorados ao longo do projeto.

Para organizar e acompanhar as atividades, será utilizado o método **Kanban**, por meio de um quadro composto por cartões que representam as tarefas necessárias ao desenvolvimento do sistema. Cada cartão registra informações sobre a atividade e permite acompanhar seu estado de execução.

O grupo pretende realizar reuniões semanais, com o dia definido entre os integrantes a cada semana. Essas reuniões têm como objetivo acompanhar o andamento das atividades, compartilhar informações sobre o desenvolvimento, discutir dificuldades e definir as próximas ações.

As responsabilidades principais foram inicialmente distribuídas entre os integrantes. Essa divisão serve como referência para a organização do trabalho, mas não impede que uma atividade seja realizada em conjunto ou receba contribuições de outros membros quando necessário.

### 1.1. Distribuição inicial de responsabilidades

| Integrante | Área principal | Responsabilidades iniciais |
|---|---|---|
| Arthur Arruda Frauches | Gerenciamento e requisitos | Organização do Kanban, acompanhamento das atividades, Product Backlog, histórias de usuário e critérios de aceitação. |
| Guilherme Lira Ribeiro | Arquitetura, Integração  e backend | Arquitetura do sistema, API, regras de negócio e autenticação. |
| João Vitor Frabis Zago | Banco de dados | Modelo físico, tabelas, relacionamentos, scripts e integração com o backend. |
| Isaac Júnior Araújo Gomes | Interface e frontend | Wireframes, storyboard, frontend e navegação. |
| Vinícius Gonçalves Duarte | Testes, interface e frontend | Testes, frontend, navegação e descrição da infraestrutura de implantação. |

Essa distribuição é inicial e poderá ser ajustada conforme as necessidades do projeto e as decisões tomadas nas reuniões.

---


### 2. Estrutura do quadro Kanban


<!-- imagem -->


<img width="1924" height="852" alt="Quadro Kanban 01" src="https://github.com/user-attachments/assets/3d4b265f-8bc6-48bf-aa3b-6477c5c4ed45" />
(Quadro da segunda reunião de alinhamento mostrando o início do projeto)

<img width="1919" height="947" alt="Quadro Kanban 02(R3)" src="https://github.com/user-attachments/assets/7d0e5b6e-1e12-4bcb-abc7-b5c38608c3cb" />
(Quadro da terceira reunião de alinhamento mostrando o início do projeto)

<img width="1366" height="623" alt="Quadro Kanban 03(R6)" src="https://github.com/user-attachments/assets/d175c003-bece-47fe-8b88-7c6b46cc04bb" />
(Quadro da quarta reunião de alinhamento mostrando o início do projeto)

O quadro está organizado nas seguintes colunas:

- **Backlog:** reúne as atividades identificadas para o projeto que ainda não foram selecionadas para execução.
- **A Fazer:** reúne as atividades selecionadas pelo grupo e prontas para serem iniciadas.
- **Em Andamento:** reúne as atividades que estão sendo executadas por um ou mais integrantes.
- **Em Revisão:** reúne as atividades realizadas que aguardam revisão ou validação.
- **Concluído:** reúne as atividades que foram realizadas e revisadas pelo grupo.

### 2.1. Fluxo de movimentação dos cartões

As atividades são registradas no quadro por meio de cartões. Conforme o trabalho avança, os cartões são movimentados entre as colunas para refletir seu estado atual.

O fluxo previsto é:

**Backlog → A Fazer → Em Andamento → Em Revisão → Concluído**

Uma atividade deve passar para **Em Revisão** quando sua execução estiver pronta para ser avaliada. Após a revisão, ela poderá ser marcada como **Concluído** quando o grupo considerar que os critérios de aceitação definidos para a tarefa foram atendidos. Caso sejam identificados problemas ou pendências, a atividade deverá continuar em revisão ou retornar à etapa apropriada para correção.

O quadro poderá ser atualizado durante o desenvolvimento e nas reuniões da equipe, de acordo com as mudanças nas atividades, nas responsabilidades e nas prioridades do projeto.

---

### 3. Cartões de Gerenciamento

#### 3.1 Modelo de Cartão

- **Título:** [Título breve da tarefa relacionada ao cartão]
- **Descrição:** [Descrição das ações da tarefa, dos artefatos
  produzidos, e referência (quando aplicável) a histórias de usuário
  e outros requisitos mapeados.]
- **Critérios de Aceitação:** [Lista de subtarefas que, quando totalmente completas,
  satisfazem o critério para mover o cartão para "In Review"]
  - [x] [Critério atingido]
  - [ ] [Critério ainda não atingido]

<!-- Tabela com todos os cartões gerados ao longo do desenvolvimento --->

| ID  | Título | Membro | Categoria | Conclusão    | Descrição |
| :-- | :----- | :----- | :-------- | :----------- | :-------- |
| #0  |        |        |           | [dd/mm/2026] |           |
| #1  |        |        |           |              |           |

#### 3.2 Lista de Cartões

<!-- Tabela atualizada com os cartões identificados no quadro Kanban. -->

| ID | Título | Membro (Responsável) | Categoria (Tags) | Conclusão (Status) | Descrição | Critério de aceitação |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **BACKLOG** | | | | | | |
| #3 | Elaborar histórias de usuário | Guilherme Lira Ribeiro | P0, S, documentation, setup | Backlog | Elaborar as histórias de usuário do sistema. | a definir |
| #5 | definir arquitetura | Guilherme Lira Ribeiro | P0, S, documentation, setup | Backlog | Definir a arquitetura do sistema. | a definir |
| #1 | Preencher documento de gerenciamento | Guilherme Lira Ribeiro | P0, S, documentation, setup | Backlog | Preencher o documento de gerenciamento do projeto. | a definir |
| #24 | Início da implementação do sistema de autenticação | Guilherme Lira Ribeiro | P0, S, accessibility, feature, good first issue | Backlog | Iniciar a implementação do sistema de autenticação. | a definir |
| #18 | Definir os critérios de aceitação | Arthur Arruda Frauches | P0, S, documentation, feature | Backlog | Definir os critérios de aceitação das tarefas. | a definir |
| #22 | Início da implementação a arquitetura de Banco de dados | João Vitor Frabis Zago | P0, S, database, documentation | Backlog | Iniciar a implementação da arquitetura do banco de dados. | a definir |
| #16 | Definir Visão e Escopo | a definir | P0, S, documentation | Backlog | a definir | a definir |
| #2 | Elaborar documento de visão e escopo (docs/visao.md) | a definir | P0, S, documentation | Backlog | a definir | a definir |
| **A FAZER** | | | | | | |
| #38 | Frontend - Implementação da tela Projetos | Vinícius Gonçalves Duarte | P0, S, accessibility, feature | A Fazer | Implementar a tela principal de projetos. | a definir |
| #41 | Frontend - Implementação Base da Tela de Projetos | Vinícius Gonçalves Duarte | P0, S | A Fazer | Implementar a estrutura básica da tela de projetos. | a definir |
| #42 | Frontend - Implementação Avançada da Tela de Projeto | Vinícius Gonçalves Duarte | P0, XS, feature | A Fazer | Implementar funcionalidades avançadas da tela de projetos. | a definir |
| #10 | Criar diagrama do banco de dados da primeira interação | João Vitor Frabis Zago | P1, M, database, documentation, setup | A Fazer | a definir | a definir |
| #23 | Criar uma arquitetura do Backend | Guilherme Lira Ribeiro | P1, S, documentation, good first issue | A Fazer | a definir | a definir |
| #45 | Frontend - Implementação do sistema de Tags | Vinícius Gonçalves Duarte | P1, M, accessibility | A Fazer | Implementar o sistema de tags no frontend. | a definir |
| #17 | Estudar MoSCoW e RICE | a definir | P2, L, documentation, feature | A Fazer | a definir | a definir |
| **EM ANDAMENTO** | | | | | | |
| #43 | Backend - Implementação das partes da tela projeto | Guilherme Lira Ribeiro | P0, XS, accessibility, database, feature | Em Andamento | Implementar as funcionalidades de backend necessárias à tela de projeto. | a definir |
| #13 | Criar os modelos da arquitetura de telas (frontend) | a definir | P0, M, accessibility, feature | Em Andamento | Criar os modelos da arquitetura de telas do frontend. | a definir |
| #36 | Backend - Fazer nova base do backend | Guilherme Lira Ribeiro | P1, M, documentation | Em Andamento | Desenvolver uma nova base para o backend. | a definir |
| #31 | Frontend - Gerar o modelo para a tela de controle de projetos | a definir | P2, L, feature | Em Andamento | Gerar o modelo da tela de controle de projetos. | a definir |
| #32 | Frontend - Gerar o modelo das telas de projetos | a definir | P2, M, feature | Em Andamento | Gerar os modelos das telas de projetos. | a definir |
| **EM REVISÃO** | | | | | | |
| #39 | Backend - Implementação da parte de Projetos | Guilherme Lira Ribeiro | P0, M, feature | Em Revisão | Implementar a parte de projetos no backend. | a definir |
| #33 | Backend - Conectar a tela autenticação e Banco de dados | Guilherme Lira Ribeiro | P1, S, database, feature | Em Revisão | Conectar a tela de autenticação ao banco de dados. | a definir |
| #30 | Frontend - Implementação da tela Autenticação | a definir | P1, M, feature | Em Revisão | Implementar a tela de autenticação no frontend. | a definir |
| **CONCLUÍDO** | | | | | | |
| a Definir | BD - Implementação do banco de dados da tela projeto | a definir | P0, XS, database, feature | Concluído | a definir | a definir |
| #29 | Teste do sistema de autenticação | a definir | P0, S, accessibility, feature | Concluído | a definir | a definir |
| #40 | BD - Implementação da parte de Projetos | a definir | P0, S, accessibility, database, feature | Concluído | a definir | a definir |
| #34 | BD - Criar o banco de dados para autenticação | João Vitor Frabis Zago | P0, XS, database, feature | Concluído | Criar o banco de dados para autenticação. | a definir |
| #15 | Atualizar a documentação | Arthur Arruda Frauches | P1, M, documentation | Concluído | Atualizar a documentação do projeto. | a definir |
| #35 | BD - Gerar um modelo atualizado do Banco de dados | João Vitor Frabis Zago | P2, M, database, documentation | Concluído | Gerar um modelo atualizado do Banco de dados. | a definir |
| #46 | BD - Implementação de Tags | a definir | accessibility, database | Concluído | a definir | a definir |
| #26 | Definindo o nome do projeto no documento Visão | a definir | a definir | Concluído | a definir | a definir |
| #37 | a definir | a definir | a definir | Concluído | a definir | a definir |
### 3.3 Cartões no Modelo a serem desenvolvidos

---

#### #34 – BD - Criar o banco de dados para autenticação

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Criar o banco de dados para autenticação.
- **Critérios de Aceitação:** Ter desenvolvido um banco de dados para a autenticação de modo funcional e persistente.
  - [ ] Critério ainda não atingido

---

#### #33 – Backend - Conectar a tela autenticação e Banco de dados

- **Responsável:** Guilherme Lira Ribeiro
- **Descrição:** Conectar a tela de autenticação e banco de dados.
- **Critérios de Aceitação:** Construir uma arquitetura que possa conectar a transição de dados e funcionalidades.
  - [ ] Critério ainda não atingido

---

#### #36 – Backend - Fazer nova base do backend

- **Responsável:** Guilherme Lira Ribeiro
- **Descrição:** Fazer nova base do backend.
- **Critérios de Aceitação:** Com base na última reunião, desenvolver uma arquitetura do backend que satisfaça o que discutimos.
  - [ ] Critério ainda não atingido

---

#### #35 – BD - Gerar um modelo atualizado do Banco de dados

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Gerar um modelo atualizado do Banco de dados.
- **Critérios de Aceitação:** Com base na última reunião, desenvolver um novo modelo atualizado do Banco de dados que satisfaça o que discutimos.
  - [ ] Critério ainda não atingido

---

#### #29 – Teste do sistema de autenticação

- **Responsável:** Vinícius Gonçalves Duarte
- **Descrição:** Testar o sistema de autenticação.
- **Critérios de Aceitação:** Aplicar uma série de testes no sistema completo de autenticação e verificar bugs e falhas.
  - [ ] Critério ainda não atingido

---

#### #30 – Frontend - Implementação da tela Autenticação

- **Responsável:** Isaac Júnior Araújo Gomes
- **Descrição:** Implementar a tela de autenticação.
- **Critérios de Aceitação:** Implementar a tela de autenticação de maneira funcional.
  - [ ] Critério ainda não atingido

---

#### #31 – Frontend - Gerar o modelo para a tela de controle de projetos

- **Responsável:** Isaac Júnior Araújo Gomes
- **Descrição:** Gerar o modelo para a tela de controle de projetos.
- **Critérios de Aceitação:** Com base na última reunião, desenvolver um novo modelo para a tela requerida com base no que discutimos.
  - [ ] Critério ainda não atingido

---

#### #32 – Frontend - Gerar o modelo das telas de projetos

- **Responsável:** Isaac Júnior Araújo Gomes
- **Descrição:** Gerar o modelo das telas de projetos.
- **Critérios de Aceitação:** Com base na última reunião, desenvolver um novo modelo para a tela requerida com base no que discutimos.
  - [ ] Critério ainda não atingido

---

#### #18 – Definir os critérios de aceitação

- **Responsável:** Grupo todo
- **Descrição:** Definir os critérios de aceitação das tarefas e implementar nos documentos de forma gradual.
- **Critérios de Aceitação:** Ao terminar o projeto, ter detalhado os critérios de aceitação de cada tarefa.
  - [ ] Critério ainda não atingido

---

#### #24 – Início da implementação do sistema de autenticação

- **Responsável:** João Vitor Frabis Zago, Guilherme Lira Ribeiro e Isaac Júnior Araújo Gomes
- **Descrição:** Após a criação dos modelos, começar a desenvolver itens relacionados à parte da autenticação, desde o banco de dados até o Frontend, implementando o que for preciso por meio de testes.
- **Critérios de Aceitação:** Desenvolver ao menos uma base do sistema de autenticação do sistema.
  - [ ] Critério ainda não atingido

---

#### #22 – Início da implementação da arquitetura de Banco de dados

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Iniciar a implementação da arquitetura do banco de dados.
- **Critérios de Aceitação:** Desenvolver ao menos uma base do sistema de Banco de Dados.
  - [ ] Critério ainda não atingido

---

#### #15 – Atualizar a documentação

- **Responsável:** Arthur Arruda Frauches
- **Descrição:** Atualizar a documentação do projeto a cada reunião.
- **Critérios de Aceitação:** Ao fim do projeto, ter toda a documentação atualizada e bem organizada para a entrega.
  - [ ] Critério ainda não atingido

---

#### #17 – Estudar MoSCoW e RICE

- **Responsável:** Todos individualmente
- **Descrição:** Estudar os métodos de priorização MoSCoW e RICE.
- **Critérios de Aceitação:** Cada membro estudar os métodos de priorização MoSCoW e RICE individualmente para aplicar no sistema.
  - [ ] Critério ainda não atingido

---

### 3.4 Cartões no Modelo concluídos

---

#### #5 – Definir arquitetura

- **Responsável:** Arthur Arruda Frauches
- **Descrição:** Definir a arquitetura do sistema.
- **Critérios de Aceitação:** A definir.
  - [x] Critério atingido

---

#### #13 – Criar os modelos da arquitetura de telas (frontend)

- **Responsável:** Isaac Júnior Araújo Gomes e Vinícius Gonçalves Duarte
- **Descrição:** Com base no que foi discutido na reunião e também nos documentos do projeto, criar os modelos da arquitetura de telas do frontend.
- **Critérios de Aceitação:** Criar os modelos que podemos utilizar.
  - [x] Critério atingido

---

#### #1 – Preencher documento de gerenciamento

- **Responsável:** Arthur Arruda Frauches
- **Descrição:** Preencher os documentos de gerenciamento do projeto e deixar um modelo inicial do que deve ser feito.
- **Critérios de Aceitação:** Preencher o documento após a reunião inicial.
  - [x] Critério atingido

---

#### #16 – Definir Visão e Escopo

- **Responsável:** Grupo todo
- **Descrição:** Definir a visão e o escopo do projeto em grupo, com base nos documentos enviados, para conseguirmos atingir nosso objetivo sem fugir da proposta do projeto.
- **Critérios de Aceitação:** Fazer uma reunião com o grupo a fim de definir em conjunto a visão e o escopo.
  - [x] Critério atingido

---

#### #3 – Elaborar histórias de usuário

- **Responsável:** Grupo todo
- **Descrição:** Elaborar as histórias de usuário do sistema com base no que é necessário para atingir o maior êxito no desenvolvimento do projeto, lendo os requisitos necessários no documento e discutindo em grupo quais as melhores decisões a serem tomadas.
- **Critérios de Aceitação:** Desenvolver histórias de usuário o suficiente para satisfazer toda necessidade.
  - [x] Critério atingido

---

#### #10 – Criar diagrama do banco de dados da primeira iteração

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Com base no que foi discutido na reunião e também nos documentos do projeto, criar o diagrama do banco de dados da primeira iteração.
- **Critérios de Aceitação:** Criar um modelo que podemos utilizar.
  - [x] Critério atingido

---

#### #2 – Elaborar documento de visão e escopo

- **Responsável:** Grupo todo
- **Descrição:** Elaborar o documento de visão e escopo (docs/visao.md) com o máximo de especificações, mas sem redundância.
- **Critérios de Aceitação:** Criar os documentos.
  - [x] Critério atingido

---

#### #23 – Criar uma arquitetura do Backend

- **Responsável:** Guilherme Lira Ribeiro
- **Descrição:** Com base no que foi discutido na reunião e também nos documentos do projeto, criar a arquitetura do backend do sistema.
- **Critérios de Aceitação:** Criar uma arquitetura que podemos utilizar.
  - [x] Critério atingido

---
