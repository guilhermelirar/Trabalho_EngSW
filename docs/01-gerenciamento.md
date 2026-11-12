
| **Sistema de Gestão de Backlog** | **Responsável** |
| :------------------------------- | :-------------- |
| **Gerenciamento de projeto** | Arthur Arruda Frauches — Matrícula: 241017728 |

...


| Informação | Data |
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
| | **BACKLOG** | | | | | |
| | **A FAZER** | | | | | |
| #38 | Frontend - Implementação da tela Projetos | Vinícius Gonçalves Duarte | P0, S, accessibility, feature | A Fazer | Implementar a tela principal de projetos. | Ter a tela projetos de modo funcional |
| #41 | Frontend - Implementação Base da Tela de Projetos | Vinícius Gonçalves Duarte | P0, S | A Fazer | Implementar a estrutura básica da tela de projetos. | Ter a base da tela projetos de modo funcional |
| #42 | Frontend - Implementação Avançada da Tela de Projeto | Vinícius Gonçalves Duarte | P0, XS, feature | A Fazer | Implementar funcionalidades avançadas da tela de projetos. | Ter a parte mais avançada da tela projeto e a ter de modo funcional |
| #45 | Frontend - Implementação do sistema de Tags | Vinícius Gonçalves Duarte | P1, M, accessibility | A Fazer | Implementar o sistema de tags no frontend. | Ter um sistema de Tags claro e funcional ao projeto |
| | **EM ANDAMENTO** | | | | | |
| #43 | Backend - Implementação das partes da tela projeto | Guilherme Lira Ribeiro | P0, XS, accessibility, database, feature | Em Andamento | Implementar as funcionalidades de backend necessárias à tela de projeto. |Ter as funcionalidades de backend necessárias à tela de projeto e permitir, a boa comunicação entre o banco de dados e Frontend |
| #36 | Backend - Fazer nova base do backend | Guilherme Lira Ribeiro | P1, M, documentation | Em Andamento | Desenvolver uma nova base para o backend. | Desenvolver uma nova base para o backend que consiga se adaptar ao novo molde do banco de dados |
| #31 | Frontend - Gerar o modelo para a tela de controle de projetos | Isaac Júnior Araújo Gomes | P2, L, feature | Em Andamento | Gerar o modelo da tela de controle de projetos. | Ter gerado um modelo no Figma de como as telas deverão parecer no produto final junto das variações delas |
| #32 | Frontend - Gerar o modelo das telas de projetos | Isaac Júnior Araújo Gomes | P2, M, feature | Em Andamento | Gerar os modelos das telas de projetos. | Ter gerado um modelo no Figma de como as telas deverão parecer no produto final junto das variações delas |
| | **EM REVISÃO** | | | | | |
| #39 | Backend - Implementação da parte de Projetos | Guilherme Lira Ribeiro | P0, M, feature | Em Revisão | Implementar a parte de projetos no backend. | Ter a implementação do Backend sobre a parte de projetos |
| #33 | Backend - Conectar a tela autenticação e Banco de dados | Guilherme Lira Ribeiro | P1, S, database, feature | Em Revisão | Conectar a tela de autenticação ao banco de dados. | Ter a coneção do banco de dados e o frontend em relação a tela autenticação |
| #30 | Frontend - Implementação da tela Autenticação | Isaac Júnior Araújo Gomes | P1, M, feature | Em Revisão | Implementar a tela de autenticação no frontend. | Ter a tela de autenticação implementada e funcinal |
| | **CONCLUÍDO** | | | | | |
| #1 | Preencher documento de gerenciamento | Guilherme Lira Ribeiro | P0, S, documentation, setup | Concluído | Preencher o documento de gerenciamento do projeto. | Preencher o documento de gerenciamento devidamente e completo |
| #2 | Elaborar documento de visão e escopo (docs/visao.md) | Arthur Arruda Frauches | P0, S, documentation | Concluído | Preencher o documento de visão e escopo | Ter preenchido o documento de visão/escopo devidamente e apresentar ao grupo para discutir metas |
| #3 | Elaborar histórias de usuário | Em Grupo | P0, S, documentation, setup | Concluído | Elaborar as histórias de usuário do sistema. | Possuir historias de usuário o suficente que cubram as especificações do projeto |
| #5 | definir arquitetura | Em grupo | P0, S, documentation, setup | Concluído | Definir a arquitetura do sistema. | Ter como deverá ser o molde da arquitetura mesmo que possa possuir alterações futuras |
| #10 | Criar diagrama do banco de dados da primeira interação | João Vitor Frabis Zago | P1, M, database, documentation, setup | Concluído | Desenvolver um diagrama inicial de como deverá ser o banco de dados | apresentar ao grupo o diagrama inicial |
| #13 | Criar os modelos da arquitetura de telas (frontend) | Isaac Júnior Araújo Gomes | P0, M, accessibility, feature | Concluído | Criar os modelos da arquitetura de telas do frontend. | apresentar ao grupo os modelos inciais de telas |
| #16 | Definir Visão e Escopo | Em Grupo | P0, S, documentation | Concluído |  Em grupo definir qual será nossa visão e escopo | terminar a reunião com questões de visão e escopo bem claras e definidas para prosseguir o projeto |
| #17 | Estudar MoSCoW e RICE | Todos | P2, L, documentation, feature | Concluído | Todos buscarem entender oque é ambos os tópicos e como os implementar no projeto | Ter ciencia dos tópicos e os implementar devidamente |
| #18 | Definir os critérios de aceitação | Arthur Arruda Frauches | P0, S, documentation, feature | Concluído | Definir os critérios de aceitação das tarefas. | Levantas possíveis critérios de aceitação que abortem necessidades ao sistema e que sejam possíveis de se alcançar |
| #22 | Início da implementação a arquitetura de Banco de dados | João Vitor Frabis Zago | P0, S, database, documentation | Concluído | Iniciar a implementação da arquitetura do banco de dados. | Começar a implementação do banco de dados após a reunião |
| #23 | Criar uma arquitetura do Backend | Guilherme Lira Ribeiro | P1, S, documentation, good first issue | Concluído | desenvolver uma base do Backend | Apresentar a base do Backend ao grupo para revisão |
| #24 | Início da implementação do sistema de autenticação | Guilherme Lira Ribeiro | P0, S, accessibility, feature, good first issue | Concluído | Iniciar a implementação do sistema de autenticação. | Inicia a implementação do Backend com base noque foi discutido em reunião  |
| #15 | Atualizar a documentação | Arthur Arruda Frauches | P1, M, documentation | Concluído | Atualizar a documentação do projeto. | Atualizar a documentação com todos os dados atuais |
| #26 | Definindo o nome do projeto no documento Visão | Arthur Arruda Frauches | P1, M, documentation | Concluído | Pensar em um nome do projeto | Apresentar o nome pensado ao grupo e depois discutir se deve ser usado ou não |
| #29 | Teste do sistema de autenticação | Vinícius Gonçalves Duarte | P0, S, accessibility, feature | Concluído | Testar as funcionalidades da tela de autenticação | apresentar os testes ao grupo |
| #34 | BD - Criar o banco de dados para autenticação | João Vitor Frabis Zago | P0, XS, database, feature | Concluído | Criar o banco de dados para autenticação. | Fazer uma implementação real e funcional no banco de dados que suporte as necessidades da tela autenticação |
| #35 | BD - Gerar um modelo atualizado do Banco de dados | João Vitor Frabis Zago | P2, M, database, documentation | Concluído | Gerar um modelo atualizado do Banco de dados. | Após uma reunião desenvolver um novo modelos de banco de dados para que suporte as novas necessidades do sistema |
| #40 | BD - Implementação da parte de Projetos | João Vitor Frabis Zago | P0, S, accessibility, database, feature | Concluído | Criar o banco de dados para projetos. | Fazer uma implementação real e funcional no banco de dados que suporte as necessidades da tela projetos |
| #44 | BD - Implementação do banco de dados da tela projeto | João Vitor Frabis Zago | P0, XS, database, feature | Concluído | Criar o banco de dados para projeto. | Fazer uma implementação real e funcional no banco de dados que suporte as necessidades da tela projeto |
| #46 | BD - Implementação de Tags | João Vitor Frabis Zago | accessibility, database | Concluído | Criar o banco de dados para Tags. | Fazer uma implementação real e funcional no banco de dados que suporte as necessidades das Tags |


### 3.3 Cartões no Modelo a serem desenvolvidos

#### A Fazer

---

#### #38 – Frontend - Implementação da tela Projetos

- **Responsável:** Vinícius Gonçalves Duarte
- **Descrição:** Implementar a tela principal de projetos.
- **Critérios de Aceitação:** Ter a tela projetos de modo funcional.
  - [ ] Critério ainda não atingido

---

#### #41 – Frontend - Implementação Base da Tela de Projetos

- **Responsável:** Vinícius Gonçalves Duarte
- **Descrição:** Implementar a estrutura básica da tela de projetos.
- **Critérios de Aceitação:** Ter a base da tela projetos de modo funcional.
  - [ ] Critério ainda não atingido

---

#### #42 – Frontend - Implementação Avançada da Tela de Projeto

- **Responsável:** Vinícius Gonçalves Duarte
- **Descrição:** Implementar funcionalidades avançadas da tela de projetos.
- **Critérios de Aceitação:** Ter a parte mais avançada da tela projeto e a ter de modo funcional.
  - [ ] Critério ainda não atingido

---

#### #45 – Frontend - Implementação do sistema de Tags

- **Responsável:** Vinícius Gonçalves Duarte
- **Descrição:** Implementar o sistema de tags no frontend.
- **Critérios de Aceitação:** Ter um sistema de Tags claro e funcional ao projeto.
  - [ ] Critério ainda não atingido

---

#### Em Andamento

---

#### #43 – Backend - Implementação das partes da tela projeto

- **Responsável:** Guilherme Lira Ribeiro
- **Descrição:** Implementar as funcionalidades de backend necessárias à tela de projeto.
- **Critérios de Aceitação:** Ter as funcionalidades de backend necessárias à tela de projeto e permitir, a boa comunicação entre o banco de dados e Frontend.
  - [ ] Critério ainda não atingido

---

#### #36 – Backend - Fazer nova base do backend

- **Responsável:** Guilherme Lira Ribeiro
- **Descrição:** Desenvolver uma nova base para o backend.
- **Critérios de Aceitação:** Desenvolver uma nova base para o backend que consiga se adaptar ao novo molde do banco de dados.
  - [ ] Critério ainda não atingido

---

#### #31 – Frontend - Gerar o modelo para a tela de controle de projetos

- **Responsável:** Isaac Júnior Araújo Gomes
- **Descrição:** Gerar o modelo da tela de controle de projetos.
- **Critérios de Aceitação:** Ter gerado um modelo no Figma de como as telas deverão parecer no produto final junto das variações delas.
  - [ ] Critério ainda não atingido

---

#### #32 – Frontend - Gerar o modelo das telas de projetos

- **Responsável:** Isaac Júnior Araújo Gomes
- **Descrição:** Gerar os modelos das telas de projetos.
- **Critérios de Aceitação:** Ter gerado um modelo no Figma de como as telas deverão parecer no produto final junto das variações delas.
  - [ ] Critério ainda não atingido

---

#### Em Revisão

---

#### #39 – Backend - Implementação da parte de Projetos

- **Responsável:** Guilherme Lira Ribeiro
- **Descrição:** Implementar a parte de projetos no backend.
- **Critérios de Aceitação:** Ter a implementação do Backend sobre a parte de projetos.
  - [ ] Critério ainda não atingido

---

#### #33 – Backend - Conectar a tela autenticação e Banco de dados

- **Responsável:** Guilherme Lira Ribeiro
- **Descrição:** Conectar a tela de autenticação ao banco de dados.
- **Critérios de Aceitação:** Ter a conexão do banco de dados e o frontend em relação a tela autenticação.
  - [ ] Critério ainda não atingido

---

#### #30 – Frontend - Implementação da tela Autenticação

- **Responsável:** Isaac Júnior Araújo Gomes
- **Descrição:** Implementar a tela de autenticação no frontend.
- **Critérios de Aceitação:** Ter a tela de autenticação implementada e funcional.
  - [ ] Critério ainda não atingido

---

### 3.4 Cartões no Modelo concluídos

---

#### #1 – Preencher documento de gerenciamento

- **Responsável:** Guilherme Lira Ribeiro
- **Descrição:** Preencher o documento de gerenciamento do projeto.
- **Critérios de Aceitação:** Preencher o documento de gerenciamento devidamente e completo.
  - [x] Critério atingido

---

#### #2 – Elaborar documento de visão e escopo (docs/visao.md)

- **Responsável:** Arthur Arruda Frauches
- **Descrição:** Preencher o documento de visão e escopo.
- **Critérios de Aceitação:** Ter preenchido o documento de visão/escopo devidamente e apresentar ao grupo para discutir metas.
  - [x] Critério atingido

---

#### #3 – Elaborar histórias de usuário

- **Responsável:** Em Grupo
- **Descrição:** Elaborar as histórias de usuário do sistema.
- **Critérios de Aceitação:** Possuir histórias de usuário o suficiente que cubram as especificações do projeto.
  - [x] Critério atingido

---

#### #5 – Definir arquitetura

- **Responsável:** Em grupo
- **Descrição:** Definir a arquitetura do sistema.
- **Critérios de Aceitação:** Ter como deverá ser o molde da arquitetura mesmo que possa possuir alterações futuras.
  - [x] Critério atingido

---

#### #10 – Criar diagrama do banco de dados da primeira interação

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Desenvolver um diagrama inicial de como deverá ser o banco de dados.
- **Critérios de Aceitação:** Apresentar ao grupo o diagrama inicial.
  - [x] Critério atingido

---

#### #13 – Criar os modelos da arquitetura de telas (frontend)

- **Responsável:** Isaac Júnior Araújo Gomes
- **Descrição:** Criar os modelos da arquitetura de telas do frontend.
- **Critérios de Aceitação:** Apresentar ao grupo os modelos iniciais de telas.
  - [x] Critério atingido

---

#### #15 – Atualizar a documentação

- **Responsável:** Arthur Arruda Frauches
- **Descrição:** Atualizar a documentação do projeto.
- **Critérios de Aceitação:** Atualizar a documentação com todos os dados atuais.
  - [x] Critério atingido

---

#### #16 – Definir Visão e Escopo

- **Responsável:** Em Grupo
- **Descrição:** Em grupo definir qual será nossa visão e escopo.
- **Critérios de Aceitação:** Terminar a reunião com questões de visão e escopo bem claras e definidas para prosseguir o projeto.
  - [x] Critério atingido

---

#### #17 – Estudar MoSCoW e RICE

- **Responsável:** Todos
- **Descrição:** Todos buscarem entender o que é ambos os tópicos e como os implementar no projeto.
- **Critérios de Aceitação:** Ter ciência dos tópicos e os implementar devidamente.
  - [x] Critério atingido

---

#### #18 – Definir os critérios de aceitação

- **Responsável:** Arthur Arruda Frauches
- **Descrição:** Definir os critérios de aceitação das tarefas.
- **Critérios de Aceitação:** Levantar possíveis critérios de aceitação que abordem necessidades ao sistema e que sejam possíveis de se alcançar.
  - [x] Critério atingido

---

#### #22 – Início da implementação a arquitetura de Banco de dados

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Iniciar a implementação da arquitetura do banco de dados.
- **Critérios de Aceitação:** Começar a implementação do banco de dados após a reunião.
  - [x] Critério atingido

---

#### #23 – Criar uma arquitetura do Backend

- **Responsável:** Guilherme Lira Ribeiro
- **Descrição:** Desenvolver uma base do Backend.
- **Critérios de Aceitação:** Apresentar a base do Backend ao grupo para revisão.
  - [x] Critério atingido

---

#### #24 – Início da implementação do sistema de autenticação

- **Responsável:** Guilherme Lira Ribeiro
- **Descrição:** Iniciar a implementação do sistema de autenticação.
- **Critérios de Aceitação:** Iniciar a implementação do Backend com base no que foi discutido em reunião.
  - [x] Critério atingido

---

#### #26 – Definindo o nome do projeto no documento Visão

- **Responsável:** Arthur Arruda Frauches
- **Descrição:** Pensar em um nome do projeto.
- **Critérios de Aceitação:** Apresentar o nome pensado ao grupo e depois discutir se deve ser usado ou não.
  - [x] Critério atingido

---

#### #29 – Teste do sistema de autenticação

- **Responsável:** Vinícius Gonçalves Duarte
- **Descrição:** Testar as funcionalidades da tela de autenticação.
- **Critérios de Aceitação:** Apresentar os testes ao grupo.
  - [x] Critério atingido

---

#### #34 – BD - Criar o banco de dados para autenticação

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Criar o banco de dados para autenticação.
- **Critérios de Aceitação:** Fazer uma implementação real e funcional no banco de dados que suporte as necessidades da tela autenticação.
  - [x] Critério atingido

---

#### #35 – BD - Gerar um modelo atualizado do Banco de dados

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Gerar um modelo atualizado do Banco de dados.
- **Critérios de Aceitação:** Após uma reunião desenvolver um novo modelo de banco de dados para que suporte as novas necessidades do sistema.
  - [x] Critério atingido

---

#### #40 – BD - Implementação da parte de Projetos

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Criar o banco de dados para projetos.
- **Critérios de Aceitação:** Fazer uma implementação real e funcional no banco de dados que suporte as necessidades da tela projetos.
  - [x] Critério atingido

---

#### #44 – BD - Implementação do banco de dados da tela projeto

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Criar o banco de dados para projeto.
- **Critérios de Aceitação:** Fazer uma implementação real e funcional no banco de dados que suporte as necessidades da tela projeto.
  - [x] Critério atingido

---

#### #46 – BD - Implementação de Tags

- **Responsável:** João Vitor Frabis Zago
- **Descrição:** Criar o banco de dados para Tags.
- **Critérios de Aceitação:** Fazer uma implementação real e funcional no banco de dados que suporte as necessidades das Tags.
  - [x] Critério atingido

---
