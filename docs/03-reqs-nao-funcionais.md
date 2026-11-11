
| **Sistema de Gestão de Backlog** | **Responsável** |
| :------------------------------- | :-------------- |
| **Requisitos Não Funcionais** | Arthur Arruda Frauches — Matrícula: 241017728 |

---

# Backlog Manager

## Requisitos Não Funcionais

### 1. Propósito

Este documento descreve os requisitos não funcionais considerados relevantes para o desenvolvimento do Backlog Manager.

Os requisitos não funcionais definem características e restrições relacionadas à qualidade, ao funcionamento e à utilização do sistema, complementando os requisitos funcionais definidos por meio das histórias de usuário.

Os requisitos apresentados neste documento constituem uma definição inicial e poderão ser revisados pelo grupo conforme o desenvolvimento do projeto.

## 2. Requisitos Não Funcionais

### RNF-001 — Usabilidade

O sistema deverá possuir uma interface gráfica organizada e de fácil compreensão, permitindo que o usuário utilize as funcionalidades disponibilizadas de maneira clara e intuitiva.

A organização da interface deverá facilitar o acesso às funcionalidades relacionadas ao gerenciamento de projetos, backlogs, histórias de usuário, épicos, critérios de aceitação, Story Points, MoSCoW e RICE.

**Métrica:**
- Pelo menos 80% dos usuários participantes dos testes deverão conseguir realizar as principais tarefas do sistema sem auxílio externo.
- As operações principais deverão ser realizadas sem que o usuário precise recorrer a instruções externas para compreender a navegação.

---

### RNF-002 — Segurança

O sistema deverá proteger o acesso às funcionalidades que dependem de autenticação, permitindo que seus serviços sejam acessados somente após a autenticação do usuário.

O sistema também deverá garantir que cada usuário tenha acesso somente aos projetos vinculados à sua própria conta, impedindo a visualização, a consulta, a atualização ou a exclusão de projetos pertencentes a outros usuários.

As informações relacionadas às contas dos usuários e aos dados gerenciados pelo sistema deverão ser protegidas contra acessos e operações não autorizados.

**Métrica:**
- 100% das funcionalidades protegidas deverão impedir o acesso de usuários não autenticados.
- 100% dos testes de autorização deverão impedir que um usuário consulte, altere ou exclua projetos pertencentes a outra conta.
- Nenhuma operação não autorizada deverá modificar os dados armazenados no sistema.

---

### RNF-003 — Desempenho

O sistema deverá apresentar desempenho adequado durante a utilização de suas funcionalidades, permitindo que o usuário realize as operações de gerenciamento sem atrasos que prejudiquem sua utilização.

O desempenho deverá ser considerado principalmente nas operações de consulta e gerenciamento dos dados do sistema.

**Métrica:**
- As operações de consulta, criação, atualização e exclusão deverão apresentar tempo de resposta de até 2 segundos em pelo menos 95% dos testes realizados.
- As operações de carregamento das principais telas do sistema deverão apresentar tempo de resposta de até 3 segundos em condições normais de utilização.

---

### RNF-004 — Confiabilidade

O sistema deverá executar suas funcionalidades de maneira consistente, apresentando resultados compatíveis com as operações solicitadas pelo usuário.

As operações de criação, consulta, atualização e exclusão deverão funcionar conforme o comportamento esperado, evitando falhas que comprometam a utilização do sistema.

**Métrica:**
- Pelo menos 99% das operações válidas deverão ser concluídas corretamente durante os testes.
- Nenhuma operação deverá informar sucesso quando a ação solicitada não tiver sido concluída corretamente.
- As operações deverão apresentar resultados compatíveis com os critérios de aceitação definidos nas respectivas histórias de usuário.

---

### RNF-005 — Manutenibilidade

O sistema deverá ser desenvolvido de forma organizada, facilitando a manutenção, a correção de problemas e a evolução das funcionalidades ao longo do desenvolvimento do projeto.

A organização do sistema deverá permitir que os diferentes integrantes responsáveis pela arquitetura e pelo back-end, pelo banco de dados e pela interface e pelo front-end possam trabalhar e realizar alterações de maneira estruturada.

**Métrica:**
- 100% das funcionalidades implementadas deverão possuir código organizado e integrado à estrutura definida para o projeto.
- As alterações realizadas deverão preservar o funcionamento das funcionalidades existentes, conforme verificado pelos testes de regressão.
- Os componentes e módulos do sistema deverão seguir os padrões de organização e documentação definidos pelo grupo.

---

### RNF-006 — Acessibilidade

O sistema deverá apresentar uma interface que facilite a utilização por pessoas com diferentes necessidades, considerando aspectos como legibilidade dos textos, organização dos elementos visuais e facilidade de navegação.

Os componentes da interface deverão ser organizados de maneira clara, permitindo que o usuário identifique as funcionalidades disponíveis e interaja com elas adequadamente.

**Métrica:**
- 100% dos campos de formulário deverão possuir identificação ou rótulos que permitam compreender sua finalidade.
- Os principais elementos de navegação e interação deverão poder ser utilizados por meio do teclado.
- Os textos e elementos visuais deverão apresentar contraste adequado para facilitar a leitura, adotando como referência o nível AA das diretrizes WCAG 2.1.

---

### RNF-007 — Integridade dos Dados

O sistema deverá preservar a integridade das informações armazenadas no banco de dados, garantindo que os registros respeitem as regras de negócio e os relacionamentos definidos para o projeto.

As operações realizadas deverão evitar inconsistências nos dados, como associações inválidas entre projetos, backlogs, histórias de usuário, épicos e critérios de aceitação.

**Métrica:**
- 100% dos relacionamentos definidos no modelo físico do banco de dados deverão respeitar as restrições de integridade referencial.
- Nenhuma operação válida deverá gerar registros com associações incompatíveis com as regras de negócio.
- 100% dos testes de validação deverão impedir a inserção de dados que violem as restrições e regras de negócio implementadas.

---

As métricas e os critérios apresentados constituem metas iniciais para a avaliação dos requisitos não funcionais. Seus valores poderão ser revisados pelo grupo conforme as tecnologias utilizadas, os resultados dos testes e as decisões tomadas durante o desenvolvimento do projeto.

Os requisitos não funcionais poderão ser revisados ou complementados conforme novas decisões forem tomadas durante o desenvolvimento do projeto.
