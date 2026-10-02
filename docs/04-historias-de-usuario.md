| Sistema de Gestão de Backlog |                  |
| :--------------------------- | :--------------- |
| **Histórias de Usuário**     | Data: dd/mm/2026 |

# Histórias de Usuário (User Stories)

Este documento mapeia os requisitos funcionais do sistema por meio de Histórias de Usuário (US) e seus respectivos critérios de aceitação.

---

## 1. Visão Geral (Backlog Completo)

| **ID**     | **Título**                                              | **Quem**            | **Ação**                                                     | **Benefício**                                                      |
| ---------- | ------------------------------------------------------- | ------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------ |
| **US-001** | Utilizar o sistema por meio de uma interface            | Usuário             | Utilizar o sistema por meio de uma interface gráfica         | Acessar os serviços disponibilizados                               |
| **US-002** | Criar conta                                             | Usuário             | Criar uma conta no sistema                                   | Poder acessar os serviços disponibilizados                         |
| **US-003** | Autenticar no sistema                                   | Usuário             | Se autenticar no sistema                                     | Acessar os serviços disponibilizados                               |
| **US-004** | Acessar os serviços após autenticação                   | Usuário autenticado | Acessar os serviços disponibilizados                         | Utilizar as funcionalidades do sistema                             |
| **US-005** | Gerenciar projetos                                      | Usuário             | Criar, consultar, atualizar e excluir projetos               | Gerenciar os projetos cadastrados no sistema                       |
| **US-006** | Gerenciar Product Backlog                               | Usuário             | Criar, consultar, atualizar e excluir um Product Backlog     | Gerenciar o backlog de um projeto                                  |
| **US-007** | Restringir a quantidade de Product Backlogs por projeto | Usuário             | Manter no máximo um Product Backlog por projeto              | Manter a organização do backlog do projeto                         |
| **US-008** | Gerenciar Sprint Backlogs                               | Usuário             | Criar, consultar, atualizar e excluir Sprint Backlogs        | Organizar o trabalho das diferentes sprints de um projeto          |
| **US-009** | Movimentar histórias entre backlogs                     | Usuário             | Movimentar histórias de usuário entre backlogs               | Organizar as histórias conforme o planejamento do projeto          |
| **US-010** | Gerenciar histórias de usuário                          | Usuário             | Criar, consultar, atualizar e excluir histórias de usuário   | Registrar e gerenciar os requisitos do projeto                     |
| **US-011** | Utilizar o formato padrão de história de usuário        | Usuário             | Registrar histórias no formato definido                      | Padronizar a descrição dos requisitos                              |
| **US-012** | Gerenciar épicos                                        | Usuário             | Criar, consultar, atualizar e excluir épicos                 | Organizar grandes blocos de trabalho do projeto                    |
| **US-013** | Vincular histórias de usuário a épicos                  | Usuário             | Vincular histórias de usuário a épicos                       | Organizar as histórias de acordo com os grandes blocos de trabalho |
| **US-014** | Gerenciar critérios de aceitação                        | Usuário             | Criar, consultar, atualizar e excluir critérios de aceitação | Definir as condições necessárias para aceitação                    |
| **US-015** | Utilizar o formato padrão de critério de aceitação      | Usuário             | Registrar critérios no formato definido                      | Padronizar os critérios das histórias de usuário                   |
| **US-016** | Atribuir Story Points                                   | Usuário             | Atribuir Story Points às histórias de usuário                | Estimar o esforço das histórias                                    |
| **US-017** | Utilizar valores válidos de Story Points                | Usuário             | Atribuir somente valores permitidos de Story Points          | Manter o padrão de estimativa definido pelo sistema                |
| **US-018** | Atribuir etiqueta MoSCoW                                | Usuário             | Atribuir uma etiqueta MoSCoW a uma história                  | Classificá-la segundo sua prioridade                               |
| **US-019** | Atribuir critérios RICE                                 | Usuário             | Atribuir Reach, Impact, Confidence e Effort                  | Registrar os dados necessários à priorização RICE                  |
| **US-020** | Calcular pontuação RICE                                 | Usuário             | Calcular a pontuação RICE de uma história                    | Obter sua pontuação segundo os critérios definidos                 |

## As 20 histórias foram organizadas a partir dos oito épicos registrados na primeira reunião.
---

# 2. Detalhamento das Histórias de Usuário

## EP01 — Interface e Acesso ao Sistema

### US-001 — Utilizar o sistema por meio de uma interface

* **Como** usuário
* **Eu quero** utilizar o sistema por meio de uma interface gráfica
* **Para** acessar os serviços disponibilizados.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

### US-002 — Criar conta

* **Como** usuário
* **Eu quero** criar uma conta no sistema
* **Para** poder acessar os serviços disponibilizados.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

### US-003 — Autenticar no sistema

* **Como** usuário
* **Eu quero** me autenticar no sistema
* **Para** acessar os serviços disponibilizados.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

### US-004 — Acessar os serviços após autenticação

* **Como** usuário autenticado
* **Eu quero** acessar os serviços disponibilizados pelo sistema
* **Para** utilizar suas funcionalidades.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

# EP02 — Gestão de Projetos

### US-005 — Gerenciar projetos

* **Como** usuário
* **Eu quero** criar, consultar, atualizar e excluir projetos
* **Para** gerenciar os projetos cadastrados no sistema.

**Critérios de Aceitação:**
A definir na próxima reunião.

**Critérios derivados do requisito já registrados:**

* O sistema deve disponibilizar a operação de criação de projetos.
* O sistema deve disponibilizar a operação de consulta de projetos.
* O sistema deve disponibilizar a operação de atualização de projetos.
* O sistema deve disponibilizar a operação de exclusão de projetos.

---

# EP03 — Gestão de Backlogs

## Product Backlog

### US-006 — Gerenciar Product Backlog

* **Como** usuário
* **Eu quero** criar, consultar, atualizar e excluir um Product Backlog
* **Para** gerenciar o backlog de um projeto.

**Regra registrada:** Cada projeto pode possuir no máximo um Product Backlog.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

### US-007 — Restringir a quantidade de Product Backlogs por projeto

* **Como** usuário
* **Eu quero** que cada projeto tenha no máximo um Product Backlog
* **Para** manter a organização do backlog do projeto.

**Regra registrada:** Um projeto não pode possuir mais de um Product Backlog.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

## Sprint Backlog

### US-008 — Gerenciar Sprint Backlogs

* **Como** usuário
* **Eu quero** criar, consultar, atualizar e excluir Sprint Backlogs
* **Para** organizar o trabalho das diferentes sprints de um projeto.

**Regra registrada:** Um projeto pode possuir vários Sprint Backlogs.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

### US-009 — Movimentar histórias entre backlogs

* **Como** usuário
* **Eu quero** movimentar histórias de usuário entre backlogs
* **Para** organizar as histórias conforme o planejamento do projeto.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

# EP04 — Gestão de Histórias de Usuário

### US-010 — Gerenciar histórias de usuário

* **Como** usuário
* **Eu quero** criar, consultar, atualizar e excluir histórias de usuário
* **Para** registrar e gerenciar os requisitos do projeto.

**Regra registrada:** Ao ser criada, uma história de usuário deve ser inicialmente associada a um Product Backlog.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

### US-011 — Utilizar o formato padrão de história de usuário

* **Como** usuário
* **Eu quero** registrar histórias de usuário no formato "Como um [papel] eu quero [ação] para [benefício]"
* **Para** padronizar a descrição dos requisitos.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

# EP05 — Gestão de Épicos

### US-012 — Gerenciar épicos

* **Como** usuário
* **Eu quero** criar, consultar, atualizar e excluir épicos
* **Para** organizar grandes blocos de trabalho do projeto.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

### US-013 — Vincular histórias de usuário a épicos

* **Como** usuário
* **Eu quero** vincular histórias de usuário a épicos
* **Para** organizar as histórias de acordo com os grandes blocos de trabalho do projeto.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

# EP06 — Gestão de Critérios de Aceitação

### US-014 — Gerenciar critérios de aceitação

* **Como** usuário
* **Eu quero** criar, consultar, atualizar e excluir critérios de aceitação de uma história de usuário
* **Para** definir as condições necessárias para sua aceitação.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

### US-015 — Utilizar o formato padrão de critério de aceitação

* **Como** usuário
* **Eu quero** registrar critérios de aceitação no formato "Dado [contexto], quando [ação], então [resultado]"
* **Para** padronizar os critérios das histórias de usuário.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

# EP07 — Estimativa por Story Points

### US-016 — Atribuir Story Points

* **Como** usuário
* **Eu quero** atribuir Story Points às histórias de usuário
* **Para** estimar seu esforço.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

### US-017 — Utilizar valores válidos de Story Points

* **Como** usuário
* **Eu quero** atribuir somente valores permitidos de Story Points às histórias de usuário
* **Para** manter o padrão de estimativa definido pelo sistema.

**Valores permitidos:**
0, 1, 2, 3, 5, 8, 13, 21, 34 e 55.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

# EP08 — Priorização com MoSCoW e RICE

## MoSCoW

### US-018 — Atribuir etiqueta MoSCoW

* **Como** usuário
* **Eu quero** atribuir uma etiqueta MoSCoW a uma história de usuário
* **Para** classificá-la segundo sua prioridade.


**Valores permitidos:**
M, S, C e W.

**Critérios de Aceitação:**
A definir na próxima reunião.

---

## RICE

### US-019 — Atribuir critérios RICE

* **Como** usuário
* **Eu quero** atribuir os critérios Reach, Impact, Confidence e Effort a uma história de usuário
* **Para** registrar os dados necessários à priorização RICE.


**Regras dos critérios:**

| **Critério**   | **Valores permitidos**                          |
| -------------- | ----------------------------------------------- |
| **Reach**      | Número de usuários                              |
| **Impact**     | 3, 2, 1, 0.5 ou 0.25                            |
| **Confidence** | 100, 80 ou 50                                   |
| **Effort**     | 0, 1, 2, 3, 5, 8, 13, 21, 34 ou 55 Story Points |

**Critérios de Aceitação:**
A definir na próxima reunião.

---

### US-020 — Calcular pontuação RICE

* **Como** usuário
* **Eu quero** calcular a pontuação RICE de uma história de usuário
* **Para** obter sua pontuação segundo os critérios definidos.

**Fórmula obrigatória:**

```text
RICE = (Reach × Impact × Confidence) / Effort
```

**Critérios de Aceitação:**
A definir na próxima reunião.

---
