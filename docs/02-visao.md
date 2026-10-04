| `Backlog Manager`             |                  |
| :------------------------------ | :--------------- |
| **Documento de Visão e Escopo** | Data: dd/mm/2026 |

...

#BACKLOG MANAGER

## Visão

### 1. Introdução
<!-- Descrever elementos da solução nessa seção -->

O projeto consiste no desenvolvimento de um sistema para gerenciamento de requisitos baseado em histórias de usuário.

O sistema permitirá que equipes criem e gerenciem projetos, Product Backlogs, Sprint Backlogs, épicos, histórias de usuário e critérios de aceitação, além de utilizar Story Points, MoSCoW e RICE.

Foi definido pelo grupo que o sistema será desenvolvido como um site, devido à maior facilidade de encontrar informações e realizar o desenvolvimento dessa forma.


### 2. Posicionamento

#### 2.1 Declaração de Problema

| **Campo**                        | **Descrição**                                                                                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **O problema**                   | Necessidade de organizar e gerenciar os elementos relacionados aos requisitos de um projeto.                                                                                    |
| **Afeta**                        | Equipes que trabalham com o gerenciamento de requisitos por meio de histórias de usuário.                                                                                       |
| **O impacto é**                  | Fornecer suporte à gestão de requisitos em projetos onde histórias de usuário são utilizadas.                                                                                   |
| **Uma solução de sucesso seria** | Um sistema que permita gerenciar projetos, backlogs, histórias de usuário, épicos, critérios de aceitação e os mecanismos de estimativa e priorização definidos para o projeto. |


#### 2.2 Declaração da Posição do Produto

#### 
| **Campo**                                           | **Descrição**                                                                                                                                                       |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Para**                                            | Usuários e equipes que utilizam histórias de usuário para gerenciamento de requisitos.                                                                              |
| **Quem**                                            | Precisam criar, organizar e gerenciar os elementos relacionados aos requisitos de seus projetos.                                                                    |
| **O Backlog Manager**                             | é um sistema para gerenciamento de requisitos baseado em histórias de usuário.                                                                                      |
| **Que**                                             | Permite gerenciar projetos, Product Backlogs, Sprint Backlogs, épicos, histórias de usuário e critérios de aceitação, além de utilizar Story Points, MoSCoW e RICE. |
| **Ao contrário de**                                 | Alternativas de gerenciamento de requisitos que não ofereçam, em um único sistema, as funcionalidades definidas para o projeto.                                     |
| **Nosso produto**                                   | Reúne as funcionalidades de gerenciamento, estimativa e priorização definidas pelo grupo em um único sistema.                                                       |


### 3. Descrição das Partes Interessadas (Stakeholders)

#### 3.1. Resumo das partes interessadas

| **Nome**               | **Descrição**                                                                                       | **Responsabilidades**                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Usuário do sistema** | Usuário que utilizará o sistema para gerenciar os elementos relacionados aos requisitos do projeto. | Criar e gerenciar os elementos disponibilizados pelo sistema.                         |
| **Equipe do projeto**  | Integrantes responsáveis pelo desenvolvimento do sistema e dos artefatos do trabalho.               | Desenvolver o sistema, seus artefatos e realizar as atividades atribuídas pelo grupo. |

A reunião registrou a divisão das responsabilidades da equipe entre gerenciamento/requisitos, arquitetura/backend, banco de dados, interface/frontend e integração/testes/documentação.

#### 3.2. Descrição do ambiente de trabalho dos usuários

O sistema será desenvolvido como um **site**, disponibilizando uma interface para utilização de suas funcionalidades.

O grupo pretende trabalhar inicialmente com **usuário único, sem diferenciar as pessoas**, ficando as funcionalidades que esse usuário poderá realizar descritas nas histórias de usuário.

<!-- Descreva o ambiente de trabalho do Product Owner / Gerente de Projeto (dispositivos utilizados, sistemas operacionais, se o trabalho é individual ou em equipe). -->

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

#### 4.1 Necessidades e features

<!-- evitar design, manter descrições em nível geral. capacidades necessárias e
porque (não como) elas devem ser implementadas -->

| **Necessidade**            | **Prioridade** | **Features**                                                                                       |
| -------------------------- | -------------- | -------------------------------------------------------------------------------------------------- |
| Acesso ao sistema          | A definir      | Interface gráfica, criação de conta, autenticação e acesso aos serviços após autenticação.         |
| Gerenciamento de projetos  | A definir      | Criar, consultar, atualizar e excluir projetos.                                                    |
| Gerenciamento de backlogs  | A definir      | Gerenciar Product Backlog e Sprint Backlogs e movimentar histórias entre backlogs.                 |
| Gerenciamento de histórias | A definir      | Criar, consultar, atualizar e excluir histórias de usuário e utilizar o formato padrão definido.   |
| Gerenciamento de épicos    | A definir      | Criar, consultar, atualizar e excluir épicos e vinculá-los às histórias de usuário.                |
| Critérios de aceitação     | A definir      | Criar, consultar, atualizar e excluir critérios de aceitação e utilizar o formato padrão definido. |
| Estimativa                 | A definir      | Atribuir Story Points utilizando os valores permitidos.                                            |
| Priorização                | A definir      | Utilizar etiquetas MoSCoW e critérios RICE, incluindo o cálculo da pontuação.                      |

<!-- OBS: coluna de lancamento planejado removida, porque provavelmente não 
aplicavel, mas caso necessario pode entrar como ultima coluna -->

### 5. Outros requisitos de produto

<!-- em alto nível, listar os padrões aplicáveis, hardware, e requisitos de
plataforma, requisitos de performance, e ambientais --->
<!-- definir range de qualidade para performance, robustez, tolerancia a falhas,
usabilidade--->
<!-- mencionar restrições de design e de ambiente, ou outras coisas assumidas, que
se mudarem, vão alterar este documento (exemplo, ferramenta x nao disponivel)-->
<!-- definir requisitos de documentação, incluindo manual de usuario, ajuda online -->
<!-- definir a prioridade desses outros requisitos de software; incluir, se util,
atributos como estabilidade, beneficio, esforço e risco -->

| **Requisito**                                                                                             | **Prioridade** |
| --------------------------------------------------------------------------------------------------------- | -------------- |
| O sistema deverá possuir uma interface gráfica.                                                           | A definir      |
| O usuário deverá poder criar uma conta.                                                                   | A definir      |
| O usuário deverá poder se autenticar no sistema.                                                          | A definir      |
| Os serviços do sistema deverão ser acessíveis após a autenticação.                                        | A definir      |
| Cada projeto poderá possuir no máximo um Product Backlog.                                                 | A definir      |
| Um projeto poderá possuir vários Sprint Backlogs.                                                         | A definir      |
| Uma história de usuário deverá ser inicialmente associada a um Product Backlog.                           | A definir      |
| As histórias de usuário deverão utilizar o formato "Como um [papel] eu quero [ação] para [benefício]".    | A definir      |
| Os critérios de aceitação deverão utilizar o formato "Dado [contexto], quando [ação], então [resultado]". | A definir      |
| Os Story Points permitidos serão 0, 1, 2, 3, 5, 8, 13, 21, 34 e 55.                                       | A definir      |
| As etiquetas MoSCoW permitidas serão M, S, C e W.                                                         | A definir      |
| O RICE deverá utilizar Reach, Impact, Confidence e Effort.                                                | A definir      |
| A pontuação RICE deverá ser calculada pela fórmula `(Reach × Impact × Confidence) / Effort`.              | A definir      |

<!-- OBS: coluna de lancamento planejado removida, porque provavelmente não 
aplicavel, mas caso necessario pode entrar como ultima coluna -->

<!-- fonte: OpenUP, adaptações talvez necessárias -->
