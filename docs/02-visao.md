| Informação | Descrição |
|---|---|
| **Projeto** | Backlog Manager |
| **Documento** | Visão e Escopo |
| **Data da versão** | 07/10/2026 |
| **Finalidade** | Apresentar a visão geral, os objetivos, o escopo e as principais características do produto. |

---
# Backlog Manager

## Visão

## 1. Visão

### 1.1. Introdução

O Backlog Manager consiste em um sistema para gerenciamento de requisitos baseado em histórias de usuário. Seu objetivo é oferecer um ambiente centralizado para organizar os elementos relacionados aos requisitos de projetos de software.

O sistema permitirá gerenciar projetos, Product Backlogs, Sprint Backlogs, histórias de usuário, épicos e critérios de aceitação. Também oferecerá suporte à estimativa de histórias por meio de Story Points e à priorização utilizando MoSCoW e RICE.

A aplicação será desenvolvida como um site, permitindo que os usuários acessem suas funcionalidades por meio de uma interface gráfica. As tecnologias específicas de frontend, backend e banco de dados serão registradas nos respectivos documentos técnicos do projeto.

### 1.2. Objetivos do produto

Os principais objetivos do Backlog Manager são:

- Centralizar o gerenciamento dos requisitos de projetos.
- Permitir a criação e a organização de projetos e seus respectivos backlogs.
- Facilitar a criação, a atualização e a organização de histórias de usuário.
- Permitir a criação de épicos e sua associação às histórias de usuário.
- Padronizar a elaboração de histórias de usuário e de seus critérios de aceitação.
- Permitir a atribuição de Story Points às histórias de usuário.
- Apoiar a priorização de histórias por meio dos métodos MoSCoW e RICE.

### 1.3. Declaração do problema

| Campo | Descrição |
|---|---|
| **O problema** | Necessidade de organizar e gerenciar os elementos relacionados aos requisitos de projetos de software. |
| **Afeta** | Usuários e equipes que utilizam histórias de usuário para gerenciar requisitos de projetos. |
| **O impacto é** | Dificuldade de manter organizados os projetos, backlogs, histórias, critérios de aceitação e informações de estimativa e priorização quando esses elementos não estão centralizados. |
| **Uma solução de sucesso seria** | Um sistema que permita gerenciar esses elementos em um único ambiente, de acordo com as funcionalidades definidas para o projeto. |

### 1.4. Declaração de posicionamento do produto

| Campo | Descrição |
|---|---|
| **Para** | Usuários que precisam organizar e gerenciar requisitos de projetos de software. |
| **Quem** | Precisam criar, organizar, estimar e priorizar histórias de usuário. |
| **O Backlog Manager** | É um sistema para gerenciamento de requisitos baseado em histórias de usuário. |
| **Que** | Permite gerenciar projetos, backlogs, histórias de usuário, épicos e critérios de aceitação, além de utilizar Story Points, MoSCoW e RICE. |
| **Ao contrário de** | Alternativas que não reúnam, em um único sistema, as funcionalidades previstas para o projeto. |
| **Nosso produto** | Reúne as funcionalidades de gerenciamento, estimativa e priorização de requisitos definidas para o sistema. |

---
## 2. Escopo do produto

### 2.1. Funcionalidades incluídas no escopo

O produto deverá contemplar os seguintes grupos de funcionalidades:

| Grupo funcional | Descrição |
|---|---|
| **Interface e acesso ao sistema** | Disponibilizar uma interface gráfica, permitir a criação de contas, a autenticação e o acesso aos serviços após a autenticação. |
| **Gerenciamento de projetos** | Permitir criar, consultar, atualizar e excluir projetos. |
| **Gerenciamento de backlogs** | Permitir gerenciar Product Backlogs e Sprint Backlogs e movimentar histórias entre backlogs. |
| **Gerenciamento de histórias de usuário** | Permitir criar, consultar, atualizar e excluir histórias, utilizando o formato padrão definido para sua descrição. |
| **Gerenciamento de épicos** | Permitir criar, consultar, atualizar e excluir épicos, além de vinculá-los às histórias de usuário. |
| **Gerenciamento de critérios de aceitação** | Permitir criar, consultar, atualizar e excluir critérios de aceitação das histórias de usuário, utilizando o formato padrão definido. |
| **Estimativa por Story Points** | Permitir atribuir às histórias de usuário os valores de Story Points estabelecidos nos requisitos do projeto. |
| **Priorização com MoSCoW e RICE** | Permitir atribuir etiquetas MoSCoW, registrar os critérios RICE e calcular a pontuação conforme a fórmula definida. |

Esses grupos representam as principais capacidades previstas para o produto e deverão estar alinhados às histórias de usuário e aos demais artefatos do projeto.

### 2.2. Funcionalidades fora do escopo

Não serão acrescentadas funcionalidades que não tenham sido definidas nos requisitos ou aprovadas pelo grupo.

Funcionalidades adicionais, integrações externas ou recursos complementares deverão ser avaliados pela equipe antes de serem incorporados ao escopo do projeto.

---

## 3. Partes interessadas (Stakeholders)

### 3.1. Resumo das partes interessadas

| Parte interessada | Descrição | Responsabilidades ou necessidades |
|---|---|---|
| **Usuário do sistema** | Pessoa que utilizará o Backlog Manager para gerenciar os requisitos de seus projetos. | Criar e gerenciar os elementos disponibilizados pelo sistema, conforme as funcionalidades implementadas. |
| **Equipe do projeto** | Integrantes responsáveis pelo desenvolvimento do sistema e pela elaboração dos artefatos acadêmicos. | Definir requisitos, projetar e desenvolver a solução, testar o sistema e manter a documentação atualizada. |

### 3.2. Ambiente de utilização

O Backlog Manager será desenvolvido como um site, com interface gráfica acessível por meio de um navegador.

O sistema contará com criação de contas e autenticação. A existência de contas individuais não implica, por si só, a existência de diferentes perfis de acesso. A diferenciação de permissões deverá seguir as decisões registradas nos requisitos do projeto.

As tecnologias específicas e os detalhes do ambiente de execução serão descritos nos documentos de arquitetura e de infraestrutura.

### 3.3. Organização da equipe

As responsabilidades principais da equipe foram inicialmente distribuídas da seguinte forma:

| Área | Responsável principal | Atividades principais |
|---|---|---|
| **Gerenciamento e requisitos** | Arthur Arruda Frauches | Organização do Kanban, acompanhamento das atividades, Product Backlog, histórias de usuário e critérios de aceitação. |
| **Arquitetura e backend** | Guilherme Lira Ribeiro | Arquitetura do sistema, API, regras de negócio e autenticação. |
| **Banco de dados** | João Vitor Frabis Zago | Modelo físico, tabelas, relacionamentos, scripts e integração com o backend. |
| **Interface e frontend** | Isaac Júnior Araújo Gomes | Wireframes, storyboard, frontend e navegação. |
| **Integração, testes e documentação** | Vinícius Gonçalves Duarte | Integração dos componentes, testes, documentação das atualizações dos testes e descrição da infraestrutura de implantação. |

Essa divisão representa as responsabilidades principais e não impede a colaboração entre os integrantes. A distribuição poderá ser ajustada conforme as necessidades e as decisões do grupo.

---

### 4. Visão geral do produto

O produto será um sistema para gerenciamento de requisitos baseado em histórias de usuário.

Suas funcionalidades estão organizadas nos seguintes grupos:

* Interface e acesso ao sistema;
* Gestão de projetos;
* Gestão de Product Backlog e Sprint Backlogs;
* Gestão de histórias de usuário;
* Gestão de épicos;
* Gestão de critérios de aceitação;
* Estimativa por Story Points;
* Priorização com MoSCoW e RICE.

Esses grupos correspondem aos oito épicos definidos pelo grupo na reunião.

## 4. Regras e restrições gerais do produto

As funcionalidades do sistema deverão respeitar as seguintes regras definidas para o projeto:

| Identificador | Regra |
|---|---|
| **RG-01** | Cada projeto poderá possuir, no máximo, um Product Backlog. |
| **RG-02** | Um projeto poderá possuir vários Sprint Backlogs. |
| **RG-03** | Uma história de usuário deverá ser inicialmente associada a um Product Backlog. |
| **RG-04** | As histórias de usuário deverão utilizar o formato: `Como um [papel], eu quero [ação] para [benefício]`. |
| **RG-05** | Os critérios de aceitação deverão utilizar o formato: `Dado [contexto], quando [ação], então [resultado]`. |
| **RG-06** | Os Story Points permitidos serão: 0, 1, 2, 3, 5, 8, 13, 21, 34 e 55. |
| **RG-07** | As etiquetas MoSCoW permitidas serão M, S, C e W. |
| **RG-08** | O RICE deverá considerar Reach, Impact, Confidence e Effort. |
| **RG-09** | A pontuação RICE deverá seguir a fórmula `(Reach × Impact × Confidence) / Effort`. |

### 4.1. Regras do RICE

Os critérios RICE deverão respeitar os seguintes valores e significados:

| Critério | Regra |
|---|---|
| **Reach (Alcance)** | Representado pelo número de usuários alcançados. |
| **Impact (Impacto)** | Valores permitidos: 3 (massivo), 2 (alto), 1 (médio), 0,5 (baixo) e 0,25 (mínimo). |
| **Confidence (Confiança)** | Valores permitidos: 100% (alta), 80% (média) e 50% (baixa). |
| **Effort (Esforço)** | Representado por Story Points, utilizando os valores permitidos para o projeto. |
| **Cálculo** | A pontuação deverá ser calculada por `(Reach × Impact × Confidence) / Effort`. |

**Observação:** como o valor zero é permitido para Story Points, o grupo deverá definir o tratamento de Effort igual a zero no cálculo RICE, pois não é possível realizar uma divisão por zero. Essa situação deverá ser tratada antes da implementação da funcionalidade.

---
## 5. Requisitos gerais e atributos de qualidade

O sistema deverá disponibilizar uma interface gráfica e exigir autenticação para acesso aos serviços previstos. Também deverá respeitar as regras de negócio definidas para projetos, backlogs, histórias de usuário, épicos, critérios de aceitação, estimativas e priorização.

Os requisitos não funcionais detalhados, incluindo critérios mensuráveis de segurança, usabilidade, desempenho, confiabilidade, padrões e métricas, serão especificados no documento próprio de requisitos não funcionais.

Os detalhes de arquitetura, tecnologias, estrutura do banco de dados, interface e ambiente de implantação serão documentados nos respectivos artefatos do projeto.

---

## 6. Premissas e decisões técnicas

O projeto considera as seguintes premissas:

- O sistema será desenvolvido como uma aplicação web.
- A solução contará com interface gráfica e autenticação.
- As funcionalidades serão implementadas de acordo com os requisitos e as histórias de usuário definidos pelo grupo.
- O desenvolvimento será acompanhado pelo processo de gerenciamento do projeto e pelo quadro Kanban.

As tecnologias específicas de frontend, backend e banco de dados deverão ser registradas nos documentos técnicos correspondentes após sua definição pela equipe.

---

## 7. Relação com os demais artefatos

Este documento apresenta a visão geral e o escopo do Backlog Manager. Os detalhes de implementação e especificação serão registrados nos seguintes artefatos:

| Artefato | Conteúdo principal |
|---|---|
| **Gerenciamento do projeto** | Processo de gerenciamento, quadro Kanban, cartões e acompanhamento das atividades. |
| **Requisitos não funcionais** | Requisitos de qualidade, normas, padrões, métricas e critérios de verificação. |
| **Histórias de usuário** | Especificação das funcionalidades, histórias, critérios de aceitação, estimativas e priorização. |
| **Architecture Notebook** | Arquitetura do software, componentes, relacionamentos e decisões técnicas. |
| **Projeto de interface** | Storyboard, wireframes e organização das telas. |
| **Projeto físico do banco de dados** | Tabelas, colunas, chaves, relacionamentos e descrição das estruturas de dados. |
| **Protótipo e testes** | Implementação do protótipo e demonstração do funcionamento por meio de testes de sistema. |
| **Infraestrutura de implantação** | Hardware, software e serviços necessários para implantação. |

---

## 8. Considerações finais

O Backlog Manager tem como finalidade centralizar e organizar o gerenciamento de requisitos de projetos de software por meio de histórias de usuário, backlogs, épicos, critérios de aceitação, estimativas e mecanismos de priorização.

Este documento estabelece a visão geral do produto, seus principais usuários, as funcionalidades previstas e as regras gerais que deverão orientar o desenvolvimento. Os demais artefatos do projeto deverão detalhar os requisitos funcionais e não funcionais, as decisões arquiteturais, a interface, o banco de dados, os testes e a infraestrutura necessários para a construção da solução.
