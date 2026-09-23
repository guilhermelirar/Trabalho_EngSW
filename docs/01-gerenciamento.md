| `<Nome do Projeto>`            |                  |
| :----------------------------- | :--------------- |
| **Documento de Gerenciamento** | Data: dd/mm/2026 |

...

# (Nome do Projeto)

## Gerenciamento

### 1. Metodologia de Gerenciamento

Para este projeto será utilizada a metodologia Kanban como ferramenta de
gerenciamento, permitindo observabilidade do progresso de forma visual para
todos os membros da equipe. O controle é realizado por meio de cartões contendo
título, descrição, responsável e critérios de aceitação.

A integração entre o gerenciamento e desenvolvimento será feita via Git: para
cada cartão na coluna "In Progress", o responsável trabalha nas alterações via
branch local (`feature/nome-da-feature`). Ao concluir e o cartão for para
"In Review", o responsável sinaliza a abertura de um Pull Request (PR)
direcionado à branch de desenvolvimento (`dev`). O carão é movido para "Done"
após a revisão e aprovação por outro membro. A branch `main` segue protegida
durante a iteração, com o merge acontecendo apenas em versões estáveis (ao fim
de uma iteração).

Para centralizar o versionamento de código e o gerenciamento do Kanban será
utilizado o site Github, como função de repositório de código e como Kanban por
meio do recurso Github Projects. Dessa forma, um cartão Kanban pode ser mapeado
diretamente a um issue no código, que por sua vez pode ser mapeado a um PR.

### 2. Estrutura do quadro Kanban

<!-- imagem -->

#### 2.1 Propósito das Colunas

- **Backlog**: tarefas mapeadas que ainda não foram priorizadas nem atribuídas.
  A cada iteração, esta lista é refeita.
- **To do**: tarefas que foram priorizadas, desbloqueadas
  e estão prontas para serem puxadas por algum membro da equipe.
- **In progress**: tarefas selecionadas por um ou mais membros da equipe e que estão
  sendo trabalhadas (execução ativa)
- **In review:** tarefas dadas por concluídas pelos seus responsáveis, e portanto
  prontas para serem revisadas por meio de um Pull Request.
- **Done:** tarefas finalizadas, revisadas e integradas à branch de desenvolvimento
  principal

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
