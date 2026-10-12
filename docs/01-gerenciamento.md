| `Backlog Manager`            |                  |
| :----------------------------- | :--------------- |
| **Documento de Gerenciamento** | Data: dd/mm/2026 |
| Primeira reunião oficial | Data: 25/09/2026 |
| Segunda reunião oficial | Data: 03/10/2026 |
| Terceira reunião oficial | Data: 10/10/2026 |

...

# BACKLOG MANAGER

## Gerenciamento

### 1. Metodologia de Gerenciamento
O projeto será desenvolvido utilizando uma abordagem iterativa e incremental, conforme estabelecido no trabalho da disciplina.

Para o gerenciamento das atividades, será utilizado um quadro Kanban, no qual as tarefas serão organizadas em cartões e acompanhadas conforme seu andamento.

O grupo pretende realizar uma reunião por semana, com o dia definido semanalmente, para acompanhar o desenvolvimento do projeto, atualizar os integrantes sobre o andamento das atividades e discutir as próximas ações.

As responsabilidades principais foram inicialmente divididas entre os integrantes, mas as atividades poderão ser realizadas em conjunto quando necessário.
### 2. Estrutura do quadro Kanban

<!-- imagem -->


<img width="1924" height="852" alt="Quadro Kanban 01" src="https://github.com/user-attachments/assets/3d4b265f-8bc6-48bf-aa3b-6477c5c4ed45" />
(Quadro da segunda reunião de alinhamento mostrando o início do projeto)

- **Backlog:** reúne as atividades identificadas para o projeto que ainda não foram selecionadas para execução. Tem como propósito manter registradas as atividades que precisam ser realizadas durante o desenvolvimento do projeto.
- **A Fazer:** reúne as atividades selecionadas pelo grupo e que estão prontas para serem iniciadas. Tem como propósito indicar as atividades que já foram selecionadas para execução.
- **Em Andamento:** reúne as atividades que estão sendo executadas por um ou mais integrantes. Tem como propósito indicar quais atividades estão atualmente sendo desenvolvidas.
- **Em Revisão:** reúne as atividades que foram realizadas e aguardam revisão pelo grupo. Tem como propósito indicar quais atividades foram realizadas e precisam ser revisadas.
- **Concluído:** reúne as atividades realizadas e revisadas pelo grupo. Tem como propósito registrar as atividades que foram finalizadas após revisão.


> **Observação:** a organização das colunas acima constitui a estrutura inicial do quadro. Ao decorrer das reuniões iremos adicionar mais informações ao quadro.

#### 2.1 Propósito das Colunas

<!-- placeholder -->

- **Backlog:** manter registradas as atividades que precisam ser realizadas durante o desenvolvimento do projeto.
- **A Fazer:** indicar as atividades que já foram selecionadas para execução.
- **Em Andamento:** indicar quais atividades estão atualmente sendo desenvolvidas.
- **Em Revisão:** indicar quais atividades foram realizadas e precisam ser revisadas.
- **Concluído:**  registrar as atividades que foram finalizadas após revisão.

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

<!-- Tabela com todos os cartões gerados ao longo do desenvolvimento -->

| ID    | Título                                                       | Membro                                                              | Categoria                                     | Conclusão     | Descrição                                                                                     |
| :---- | :----------------------------------------------------------- | :------------------------------------------------------------------ | :-------------------------------------------- | :------------ | :-------------------------------------------------------------------------------------------- |
| #34   | BD - Criar o banco de dados para autenticação                |  João Vitor Frabis Zago                                                           | P0, XS, database, feature                     | Backlog       | Criar o banco de dados para autenticação.                                                     |
| #33   | Backend - Conectar a tela autenticação e Banco de dados      | Guilherme Lira Ribeiro                                                           | P1, S, database, feature                      | Backlog       | Conectar a tela autenticação e banco de dados.                                                |
| #36   | Backend - Fazer nova base do backend                         | Guilherme Lira Ribeiro                                                           | P1, M, documentation                          | Backlog       | Fazer nova base do backend.                                                                   |
| #35   | BD - Gerar um modelo atualizado do Banco de dados            |  João Vitor Frabis Zago                                                           | P2, M, database, documentation                | Backlog       | Gerar um modelo atualizado do Banco de dados.                                                 |
| #29   | Teste do sistema de autenticação                             | Vinícius Gonçalves Duarte                                                           | P0, S, accessibility, feature                 | A Fazer       | Testar o sistema de autenticação.                                                             |
| #30   | Frontend - Implementação da tela Autenticação                | Isaac Júnior Araújo Gomes                                                           | P1, M, feature                                | A Fazer       | Implementar a tela de autenticação.                                                           |
| #31   | Frontend - Gerar o modelo para a tela de controle de projetos| Isaac Júnior Araújo Gomes                                                           | P2, L, feature                                | A Fazer       | Gerar o modelo para a tela de controle de projetos.                                           |
| #32   | Frontend - Gerar o modelo das telas de projetos              | Isaac Júnior Araújo Gomes                                                           | P2, M, feature                                | A Fazer       | Gerar o modelo das telas de projetos.                                                         |
| #18   | Definir os critérios de aceitação                            | Grupo todo                                                          | P0, S, documentation, feature                 | Em Andamento  | Definir os critérios de aceitação das tarefas.                                                |
| #24   | Início da implementação do sistema de autenticação           | João Vitor Frabis Zago, Guilherme Lira Ribeiro, Isaac Júnior Araújo Gomes | P0, S, accessibility, feature, good first issue | Em Andamento  | Iniciar a implementação do sistema de autenticação.                                           |
| #22   | Início da implementação a arquitetura de Banco de dados      | João Vitor Frabis Zago                                              | P0, S, database, documentation                | Em Andamento  | Iniciar a implementação da arquitetura do banco de dados.                                     |
| #15   | Atualizar a documentação                                     | Arthur Arruda Frauches                                              | P1, M, documentation                          | Em Andamento  | Atualizar a documentação do projeto.                                                          |
| #17   | Estudar MoSCoW e RICE                                        | Todos individualmente                                               | P2, L, documentation, feature                 | Em Andamento  | Estudar os métodos de priorização MoSCoW e RICE.                                              |
| #5    | definir arquitetura                                          | Arthur Arruda Frauches                                                           | P0, S, documentation, setup                   | Em Revisão    | Definir a arquitetura do sistema.                                                             |
| #13   | Criar os modelos da arquitetura de telas (frontend)          | Isaac Júnior Araújo Gomes, Vinícius Gonçalves Duarte                | P0, M, accessibility, feature                 | Em Revisão    | Criar os modelos da arquitetura de telas do frontend.                                         |
| #1    | Preencher documento de gerenciamento                         | Arthur Arruda Frauches                                              | P0, S, documentation, setup                   | Concluído     | Preencher o documento de gerenciamento do projeto.                                            |
| #16   | Definir Visão e Escopo                                       | Grupo todo                                                          | P0, S, documentation                          | Concluído     | Definir a visão e o escopo do projeto.                                                        |
| #3    | Elaborar histórias de usuário                                | Grupo todo                                                          | P0, S, documentation, setup                   | Concluído     | Elaborar as histórias de usuário do sistema.                                                  |
| #10   | Criar diagrama do banco de dados da primeira interação       | João Vitor Frabis Zago                                              | P1, M, database, documentation, setup         | Concluído     | Criar o diagrama do banco de dados da primeira iteração.                                      |
| #2    | Elaborar documento de visão e escopo                         | Grupo todo                                                          | P1, M, documentation, setup                   | Concluído     | Elaborar o documento de visão e escopo (docs/visao.md).                                       |
| #23   | Criar uma arquitetura do Backend                             | Guilherme Lira Ribeiro                                              | P1, M, documentation                          | Concluído     | Criar a arquitetura do backend do sistema.                                                |

#### 3.3 Cartões no Modelo a serem desenvolvidos

- **Título:** #34 BD - Criar o banco de dados para autenticação
- **Descrição:** Criar o banco de dados para autenticação.
- **Critérios de Aceitação:** Ter desenvolvido um banco de dados para a autenticação de modo funcional e percistente
  - [ ] [Critério ainda não atingido]

---

- **Título:** #33 Backend - Conectar a tela autenticação e Banco de dados
- **Descrição:** Conectar a tela autenticação e banco de dados.
- **Critérios de Aceitação:** Construir uma arquitetura que possa conectar a transisão de dados e funcionalidades
  - [ ] [Critério ainda não atingido]

---

- **Título:** #36 Backend - Fazer nova base do backend
- **Descrição:** Fazer nova base do backend.
- **Critérios de Aceitação:** Com base na ultima reunião desenvolver uma arquitetura do Backend que satisfaça oque discutimos
  - [ ] [Critério ainda não atingido]

---

- **Título:** #35 BD - Gerar um modelo atualizado do Banco de dados
- **Descrição:** Gerar um modelo atualizado do Banco de dados.
- **Critérios de Aceitação:** Com base na ultima reunião desenvolver um novo modelo atualizado do Banco de dados que satisfaça oque discutimos
  - [ ] [Critério ainda não atingido]

---

- **Título:** #29 Teste do sistema de autenticação
- **Descrição:** Testar o sistema de autenticação.
- **Critérios de Aceitação:** Aplicar uma serie de testes no sistema completo de autenticação e verificar bugs e falhas
  - [ ] [Critério ainda não atingido]

---

- **Título:** #30 Frontend - Implementação da tela Autenticação
- **Descrição:** Implementar a tela de autenticação.
- **Critérios de Aceitação:** Implementar a tela de autenticação de maneira funcional
  - [ ] [Critério ainda não atingido]

---

- **Título:** #31 Frontend - Gerar o modelo para a tela de controle de projetos
- **Descrição:** Gerar o modelo para a tela de controle de projetos.
- **Critérios de Aceitação:** Com base na ultima reunião desenvolver um novo modelo para a tela requerida com base noque discutimos
  - [ ] [Critério ainda não atingido]

---

- **Título:** #32 Frontend - Gerar o modelo das telas de projetos
- **Descrição:** Gerar o modelo das telas de projetos.
- **Critérios de Aceitação:** Com base na ultima reunião desenvolver um novo modelo para a tela requerida com base noque discutimos
  - [ ] [Critério ainda não atingido]

---

- **Título:** #18 Definir os critérios de aceitação
- **Descrição:** Definir os critérios de aceitação das tarefas e implementar nos documentos de forma gradual.
- **Critérios de Aceitação: Ao terminar o projeto ter detalhado os critários de aceitação de cada tarefa**
  - [ ] [Critério ainda não atingido]

---

- **Título:** #24 Início da implementação do sistema de autenticação
- **Descrição:** Após a criação dos modelos, começar a desenvolver itens relacionados a parte da autenticação, desde o banco de dados até o Frontend e implementando oque for preciso através de testes.
- **Critérios de Aceitação: Desenvolver ao menos uma base do sistema de autenticação do sistema**
  - [ ] [Critério ainda não atingido]

---

- **Título:** #22 Início da implementação a arquitetura de Banco de dados
- **Descrição:** Iniciar a implementação da arquitetura do banco de dados.
- **Critérios de Aceitação: Desenvolver ao menos uma base do sistema de Banco de Dados**
  - [ ] [Critério ainda não atingido]

---

- **Título:** #15 Atualizar a documentação
- **Descrição:** Atualizar a documentação do projeto a cada reunião.
- **Critérios de Aceitação: ao fim do projeto ter toda a documentação atualizada e bem organizada para a entrega**
  - [ ] [Critério ainda não atingido]

---

- **Título:** #17 Estudar MoSCoW e RICE
- **Descrição:** Estudar os métodos de priorização MoSCoW e RICE.
- **Critérios de Aceitação: Cada membro estudar os métodos de priorização MoSCoW e RICE individualmente para alicar no sistema**
  - [ ] [Critério ainda não atingido]

#### 3.4 Cartões no Modelo concluídos

- **Título:** #5 definir arquitetura
- **Descrição:** Definir a arquitetura do sistema.
- **Critérios de Aceitação: A definir**
  - [x] [Critério atingido]

---

- **Título:** #13 Criar os modelos da arquitetura de telas (frontend)
- **Descrição:** Com base noque foi discutido na reunião e também nos documento do projeto, criar os modelos da arquitetura de telas do frontend.
- **Critérios de Aceitação: Criar os modelos que podemos utilizar**
  - [x] [Critério atingido]

---

- **Título:** #1 Preencher documento de gerenciamento
- **Descrição:** Preencher os documentos de gerenciamento do projeto e deixar um monde inicial doque deve ser feito.
- **Critérios de Aceitação: Preencher o documento após a reunião incial**
   - [x] [Critério atingido]

---

- **Título:** #16 Definir Visão e Escopo
- **Descrição:** Definir a visão e o escopo do projeto em grupo com base nos documentos enviados e assim conseguirmos atingir nosso objetivo sem fugir da proposta do projeto.
- **Critérios de Aceitação:Fazer uma reunião com o grupo afim de definir em conjunto a visão e Escopo**
 - [x] [Critério atingido]

---

- **Título:** #3 Elaborar histórias de usuário
- **Descrição:** Elaborar as histórias de usuário do sistema com base noque é necessário para atingir o maior êxito no desenvolvimento do projeto, lendo os requisitos necessários no documento e discutindo em grupo quais as melhores decisões a serem tomadas.
- **Critérios de Aceitação: Desenvolver histórias de usuário o suficiente para satisfazer toda necessidade**
 - [x] [Critério atingido]

---

- **Título:** #10 Criar diagrama do banco de dados da primeira interação
- **Descrição:** Com base noque foi discutido na reunião e também nos documento do projeto, criar o diagrama do banco de dados da primeira iteração.
- **Critérios de Aceitação: Criar um modelo que podemos utilizar**
 - [x] [Critério atingido]

---

- **Título:** #2 Elaborar documento de visão e escopo
- **Descrição:** Elaborar o documento de visão e escopo (docs/visao.md) com o máximo de especificações mas sem redundância.
- **Critérios de Aceitação: Criar os documentos**
 - [x] [Critério atingido]

---

- **Título:** #23 Criar uma arquitetura do Backend
- **Descrição:** Com base noque foi discutido na reunião e também nos documento do projeto, criar a arquitetura do backend do sistema.
- **Critérios de Aceitação: Criar uma arquitetura que podemos utilizar**
 - [x] [Critério atingido]

---
