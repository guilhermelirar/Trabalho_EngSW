
| **Sistema de Gestão de Backlog** | **Responsável** |
| :------------------------------- | :-------------- |
| **Visão e Escopo** | Arthur Arruda Frauches — Matrícula: 241017728 |

---

# Backlog Manager

## 1. Visão

### 1.1. Introdução

O Backlog Manager consiste em um sistema para gerenciamento de requisitos baseado em histórias de usuário. Seu objetivo é oferecer um ambiente centralizado para organizar os elementos relacionados aos requisitos de projetos de software.

O sistema permitirá gerenciar projetos, Product Backlogs, Sprint Backlogs, histórias de usuário, épicos e critérios de aceitação. Também oferecerá suporte à estimativa de histórias por meio de Story Points e à priorização utilizando MoSCoW e RICE.

A aplicação será desenvolvida como um site, permitindo que os usuários acessem suas funcionalidades por meio de uma interface gráfica. As tecnologias específicas de front-end, back-end e banco de dados serão registradas nos respectivos documentos técnicos do projeto.

### 1.2. Objetivos do produto

Os principais objetivos do Backlog Manager são:

- Centralizar o gerenciamento dos requisitos de projetos.
- Permitir a criação e a organização de projetos e seus respectivos backlogs.
- Facilitar a criação, a atualização e a organização de histórias de usuário.
- Permitir a criação de épicos e sua associação às histórias de usuário.
- Padronizar a elaboração de histórias de usuário e de seus critérios de aceitação.
- Permitir a atribuição de Story Points às histórias de usuário.
- Apoiar a priorização de histórias por meio dos métodos MoSCoW e RICE.
- Garantir que cada usuário tenha acesso apenas aos projetos vinculados à sua própria conta.
- Permitir o gerenciamento dos registros cadastrados, incluindo sua exclusão definitiva quando solicitada pelo usuário.

### 1.3. Declaração do problema

| Campo | Descrição |
|---|---|
| **O problema** | Necessidade de organizar e gerenciar os elementos relacionados aos requisitos de projetos de software. |
| **Afeta** | Usuários e equipes que utilizam histórias de usuário para gerenciar requisitos de projetos. |
| **O impacto é** | Dificuldade de manter organizados os projetos, backlogs, histórias, critérios de aceitação e informações de estimativa e priorização quando esses elementos não estão centralizados. |
| **Uma solução de sucesso seria** | Um sistema que permita gerenciar esses elementos em um único ambiente, de acordo com as funcionalidades definidas para o projeto, mantendo os projetos de cada usuário separados dos projetos dos demais usuários. |

### 1.4. Declaração de posicionamento do produto

| Campo | Descrição |
|---|---|
| **Para** | Usuários que precisam organizar e gerenciar requisitos de projetos de software. |
| **Quem** | Precisam criar, organizar, estimar e priorizar histórias de usuário. |
| **O Backlog Manager** | É um sistema para gerenciamento de requisitos baseado em histórias de usuário. |
| **Que** | Permite gerenciar projetos, backlogs, histórias de usuário, épicos e critérios de aceitação, além de utilizar Story Points, MoSCoW e RICE. |
| **Ao contrário de** | Alternativas que não reúnam, em um único sistema, as funcionalidades previstas para o projeto. |
| **Nosso produto** | Reúne as funcionalidades de gerenciamento, estimativa e priorização de requisitos definidas para o sistema, mantendo os projetos de cada usuário restritos à sua própria conta. |

---

## 2. Escopo do produto

### 2.1. Funcionalidades incluídas no escopo

O produto deverá contemplar os seguintes grupos de funcionalidades:

| Grupo funcional | Descrição |
|---|---|
| **Interface e acesso ao sistema** | Disponibilizar uma interface gráfica, permitir a criação de contas, a autenticação e o acesso aos serviços após a autenticação. |
| **Gerenciamento de projetos** | Permitir criar, consultar, atualizar e excluir projetos, garantindo que cada usuário visualize e gerencie somente seus próprios projetos. |
| **Gerenciamento de backlogs** | Permitir gerenciar Product Backlogs e Sprint Backlogs e movimentar histórias entre backlogs. |
| **Gerenciamento de histórias de usuário** | Permitir criar, consultar, atualizar e excluir histórias, utilizando o formato padrão definido para sua descrição. |
| **Gerenciamento de épicos** | Permitir criar, consultar, atualizar e excluir épicos, além de vinculá-los às histórias de usuário. |
| **Gerenciamento de critérios de aceitação** | Permitir criar, consultar, atualizar e excluir critérios de aceitação das histórias de usuário, utilizando o formato padrão definido. |
| **Estimativa por Story Points** | Permitir atribuir às histórias de usuário os valores de Story Points estabelecidos nos requisitos do projeto. |
| **Priorização com MoSCoW e RICE** | Permitir atribuir etiquetas MoSCoW, registrar os critérios RICE e calcular a pontuação conforme a fórmula definida. |

Esses grupos representam as principais capacidades previstas para o produto e deverão estar alinhados às histórias de usuário e aos demais artefatos do projeto.

### 2.2. Funcionalidades fora do escopo

Não serão acrescentadas funcionalidades que não tenham sido definidas nos requisitos ou aprovadas pelo grupo.

O compartilhamento de projetos entre diferentes usuários não fará parte do escopo do sistema. Cada usuário terá acesso somente aos projetos vinculados à sua própria conta.

Funcionalidades adicionais, integrações externas ou recursos complementares deverão ser avaliados pela equipe antes de serem incorporados ao escopo do projeto.

---

## 3. Partes interessadas (Stakeholders)

### 3.1. Resumo das partes interessadas

| Parte interessada | Descrição | Responsabilidades ou necessidades |
|---|---|---|
| **Usuário do sistema** | Pessoa que utilizará o Backlog Manager para gerenciar os requisitos de seus projetos. | Criar e gerenciar os elementos disponibilizados pelo sistema, conforme as funcionalidades implementadas, tendo acesso somente aos projetos vinculados à sua própria conta. |
| **Equipe do projeto** | Integrantes responsáveis pelo desenvolvimento do sistema e pela elaboração dos artefatos acadêmicos. | Definir requisitos, projetar e desenvolver a solução, testar o sistema e manter a documentação atualizada. |


### 3.2. Ambiente de utilização

O Backlog Manager será desenvolvido como uma aplicação web, com interface gráfica acessível por meio de navegadores modernos, sem exigir a instalação de um programa específico nos dispositivos dos usuários.

Os futuros usuários poderão acessar o sistema por meio de computadores, notebooks, tablets e celulares, desde que possuam um navegador compatível e conexão de rede para comunicação com o servidor da aplicação.

A interface deverá adaptar sua organização a diferentes tamanhos de tela, permitindo a utilização em dispositivos móveis e computadores. Como referências para os testes de apresentação, deverão ser consideradas as resoluções de 360 × 640 pixels, para dispositivos móveis, e 1366 × 768 pixels, para computadores.

A aplicação deverá funcionar nos navegadores Google Chrome, Mozilla Firefox, Chromium e Microsoft Edge, conforme os requisitos de compatibilidade estabelecidos no documento de Requisitos Não Funcionais.

O acesso às funcionalidades dependerá de uma conta autenticada. Cada usuário poderá visualizar e gerenciar somente os projetos vinculados à sua própria conta, sem acesso aos projetos de outros usuários.

Os detalhes técnicos relativos aos navegadores suportados, à responsividade e à infraestrutura de execução serão apresentados nos documentos de Requisitos Não Funcionais e de Infraestrutura de Implantação.


### 3.3. Organização da equipe

As principais responsabilidades da equipe foram inicialmente distribuídas da seguinte forma:

| Área                                   | Responsável principal     | Atividades principais                                                                                                 |
| -------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Gerenciamento e requisitos**         | Arthur Arruda Frauches    | Organização do Kanban, acompanhamento das atividades, Product Backlog, histórias de usuário e critérios de aceitação. |
| **Arquitetura, integração e back-end** | Guilherme Lira Ribeiro    | Arquitetura do sistema, API, regras de negócio e autenticação.                                                        |
| **Banco de dados**                     | João Vitor Frabis Zago    | Modelo físico, tabelas, relacionamentos, scripts e integração com o back-end.                                         |
| **Interface e front-end**              | Isaac Júnior Araújo Gomes | Wireframes, storyboard, front-end e navegação.                                                                        |
| **Testes, interface e front-end**      | Vinícius Gonçalves Duarte | Testes, front-end, navegação e descrição da infraestrutura de implantação.                                            |

Essa divisão representa as responsabilidades principais e não impede a colaboração entre os integrantes. A distribuição poderá ser ajustada conforme as necessidades e as decisões do grupo.

## 4. Visão geral do produto

O produto será um sistema para gerenciamento de requisitos baseado em histórias de usuário.

Suas funcionalidades estão organizadas nos seguintes grupos:

- Interface e acesso ao sistema;
- Gerenciamento de projetos;
- Gerenciamento de Product Backlogs e Sprint Backlogs;
- Gerenciamento de histórias de usuário;
- Gerenciamento de épicos;
- Gerenciamento de critérios de aceitação;
- Estimativa por Story Points;
- Priorização com MoSCoW e RICE.

Esses grupos correspondem aos oito épicos definidos pelo grupo e documentados no artefato de Histórias de Usuário.

O sistema será organizado de forma que cada usuário possa gerenciar seus próprios projetos e os respectivos elementos, sem acesso aos projetos cadastrados por outros usuários.

## 5. Regras e restrições gerais do produto

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
| **RG-10** | Cada usuário poderá visualizar e gerenciar somente os projetos vinculados à sua própria conta. |
| **RG-11** | Não será permitido compartilhar projetos entre diferentes usuários. |
| **RG-12** | Os registros excluídos serão removidos permanentemente do banco de dados e não poderão ser recuperados pelo sistema. Caso o usuário precise novamente de um registro excluído, deverá cadastrá-lo como um novo registro. |

### 5.1. Regras do RICE

Os critérios RICE deverão respeitar os seguintes valores e significados:

| Critério | Regra |
|---|---|
| **Reach (Alcance)** | Representado pelo número de usuários alcançados. |
| **Impact (Impacto)** | Valores permitidos: 3 (massivo), 2 (alto), 1 (médio), 0,5 (baixo) e 0,25 (mínimo). |
| **Confidence (Confiança)** | Valores permitidos: 100% (alta), 80% (média) e 50% (baixa). |
| **Effort (Esforço)** | Representado por Story Points, utilizando os valores permitidos para o projeto. |
| **Cálculo** | A pontuação deverá ser calculada por `(Reach × Impact × Confidence) / Effort`. |

**Observação:** como o valor zero é permitido para Story Points, o grupo deverá definir o tratamento de Effort igual a zero no cálculo RICE, pois não é possível realizar uma divisão por zero. Essa situação deverá ser tratada antes da implementação da funcionalidade.

### 5.2. Regras de acesso e exclusão de registros

O acesso aos projetos será individualizado. Cada usuário poderá consultar, criar, atualizar e excluir somente os projetos vinculados à sua própria conta. Não haverá compartilhamento de projetos entre usuários.

A exclusão de registros será definitiva. Quando um usuário excluir um registro, ele será removido do banco de dados e não poderá ser recuperado por meio do sistema.

Caso o usuário deseje utilizar novamente um registro que tenha sido excluído, deverá cadastrá-lo novamente. Esse novo cadastro será considerado um novo registro, e não uma recuperação do registro anterior.

O comportamento da exclusão de registros que possuam outros elementos associados deverá ser considerado no projeto do banco de dados e nas regras de implementação, para garantir que os relacionamentos sejam tratados corretamente.

---


## 6. Requisitos gerais e atributos de qualidade

O Backlog Manager deverá disponibilizar uma interface gráfica de fácil compreensão, apresentada em português brasileiro e acessível por meio de navegadores modernos. A organização das páginas deverá facilitar a navegação e a utilização das funcionalidades de gerenciamento de projetos, backlogs e histórias de usuário.

O sistema deverá exigir autenticação para acesso às funcionalidades protegidas, garantindo que cada usuário possa visualizar e gerenciar somente os projetos vinculados à sua própria conta. As senhas deverão ser armazenadas por meio de hash criptográfico, e as informações de configuração deverão ser protegidas contra exposição indevida.

A aplicação deverá apresentar desempenho adequado durante a execução das operações de consulta, criação, atualização e exclusão, além de manter resultados consistentes e compatíveis com as regras de negócio e os critérios de aceitação definidos.

A interface deverá ser responsiva e compatível com os navegadores estabelecidos para o projeto. Também deverá considerar critérios de acessibilidade, utilizando como referência as diretrizes WCAG 2.2, nível AA.

O desenvolvimento deverá permitir a manutenção e a evolução do sistema por meio de uma organização estruturada dos componentes, mantendo a separação entre as responsabilidades do frontend, do backend e do banco de dados.

A aplicação deverá preservar a integridade das informações armazenadas, respeitando os relacionamentos e as restrições definidos para as entidades do sistema. Os registros excluídos deverão ser removidos permanentemente do banco de dados, sem possibilidade de recuperação por meio da aplicação.

Os requisitos não funcionais detalhados, incluindo critérios mensuráveis de segurança, usabilidade, desempenho, confiabilidade, manutenibilidade, compatibilidade, acessibilidade e integridade dos dados, serão especificados no documento próprio de Requisitos Não Funcionais.

---


## 7. Premissas e decisões técnicas

O desenvolvimento do Backlog Manager considerará as seguintes premissas e decisões técnicas:

- **Tipo de aplicação:** o sistema será desenvolvido como uma aplicação web, acessível por meio de navegadores, sem exigir a instalação de um programa específico nos dispositivos dos usuários.
- **Frontend:** a interface utilizará HTML5, CSS3 e JavaScript, com páginas renderizadas no servidor por meio de templates Jinja2 integrados ao Flask. A aplicação utilizará navegação baseada em páginas e formulários tradicionais, sem exigir uma arquitetura Single Page Application (SPA).
- **Backend:** a aplicação será desenvolvida em Python, utilizando o framework Flask para disponibilizar as rotas e controlar o processamento das operações.
- **Arquitetura:** o backend seguirá uma organização em três camadas: rotas (routes), serviços (services) e modelos (models). As regras de negócio, validações e cálculos deverão permanecer concentrados na camada de serviços.
- **Banco de dados:** será utilizado um banco de dados relacional, com SQLite no ambiente de desenvolvimento e no protótipo acadêmico. A integração e a persistência dos dados serão realizadas por meio do SQLAlchemy e do Flask-SQLAlchemy.
- **Autenticação:** o gerenciamento das sessões dos usuários será realizado pelo Flask-Login. O armazenamento das senhas deverá utilizar os recursos de hash criptográfico disponibilizados pelo Werkzeug.
- **Testes:** os testes automatizados deverão utilizar o Pytest, com uma configuração de banco de dados separada daquela utilizada na execução normal do protótipo.
- **Organização da interface:** a aplicação deverá utilizar CSS responsivo para permitir sua utilização em computadores, tablets e celulares.
- **Infraestrutura:** durante o desenvolvimento e a demonstração acadêmica, será utilizado o servidor de desenvolvimento do Flask. Uma eventual implantação pública deverá utilizar uma infraestrutura apropriada para produção, conforme definido no documento de Infraestrutura de Implantação.

A implementação utilizará Python 3.10 ou superior, Flask 3.1.3, Flask-SQLAlchemy 3.1.1 e SQLAlchemy 2.0.54, além das demais dependências registradas no arquivo `requirements.txt`.

A arquitetura deverá permitir a utilização de outros SGBDs relacionais, como PostgreSQL ou MySQL, mediante as configurações necessárias de conexão, mantendo a utilização do ORM.

Os detalhes completos das tecnologias, versões, componentes, responsabilidades arquiteturais e procedimentos de execução serão apresentados no Caderno de Arquitetura e nos documentos técnicos correspondentes.


---

## 8. Relação com os demais artefatos

Este documento apresenta a visão geral e o escopo do Backlog Manager. Os detalhes de implementação e especificação serão registrados nos seguintes artefatos:

| Artefato | Conteúdo principal |
|---|---|
| **Gerenciamento do projeto** | Processo de gerenciamento, quadro Kanban, cartões e acompanhamento das atividades. |
| **Requisitos não funcionais** | Requisitos de qualidade, normas, padrões, métricas e critérios de verificação. |
| **Histórias de usuário** | Especificação das funcionalidades, histórias, critérios de aceitação, estimativas e priorização. |
| **Architecture Notebook** | Arquitetura do software, componentes, relacionamentos e decisões técnicas. |
| **Projeto de interface** | Storyboard, wireframes e organização das telas. |
| **Implementação do front-end** | Descrição das tecnologias de interface, estrutura dos templates, componentes visuais, telas implementadas, interações JavaScript, estilos CSS e responsividade. |
| **Projeto físico do banco de dados** | Tabelas, colunas, chaves, relacionamentos e descrição das estruturas de dados. |
| **Protótipo e testes** | Implementação do protótipo e demonstração do funcionamento por meio de testes de sistema. |
| **Infraestrutura de implantação** | Hardware, software e serviços necessários para implantação. |

---

## 9. Considerações finais

O Backlog Manager tem como finalidade centralizar e organizar o gerenciamento de requisitos de projetos de software por meio de histórias de usuário, backlogs, épicos, critérios de aceitação, estimativas e mecanismos de priorização.

Este documento estabelece a visão geral do produto, seus principais usuários, as funcionalidades previstas e as regras gerais que deverão orientar o desenvolvimento. Também define que os projetos serão individuais, sem compartilhamento entre usuários, e que os registros excluídos serão removidos permanentemente do banco de dados.

Os demais artefatos do projeto deverão detalhar os requisitos funcionais e não funcionais, as decisões arquiteturais, a interface, o banco de dados, os testes e a infraestrutura necessários para a construção da solução.
