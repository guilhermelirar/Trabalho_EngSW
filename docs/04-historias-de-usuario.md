
| **Sistema de Gestão de Backlog** | **Responsável** |
| :------------------------------- | :-------------- |
| **Histórias de Usuário**         | Grupo |

# Histórias de Usuário (User Stories)

Este documento apresenta os requisitos funcionais do sistema Backlog Manager por meio de Histórias de Usuário (US) e seus respectivos critérios de aceitação.

As histórias estão organizadas em épicos, que representam os principais grupos de funcionalidades do sistema. Cada história descreve uma necessidade do usuário e o benefício esperado, enquanto seus critérios de aceitação estabelecem as condições que deverão ser atendidas para considerar a funcionalidade implementada corretamente.

As histórias e seus critérios de aceitação deverão orientar o desenvolvimento, a implementação e os testes do sistema.

---

## 1. Visão Geral (Backlog Completo)

| **ID** | **Título** | **Quem** | **Ação** | **Benefício** |
| :--- | :--- | :--- | :--- | :--- |
| **US-001** | Utilizar o sistema por meio de uma interface | Usuário | Utilizar o sistema por meio de uma interface gráfica | Acessar os serviços disponibilizados |
| **US-002** | Criar conta | Usuário | Criar uma conta no sistema | Poder acessar os serviços disponibilizados |
| **US-003** | Autenticar no sistema | Usuário | Informar suas credenciais para autenticação | Acessar os serviços disponibilizados |
| **US-004** | Acessar os serviços após autenticação | Usuário autenticado | Acessar os serviços disponibilizados | Utilizar as funcionalidades do sistema |
| **US-005** | Criar projeto | Usuário | Cadastrar um novo projeto | Organizar seus trabalhos no sistema |
| **US-006** | Consultar projetos | Usuário | Visualizar os projetos cadastrados | Acompanhar os projetos registrados |
| **US-007** | Atualizar projeto | Usuário | Alterar as informações de um projeto | Manter os dados do projeto atualizados |
| **US-008** | Excluir projeto | Usuário | Excluir um projeto cadastrado | Remover projetos que não precisam mais ser gerenciados |
| **US-009** | Gerenciar Product Backlog | Usuário | Criar, consultar, atualizar e excluir um Product Backlog | Gerenciar o backlog de um projeto |
| **US-010** | Restringir a quantidade de Product Backlogs por projeto | Usuário | Manter no máximo um Product Backlog por projeto | Manter a organização do backlog do projeto |
| **US-011** | Criar Sprint Backlog | Usuário | Criar um Sprint Backlog | Organizar o trabalho de uma sprint |
| **US-012** | Consultar Sprint Backlogs | Usuário | Visualizar os Sprint Backlogs cadastrados | Acompanhar a organização das sprints |
| **US-013** | Atualizar Sprint Backlog | Usuário | Alterar as informações de um Sprint Backlog | Manter os dados da sprint atualizados |
| **US-014** | Excluir Sprint Backlog | Usuário | Excluir um Sprint Backlog | Remover sprints que não precisam mais ser gerenciadas |
| **US-015** | Movimentar histórias entre backlogs | Usuário | Movimentar histórias de usuário entre backlogs | Organizar as histórias conforme o planejamento do projeto |
| **US-016** | Criar história de usuário | Usuário | Cadastrar uma nova história de usuário | Registrar os requisitos do projeto |
| **US-017** | Consultar histórias de usuário | Usuário | Visualizar as histórias cadastradas | Acompanhar os requisitos registrados |
| **US-018** | Atualizar história de usuário | Usuário | Alterar as informações de uma história de usuário | Manter os requisitos atualizados |
| **US-019** | Excluir história de usuário | Usuário | Excluir uma história de usuário | Remover requisitos que não precisam mais ser mantidos |
| **US-020** | Utilizar o formato padrão de história de usuário | Usuário | Registrar histórias no formato definido | Padronizar a descrição dos requisitos |
| **US-021** | Gerenciar épicos | Usuário | Criar, consultar, atualizar e excluir épicos | Organizar grandes blocos de trabalho do projeto |
| **US-022** | Vincular histórias de usuário a épicos | Usuário | Vincular histórias de usuário a épicos | Organizar as histórias de acordo com os grandes blocos de trabalho |
| **US-023** | Gerenciar critérios de aceitação | Usuário | Criar, consultar, atualizar e excluir critérios de aceitação | Definir as condições necessárias para a aceitação |
| **US-024** | Utilizar o formato padrão de critério de aceitação | Usuário | Registrar critérios no formato definido | Padronizar os critérios das histórias de usuário |
| **US-025** | Atribuir Story Points | Usuário | Atribuir Story Points às histórias de usuário | Estimar o esforço das histórias |
| **US-026** | Utilizar valores válidos de Story Points | Usuário | Atribuir somente valores permitidos de Story Points | Manter o padrão de estimativa definido pelo sistema |
| **US-027** | Atribuir etiqueta MoSCoW | Usuário | Atribuir uma etiqueta MoSCoW a uma história | Classificá-la segundo sua prioridade |
| **US-028** | Atribuir critérios RICE | Usuário | Atribuir Reach, Impact, Confidence e Effort | Registrar os dados necessários à priorização RICE |
| **US-029** | Calcular pontuação RICE | Usuário | Calcular a pontuação RICE de uma história | Obter sua pontuação segundo os critérios definidos |

As 29 histórias estão organizadas a partir dos oito épicos definidos para o sistema.

---

## 2. Detalhamento das Histórias de Usuário

### EP01 — Interface e Acesso ao Sistema

#### US-001 — Utilizar o sistema por meio de uma interface

* **Como** usuário
* **Eu quero** utilizar o sistema por meio de uma interface gráfica
* **Para** acessar os serviços disponibilizados.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar uma interface gráfica para interação com o usuário.
- A interface deverá apresentar os elementos necessários para acessar as funcionalidades disponibilizadas.
- A navegação deverá permitir que o usuário acesse as diferentes áreas do sistema.

---

#### US-002 — Criar conta

* **Como** usuário
* **Eu quero** criar uma conta no sistema
* **Para** poder acessar os serviços disponibilizados.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar um formulário para cadastro de uma nova conta.
- O usuário deverá informar os dados exigidos pelo formulário para realizar o cadastro.
- Após o envio de informações válidas, a conta deverá ser cadastrada e ficar disponível para autenticações posteriores.
- Caso os dados obrigatórios não sejam informados corretamente, o sistema deverá impedir o cadastro e apresentar uma indicação do problema.

---

#### US-003 — Autenticar no sistema

* **Como** usuário
* **Eu quero** informar minhas credenciais para me autenticar no sistema
* **Para** acessar os serviços disponibilizados.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar um formulário de autenticação.
- Quando o usuário informar credenciais válidas, o sistema deverá permitir sua autenticação.
- Quando o usuário informar credenciais inválidas, o sistema deverá impedir a autenticação e apresentar uma mensagem indicando que os dados informados não são válidos.

---

#### US-004 — Acessar os serviços após autenticação

* **Como** usuário autenticado
* **Eu quero** acessar os serviços disponibilizados pelo sistema
* **Para** utilizar suas funcionalidades.

**Critérios de Aceitação:**

- Após a autenticação bem-sucedida, o sistema deverá permitir o acesso às funcionalidades protegidas.
- Usuários que não estejam autenticados não deverão conseguir acessar diretamente as funcionalidades protegidas.
- Caso um usuário não autenticado tente acessar um serviço protegido, o sistema deverá impedir o acesso.

---

### EP02 — Gestão de Projetos

#### US-005 — Criar projeto

* **Como** usuário
* **Eu quero** cadastrar um novo projeto
* **Para** organizar meus trabalhos no sistema.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar uma opção para cadastrar um projeto.
- O usuário deverá informar os dados para o cadastro do projeto.
- Após o envio de informações válidas, o projeto deverá ser registrado e disponibilizado na relação de projetos.
- Caso os dados não sejam informados, o sistema deverá impedir o cadastro.

---

#### US-006 — Consultar projetos

* **Como** usuário
* **Eu quero** visualizar os projetos cadastrados
* **Para** acompanhar os projetos registrados no sistema.

**Critérios de Aceitação:**

- O sistema deverá apresentar os projetos cadastrados disponíveis para consulta pelo usuário.
- O sistema deverá apresentar suas informações do projeto.
- Caso não existam projetos cadastrados, o sistema deverá abrir uma opção de criar o primeiro projeto.

---

#### US-007 — Atualizar projeto

* **Como** usuário
* **Eu quero** alterar as informações de um projeto
* **Para** manter seus dados atualizados.

**Critérios de Aceitação:**

- O sistema deverá permitir a seleção de um projeto cadastrado para edição.
- O usuário deverá conseguir alterar as informações disponíveis para atualização.
- Após a confirmação de informações válidas, o sistema deverá salvar as alterações.
- As informações atualizadas deverão ser apresentadas ao consultar o projeto.

---

#### US-008 — Excluir projeto

* **Como** usuário
* **Eu quero** excluir um projeto cadastrado
* **Para** remover projetos que não precisam mais ser gerenciados.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar uma opção para excluir um projeto cadastrado.
- Antes de concluir a exclusão, o sistema deverá solicitar a confirmação do usuário.(?)
- Após a confirmação, o projeto deverá deixar de aparecer entre os projetos cadastrados.(?)
- Caso o usuário cancele a operação, o projeto deverá permanecer cadastrado.(?)

---

### EP03 — Gestão de Backlogs

#### US-009 — Gerenciar Product Backlog

* **Como** usuário
* **Eu quero** criar, consultar, atualizar e excluir um Product Backlog
* **Para** gerenciar o backlog de um projeto.

**Regra de Negócio:** Cada projeto poderá possuir, no máximo, um Product Backlog.

**Critérios de Aceitação:**

- O sistema deverá permitir a criação de um Product Backlog para um projeto.
- O sistema deverá permitir a consulta das informações do Product Backlog associado ao projeto.
- O sistema deverá permitir a atualização das informações disponíveis do Product Backlog.
- O sistema deverá disponibilizar a opção de exclusão do Product Backlog, mediante confirmação do usuário.
- As operações deverão respeitar a regra de, no máximo, um Product Backlog por projeto.

---

#### US-010 — Restringir a quantidade de Product Backlogs por projeto

* **Como** usuário
* **Eu quero** que cada projeto tenha no máximo um Product Backlog
* **Para** manter a organização do backlog do projeto.

**Regra de Negócio:** Um projeto não poderá possuir mais de um Product Backlog.

**Critérios de Aceitação:**

- Quando um projeto já possuir um Product Backlog, o sistema deverá impedir a criação de outro para o mesmo projeto.
- Quando o usuário tentar cadastrar um segundo Product Backlog, o sistema deverá informar que o projeto já possui um.
- Projetos que ainda não possuam Product Backlog deverão permitir seu cadastro.

---

#### US-011 — Criar Sprint Backlog

* **Como** usuário
* **Eu quero** criar um Sprint Backlog
* **Para** organizar o trabalho de uma sprint.

**Regra de Negócio:** Um projeto poderá possuir vários Sprint Backlogs.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar uma opção para criar um Sprint Backlog associado a um projeto.
- O Sprint Backlog deverá ser registrado e associado ao projeto correspondente.
- O sistema deverá permitir a criação de mais de um Sprint Backlog para o mesmo projeto.

---

#### US-012 — Consultar Sprint Backlogs

* **Como** usuário
* **Eu quero** visualizar os Sprint Backlogs cadastrados
* **Para** acompanhar a organização das sprints do projeto.

**Critérios de Aceitação:**

- O sistema deverá apresentar os Sprint Backlogs associados ao projeto selecionado.
- Ao selecionar um Sprint Backlog, o sistema deverá apresentar suas informações.

---

#### US-013 — Atualizar Sprint Backlog

* **Como** usuário
* **Eu quero** alterar as informações de um Sprint Backlog
* **Para** manter os dados da sprint atualizados.

**Critérios de Aceitação:**

- O sistema deverá permitir a seleção de um Sprint Backlog para edição.
- O usuário deverá conseguir alterar as informações disponíveis para atualização.
- Após a confirmação de informações válidas, o sistema deverá salvar as alterações.
- As informações atualizadas deverão ser apresentadas na consulta do Sprint Backlog.

---

#### US-014 — Excluir Sprint Backlog

* **Como** usuário
* **Eu quero** excluir um Sprint Backlog
* **Para** remover sprints que não precisam mais ser gerenciadas.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar uma opção para excluir um Sprint Backlog.
- Antes de concluir a exclusão, o sistema deverá solicitar a confirmação do usuário.(?)
- Após a confirmação, o Sprint Backlog deverá deixar de aparecer entre os registros do projeto.(?)
- Caso o usuário cancele a operação, o Sprint Backlog deverá permanecer cadastrado.

---

#### US-015 — Movimentar histórias entre backlogs

* **Como** usuário
* **Eu quero** movimentar histórias de usuário entre backlogs
* **Para** organizar as histórias conforme o planejamento do projeto.

**Critérios de Aceitação:**

- O sistema deverá permitir que uma história de usuário seja selecionada para movimentação entre backlogs.
- O usuário deverá conseguir selecionar o backlog de destino.
- Após a confirmação da operação, a história deverá passar a estar associada ao backlog de destino.
- A movimentação deverá manter a associação da história a apenas um backlog por vez.

---

### EP04 — Gestão de Histórias de Usuário

#### US-016 — Criar história de usuário

* **Como** usuário
* **Eu quero** cadastrar uma nova história de usuário
* **Para** registrar os requisitos do projeto.

**Regra de Negócio:** Toda história de usuário criada deverá ser inicialmente associada ao Product Backlog do projeto correspondente.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar uma opção para cadastrar uma história de usuário.
- O usuário deverá informar os dados necessários para sua criação.
- Após o cadastro, a história deverá ser associada inicialmente ao Product Backlog do projeto.
- Caso o projeto não possua um Product Backlog, o sistema deverá impedir a criação da história e informar a necessidade de um backlog.

---

#### US-017 — Consultar histórias de usuário

* **Como** usuário
* **Eu quero** visualizar as histórias de usuário cadastradas
* **Para** acompanhar os requisitos registrados no projeto.

**Critérios de Aceitação:**

- O sistema deverá apresentar as histórias de usuário associadas ao backlog selecionado.
- Ao selecionar uma história, o sistema deverá apresentar suas informações.
- Caso o backlog não possua histórias cadastradas, o sistema deverá informar que não existem registros disponíveis.

---

#### US-018 — Atualizar história de usuário

* **Como** usuário
* **Eu quero** alterar as informações de uma história de usuário
* **Para** manter os requisitos atualizados.

**Critérios de Aceitação:**

- O sistema deverá permitir a seleção de uma história de usuário para edição.
- O usuário deverá conseguir alterar as informações disponíveis da história.
- Após a confirmação de informações válidas, o sistema deverá salvar as alterações.
- As informações atualizadas deverão ser apresentadas ao consultar a história.

---

#### US-019 — Excluir história de usuário

* **Como** usuário
* **Eu quero** excluir uma história de usuário
* **Para** remover requisitos que não precisam mais ser mantidos.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar uma opção para excluir uma história de usuário.
- Antes de concluir a exclusão, o sistema deverá solicitar a confirmação do usuário.
- Após a confirmação, a história deverá deixar de aparecer entre as histórias cadastradas.
- Caso o usuário cancele a operação, a história deverá permanecer cadastrada.

---

#### US-020 — Utilizar o formato padrão de história de usuário

* **Como** usuário
* **Eu quero** registrar histórias de usuário no formato "Como um [papel], eu quero [ação] para [benefício]"
* **Para** padronizar a descrição dos requisitos.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar campos ou uma estrutura que auxilie o usuário a preencher o papel, a ação e o benefício da história.
- O sistema deverá permitir a visualização da história no formato definido.
- Os três elementos deverão ser utilizados para compor a descrição da história de usuário.

---

### EP05 — Gestão de Épicos

#### US-021 — Gerenciar épicos

* **Como** usuário
* **Eu quero** criar, consultar, atualizar e excluir épicos
* **Para** organizar grandes blocos de trabalho do projeto.

**Critérios de Aceitação:**

- O sistema deverá permitir a criação de novos épicos associados ao projeto.
- O sistema deverá permitir a consulta dos épicos cadastrados.
- O sistema deverá permitir a atualização das informações de um épico.
- O sistema deverá disponibilizar a opção de exclusão de um épico, mediante confirmação do usuário.
- Após cada operação, o sistema deverá apresentar as informações atualizadas dos épicos.

---

#### US-022 — Vincular histórias de usuário a épicos

* **Como** usuário
* **Eu quero** vincular histórias de usuário a épicos
* **Para** organizar as histórias de acordo com os grandes blocos de trabalho do projeto.

**Critérios de Aceitação:**

- O sistema deverá permitir a seleção de uma história de usuário e de um épico cadastrado.
- Após a confirmação, a história deverá ser associada ao épico selecionado.
- A associação deverá ser apresentada nas informações da história ou do épico.
- O sistema deverá permitir a alteração da associação entre histórias e épicos.

---

### EP06 — Gestão de Critérios de Aceitação

#### US-023 — Gerenciar critérios de aceitação

* **Como** usuário
* **Eu quero** criar, consultar, atualizar e excluir critérios de aceitação de uma história de usuário
* **Para** definir as condições necessárias para sua aceitação.

**Critérios de Aceitação:**

- O sistema deverá permitir a criação de critérios de aceitação associados a uma história de usuário.
- O sistema deverá apresentar os critérios cadastrados para a história selecionada.
- O sistema deverá permitir a atualização de critérios existentes.
- O sistema deverá disponibilizar a opção de exclusão de critérios, mediante confirmação do usuário.
- As alterações realizadas deverão ser apresentadas na consulta dos critérios da história correspondente.

---

#### US-024 — Utilizar o formato padrão de critério de aceitação

* **Como** usuário
* **Eu quero** registrar critérios de aceitação no formato "Dado [contexto], quando [ação], então [resultado]"
* **Para** padronizar os critérios das histórias de usuário.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar uma estrutura que auxilie o usuário a preencher o contexto, a ação e o resultado esperado.
- O sistema deverá permitir a visualização do critério no formato definido.
- Os três elementos deverão ser utilizados para compor a descrição do critério de aceitação.

---

### EP07 — Estimativa por Story Points

#### US-025 — Atribuir Story Points

* **Como** usuário
* **Eu quero** atribuir Story Points às histórias de usuário
* **Para** estimar o esforço das histórias.

**Critérios de Aceitação:**

- O sistema deverá permitir que o usuário selecione uma história de usuário para atribuir sua estimativa.
- O sistema deverá disponibilizar os valores de Story Points definidos para seleção.
- Após a confirmação, o valor selecionado deverá ficar associado à história correspondente.
- O valor atribuído deverá ser apresentado nas informações da história.

---

#### US-026 — Utilizar valores válidos de Story Points

* **Como** usuário
* **Eu quero** atribuir somente valores permitidos de Story Points às histórias de usuário
* **Para** manter o padrão de estimativa definido pelo sistema.

**Valores permitidos:**

0, 1, 2, 3, 5, 8, 13, 21, 34 e 55.

**Critérios de Aceitação:**

- O sistema deverá disponibilizar somente os valores definidos na lista de Story Points.
- O sistema não deverá permitir o registro de valores diferentes dos estabelecidos.
- Após a seleção de um valor válido, o sistema deverá associá-lo à história de usuário correspondente.

---

### EP08 — Priorização com MoSCoW e RICE

#### MoSCoW

#### US-027 — Atribuir etiqueta MoSCoW

* **Como** usuário
* **Eu quero** atribuir uma etiqueta MoSCoW a uma história de usuário
* **Para** classificá-la segundo sua prioridade.

**Valores permitidos:**

- M — Must Have
- S — Should Have
- C — Could Have
- W — Won't Have

**Critérios de Aceitação:**

- O sistema deverá disponibilizar as quatro classificações MoSCoW para seleção.
- O usuário deverá conseguir associar uma classificação a uma história de usuário.
- A classificação selecionada deverá ser apresentada nas informações da história.
- O sistema não deverá permitir o registro de classificações diferentes das quatro opções estabelecidas.

---

#### RICE

#### US-028 — Atribuir critérios RICE

* **Como** usuário
* **Eu quero** atribuir os critérios Reach, Impact, Confidence e Effort a uma história de usuário
* **Para** registrar os dados necessários à priorização RICE.

**Regras dos critérios:**

| **Critério** | **Valores permitidos** |
| :--- | :--- |
| **Reach** | Número de usuários |
| **Impact** | 3, 2, 1, 0.5 ou 0.25 |
| **Confidence** | 100%, 80% ou 50% |
| **Effort** | 0, 1, 2, 3, 5, 8, 13, 21, 34 ou 55 Story Points |

**Critérios de Aceitação:**

- O sistema deverá permitir que o usuário informe o valor de Reach para uma história de usuário.
- O sistema deverá disponibilizar somente os valores de Impact definidos na tabela.
- O sistema deverá disponibilizar somente os valores de Confidence definidos na tabela.
- O sistema deverá disponibilizar somente os valores de Effort definidos na tabela.
- Os valores informados ou selecionados deverão ficar associados à história correspondente.
- O sistema deverá apresentar os valores RICE registrados nas informações da história.

---

#### US-029 — Calcular pontuação RICE

* **Como** usuário
* **Eu quero** calcular a pontuação RICE de uma história de usuário
* **Para** obter sua pontuação segundo os critérios definidos.

**Fórmula:**

```text
RICE = (Reach × Impact × Confidence) / Effort
```

**Critérios de Aceitação:**

- O sistema deverá utilizar os valores de Reach, Impact, Confidence e Effort associados à história para realizar o cálculo.
- O sistema deverá apresentar a pontuação RICE obtida.
- Caso algum dos critérios necessários não tenha sido informado, o sistema deverá indicar que os dados estão incompletos e impedir o cálculo.
- O cálculo deverá utilizar os valores de Confidence como porcentagem, conforme a interpretação matemática da fórmula.
- O cálculo não deverá ser realizado quando Effort for igual a zero, até que o grupo defina a regra de negócio para essa situação.

---
