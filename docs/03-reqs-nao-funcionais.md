
| **Sistema de Gestão de Backlog** | **Responsável** |
| :------------------------------- | :-------------- |
| **Requisitos Não Funcionais** | Arthur Arruda Frauches — Matrícula: 241017728 |

---

# Backlog Manager

## Requisitos Não Funcionais

### 1. Propósito

Este documento descreve os requisitos não funcionais e as características gerais que deverão ser consideradas durante o desenvolvimento do Backlog Manager.

Os requisitos apresentados estabelecem condições relacionadas à qualidade, à segurança, ao desempenho, à compatibilidade, às interfaces, às restrições de desenvolvimento, às tecnologias utilizadas e à documentação do sistema.

O documento complementa as histórias de usuário, reunindo requisitos que afetam o funcionamento geral da aplicação e que devem ser respeitados durante o desenvolvimento do frontend, do backend e do banco de dados.

As definições consideram a arquitetura, as tecnologias, as regras de negócio e a infraestrutura estabelecidas nos demais documentos do projeto.

## 2. Requisitos Funcionais Complementares

As funcionalidades principais do Backlog Manager estão especificadas no documento de histórias de usuário e organizadas nos seguintes grupos:

- Interface e acesso ao sistema.
- Gerenciamento de projetos.
- Gerenciamento de Product Backlogs e Sprint Backlogs.
- Gerenciamento de histórias de usuário.
- Gerenciamento de épicos.
- Gerenciamento de critérios de aceitação.
- Estimativa por Story Points.
- Priorização por MoSCoW e RICE.

Além das funcionalidades descritas nas histórias de usuário, o sistema deverá atender aos seguintes requisitos gerais de funcionamento:

**RF-001 — Gerenciamento de sessão**

O sistema deverá utilizar o Flask-Login para controlar as sessões dos usuários autenticados, permitindo identificar o usuário responsável por cada operação e restringir o acesso às páginas protegidas.

**RF-002 — Validação das operações**

Os dados recebidos pelos formulários deverão ser validados pelo backend antes da execução das operações. As validações realizadas exclusivamente pelo JavaScript deverão servir apenas como auxílio à interação, não substituindo as verificações realizadas no servidor.

**RF-003 — Retorno das operações**

O sistema deverá apresentar mensagens de retorno após as operações realizadas pelo usuário, informando quando uma ação for concluída ou quando ocorrer algum problema.

As mensagens deverão utilizar o mecanismo de flash messages disponibilizado pelo Flask.

**RF-004 — Tratamento de erros**

Os erros relacionados às regras de negócio deverão ser tratados por meio da estrutura de exceções da aplicação, utilizando a classe `ServiceError` e o tratamento centralizado implementado no backend.

**RF-005 — Comunicação entre páginas e servidor**

As operações de navegação e consulta deverão utilizar requisições HTTP GET. As operações de criação, atualização e exclusão deverão utilizar HTTP POST.

Após o envio de formulários por POST, deverá ser aplicado o padrão Post-Redirect-Get (PRG), evitando que a atualização da página provoque o reenvio involuntário de uma operação.

## 3. Atributos de Qualidade

### RNF-001 — Usabilidade

O sistema deverá possuir uma interface gráfica organizada e de fácil compreensão, permitindo que o usuário utilize as funcionalidades disponibilizadas de maneira clara e intuitiva.

A interface deverá ser apresentada em português brasileiro e manter uma organização consistente entre as diferentes páginas da aplicação.

A navegação deverá facilitar o acesso às funcionalidades de cadastro e autenticação, gerenciamento de projetos, backlogs, histórias de usuário, épicos, critérios de aceitação, Story Points, MoSCoW e RICE.

Os formulários deverão apresentar campos identificados e organizados, enquanto os cartões, abas, modais e mensagens deverão facilitar a visualização e a utilização das informações.

**Métricas:**

- Pelo menos 80% dos usuários participantes dos testes deverão conseguir realizar as principais tarefas do sistema sem auxílio externo.
- Os usuários deverão conseguir localizar as funcionalidades principais sem depender de instruções externas.
- Todas as operações principais deverão apresentar mensagens de retorno que permitam identificar o resultado da ação realizada.

---

### RNF-002 — Segurança

O sistema deverá proteger o acesso às funcionalidades que dependem de autenticação, permitindo que seus serviços sejam acessados somente após o usuário entrar em sua conta.

Todos os usuários autenticados deverão possuir acesso às mesmas funcionalidades, sem distinção de tipos ou níveis de usuário. Entretanto, cada usuário poderá acessar somente os projetos vinculados à sua própria conta.

O sistema deverá impedir a visualização, a consulta, a atualização ou a exclusão de projetos pertencentes a outros usuários, protegendo as informações armazenadas contra acessos e operações não autorizados.

As senhas deverão ser armazenadas por meio de hash criptográfico, utilizando os recursos de segurança disponibilizados pelo Werkzeug. O gerenciamento das sessões deverá ser realizado por meio do Flask-Login.

As informações utilizadas para configuração da aplicação, como a chave secreta do Flask, deverão ser mantidas fora do código-fonte e não deverão ser disponibilizadas publicamente no repositório.

Em uma implantação acessível pela internet, a comunicação entre o navegador e o servidor deverá utilizar HTTPS, protegendo os dados transmitidos.

**Métricas:**

- 100% das páginas e funcionalidades protegidas deverão impedir o acesso de usuários não autenticados.
- 100% dos testes de autorização deverão impedir que um usuário consulte, altere ou exclua projetos pertencentes a outra conta.
- Nenhuma operação não autorizada deverá modificar os dados armazenados no sistema.
- 100% das senhas armazenadas deverão utilizar hash criptográfico, sem armazenamento de senhas em texto simples.
- Após o encerramento da sessão, o usuário deverá perder o acesso às funcionalidades que exigem autenticação.
- Em ambiente de produção, 100% das páginas e operações deverão ser acessadas por conexão HTTPS.

---

### RNF-003 — Desempenho

O sistema deverá apresentar desempenho adequado durante a utilização de suas funcionalidades, permitindo que o usuário realize as operações de gerenciamento sem atrasos que prejudiquem sua utilização.

O desempenho deverá ser considerado principalmente nas operações de consulta, criação, atualização e exclusão dos dados, bem como no carregamento das principais páginas da aplicação.

As consultas ao banco de dados deverão ser realizadas de maneira adequada, evitando operações desnecessárias que prejudiquem o carregamento das informações dos projetos, backlogs e histórias de usuário.

Para a avaliação do protótipo acadêmico, será considerada como referência uma máquina com pelo menos 1 vCPU e 1 GB de memória RAM, utilizando SQLite e a configuração local descrita no documento de infraestrutura.

**Métricas:**

- As operações de consulta, criação, atualização e exclusão deverão apresentar tempo de resposta de até 2 segundos em pelo menos 95% dos testes realizados.
- O carregamento das principais páginas do sistema deverá apresentar tempo de resposta de até 3 segundos em condições normais de utilização.
- Os testes de desempenho do protótipo deverão considerar a configuração de referência de 1 vCPU, 1 GB de memória RAM e banco de dados SQLite.
- Os resultados deverão ser avaliados considerando a utilização normal do protótipo por um usuário autenticado.

---

### RNF-004 — Confiabilidade

O sistema deverá executar suas funcionalidades de maneira consistente, apresentando resultados compatíveis com as operações solicitadas pelo usuário.

As operações de criação, consulta, atualização e exclusão deverão funcionar conforme o comportamento esperado e os critérios de aceitação definidos nas respectivas histórias de usuário.

O sistema deverá tratar adequadamente falhas durante o processamento das operações, evitando informar sucesso quando uma ação não tiver sido concluída ou quando os dados não tiverem sido armazenados corretamente.

**Métricas:**

- Pelo menos 99% das operações válidas deverão ser concluídas corretamente durante os testes.
- Nenhuma operação deverá informar sucesso quando a ação solicitada não tiver sido concluída corretamente.
- As operações deverão apresentar resultados compatíveis com os critérios de aceitação definidos nas respectivas histórias de usuário.
- Todos os testes automatizados utilizados para validar as funcionalidades implementadas deverão ser executados com sucesso antes da aprovação de uma versão do sistema.
- Erros de negócio deverão ser tratados e apresentados ao usuário por meio de mensagens adequadas, sem expor informações internas desnecessárias da aplicação.

---

### RNF-005 — Manutenibilidade

O sistema deverá ser desenvolvido de forma organizada, permitindo a manutenção, a correção de problemas e a evolução das funcionalidades ao longo do desenvolvimento do projeto.

O backend deverá seguir a arquitetura em três camadas definida pelo grupo:

- **Rotas (routes):** responsáveis pelo recebimento das requisições HTTP, extração dos dados e encaminhamento das operações aos serviços.
- **Serviços (services):** responsáveis pela implementação das regras de negócio, validações, cálculos e tratamento das operações.
- **Modelos (models):** responsáveis pela representação das entidades e pela comunicação com o banco de dados por meio do SQLAlchemy.

O frontend deverá manter a separação entre a estrutura das páginas, a apresentação visual e as interações executadas no navegador, utilizando templates HTML, arquivos CSS e arquivos JavaScript organizados por responsabilidade.

A organização dos componentes deverá permitir que os integrantes responsáveis pelo backend, banco de dados e frontend possam realizar alterações de maneira estruturada, reduzindo a dependência entre os diferentes módulos.

**Métricas:**

- 100% das regras de negócio deverão estar organizadas na camada de serviços do backend, evitando sua implementação diretamente nas rotas ou nos templates da interface.
- Os templates, arquivos CSS e arquivos JavaScript deverão permanecer organizados de acordo com suas respectivas responsabilidades.
- As alterações realizadas deverão preservar o funcionamento das funcionalidades existentes, conforme verificado pelos testes de regressão.
- As dependências utilizadas pelo projeto deverão permanecer registradas no arquivo `requirements.txt`, com suas respectivas versões.
- Os testes automatizados deverão ser organizados e executados por meio do Pytest.

---

### RNF-006 — Compatibilidade

O sistema deverá ser desenvolvido como uma aplicação web, permitindo sua utilização por meio de navegadores modernos, sem exigir a instalação de um programa específico na máquina do usuário.

A interface deverá funcionar adequadamente nos navegadores Google Chrome, Mozilla Firefox, Chromium e Microsoft Edge, mantendo o comportamento dos elementos visuais e das funcionalidades disponibilizadas.

O ambiente responsável pela execução da aplicação deverá ser compatível com distribuições Linux, macOS e Windows, utilizando Python 3.10 ou superior.

**Métricas:**

- 100% das funcionalidades principais deverão funcionar corretamente nas versões estáveis dos navegadores Google Chrome, Mozilla Firefox, Chromium e Microsoft Edge utilizadas durante os testes.
- Não deverão ocorrer erros que impeçam a utilização das funcionalidades principais nos navegadores suportados.
- Os elementos da interface deverão manter sua organização e legibilidade nos navegadores testados.
- A aplicação deverá permitir sua execução nos sistemas operacionais Linux, macOS e Windows, respeitando os requisitos de instalação definidos para o projeto.

---

### RNF-007 — Acessibilidade

O sistema deverá apresentar uma interface que facilite a utilização por pessoas com diferentes necessidades, considerando aspectos como legibilidade dos textos, organização dos elementos visuais e facilidade de navegação.

Os campos dos formulários deverão possuir identificação adequada, permitindo que o usuário compreenda quais informações precisam ser preenchidas.

Os principais elementos de navegação e interação deverão permitir utilização por teclado, e a apresentação visual deverá respeitar critérios de contraste, legibilidade e visibilidade do foco.

Como referência para o desenvolvimento e a avaliação da acessibilidade, deverão ser utilizadas as diretrizes WCAG 2.2, nível AA.

**Métricas:**

- 100% dos campos de formulário deverão possuir identificação ou rótulos que permitam compreender sua finalidade.
- Os principais elementos de navegação e interação deverão poder ser utilizados por meio do teclado.
- Os textos comuns deverão apresentar contraste mínimo de 4,5:1 em relação ao fundo.
- Textos grandes e elementos gráficos essenciais deverão apresentar contraste mínimo de 3:1, conforme os critérios aplicáveis da WCAG 2.2.
- Os principais componentes interativos deverão apresentar indicação visual de foco durante a navegação por teclado.
- Os elementos que recebem foco não deverão ficar totalmente encobertos por conteúdos criados pela própria página.
- Os alvos de interação deverão respeitar os critérios de tamanho mínimo e espaçamento estabelecidos pela WCAG 2.2, nível AA.

---

### RNF-008 — Integridade dos Dados

O sistema deverá preservar a integridade das informações armazenadas no banco de dados, garantindo que os registros respeitem as regras de negócio e os relacionamentos definidos para o projeto.

A aplicação deverá utilizar um banco de dados relacional, mantendo os relacionamentos entre usuários, projetos, backlogs, histórias de usuário, épicos e critérios de aceitação de acordo com o modelo físico do sistema.

As regras de associação e as restrições de cada entidade deverão ser verificadas durante as operações realizadas pela aplicação, evitando a criação de registros inválidos ou inconsistentes.

**Métricas:**

- 100% dos relacionamentos definidos no modelo físico do banco de dados deverão respeitar as restrições de integridade referencial.
- Nenhuma operação deverá gerar registros com associações incompatíveis com as regras de negócio.
- 100% dos testes de validação deverão impedir a inserção de dados que violem as restrições e regras de negócio implementadas.
- As operações de criação, atualização e exclusão deverão preservar a consistência dos dados armazenados.

## 4. Requisitos de Interface

### 4.1. Interface com o Usuário

O Backlog Manager deverá disponibilizar uma interface gráfica por meio da qual os usuários possam acessar e utilizar as funcionalidades do sistema.

A aplicação será desenvolvida como um site, acessível por meio de navegadores, utilizando HTML5, CSS3 e JavaScript para a estruturação, apresentação e interação dos elementos da interface.

As páginas deverão ser renderizadas no servidor por meio de templates Jinja2 integrados à aplicação Flask. A navegação utilizará páginas e formulários HTML tradicionais, sem exigir a implementação de uma Single Page Application (SPA).

A interface deverá ser apresentada em português brasileiro e contemplar as seguintes áreas:

- **Autenticação:** página utilizada para que o usuário informe suas credenciais e acesse sua conta.
- **Cadastro:** página destinada à criação de uma nova conta.
- **Painel principal:** área que funciona como ponto de acesso às funcionalidades disponíveis.
- **Listagem de projetos:** página que apresenta os projetos vinculados à conta do usuário.
- **Detalhamento do projeto:** página que reúne as funcionalidades de gerenciamento dos backlogs, histórias de usuário, épicos, critérios de aceitação e mecanismos de priorização.

Os principais elementos da interface deverão incluir formulários, campos de entrada, botões, cartões de histórias de usuário, abas de navegação, componentes modais, mensagens de retorno e elementos de priorização.

A navegação e o envio de informações deverão seguir os mecanismos definidos na arquitetura:

- O método GET deverá ser utilizado para navegação e consulta de informações.
- O método POST deverá ser utilizado para operações de criação, atualização e exclusão.
- Após operações realizadas por POST, deverá ser utilizado o padrão Post-Redirect-Get (PRG).
- As mensagens de retorno deverão utilizar o mecanismo de flash messages do Flask.

A interface deverá adaptar sua organização a diferentes tamanhos de tela, permitindo sua utilização em computadores, tablets e celulares, por meio de CSS responsivo.

Como referência para os testes de apresentação, deverão ser consideradas as seguintes resoluções:

- 360 × 640 pixels — dispositivos móveis.
- 1366 × 768 pixels — computadores.

A tipografia principal deverá utilizar a fonte Inter, disponibilizada pelo Google Fonts, com uma família sans-serif como alternativa caso o recurso externo não esteja disponível.

Os requisitos específicos de organização, disposição dos elementos, navegação e sequência das telas deverão ser representados no documento de Projeto de Interface com o Usuário, por meio de storyboards e wireframes.

### 4.2. Interface com Dispositivos Externos

O Backlog Manager será utilizado por meio de um navegador web e não possui necessidade de comunicação direta com dispositivos físicos externos para executar as funcionalidades previstas.

A aplicação não dependerá de equipamentos específicos, sensores, impressoras, leitores ou outros dispositivos externos.

Os computadores e dispositivos móveis utilizados pelos usuários deverão possuir um navegador compatível e conexão de rede para acessar o servidor da aplicação.

### 4.3. Interface com Outros Sistemas

A arquitetura atual do Backlog Manager não prevê integração com APIs externas, compartilhamento de bancos de dados ou comunicação com outros sistemas de gerenciamento de projetos.

Os dados deverão permanecer armazenados em um único banco de dados relacional, responsável pela persistência das informações dos usuários, projetos e demais entidades do sistema.

A comunicação entre os componentes internos deverá ocorrer da seguinte maneira:

- **Frontend e backend:** comunicação por meio de requisições HTTP, formulários HTML e renderização de páginas pelo Flask utilizando templates Jinja2.
- **Backend e banco de dados:** acesso e persistência dos dados por meio do SQLAlchemy e do Flask-SQLAlchemy.
- **Navegador e aplicação:** acesso às páginas e funcionalidades por meio das rotas disponibilizadas pelo servidor Flask.

O Google Fonts será utilizado para disponibilizar a tipografia Inter na interface. Esse recurso não representa uma integração de negócio com outro sistema, mas uma dependência externa de apresentação visual.

Caso o recurso de fontes externas não esteja disponível, a interface deverá utilizar uma fonte sans-serif alternativa, preservando sua legibilidade e organização.

## 5. Normas, Leis e Padrões Aplicáveis

### 5.1. Proteção de Dados Pessoais

O Backlog Manager deverá observar as disposições da Lei nº 13.709/2018 — Lei Geral de Proteção de Dados Pessoais (LGPD), considerando que o sistema realiza o cadastro de usuários e armazena informações relacionadas às suas contas.

O tratamento das informações deverá respeitar as finalidades necessárias ao funcionamento do sistema, principalmente a criação de contas, a autenticação dos usuários e o gerenciamento dos projetos.

O sistema deverá coletar e armazenar somente as informações necessárias para disponibilizar suas funcionalidades, evitando a coleta de dados pessoais que não tenham finalidade relacionada à aplicação.

As informações das contas deverão ser protegidas contra acessos não autorizados, e os dados de cada usuário deverão permanecer restritos aos projetos vinculados à sua própria conta.

As senhas deverão ser armazenadas por meio de hash criptográfico, conforme estabelecido na arquitetura do backend.

Os dados utilizados durante o desenvolvimento e os testes deverão ser fictícios, evitando a utilização desnecessária de informações pessoais reais.

### 5.2. Marco Civil da Internet

Por se tratar de uma aplicação web, o desenvolvimento e a disponibilização do Backlog Manager deverão considerar as disposições aplicáveis da Lei nº 12.965/2014, conhecida como Marco Civil da Internet.

A utilização da aplicação deverá respeitar os princípios relacionados à privacidade, à proteção de dados pessoais e à segurança das informações transmitidas e armazenadas.

### 5.3. Acessibilidade

A interface deverá adotar como referência as diretrizes WCAG 2.2, nível AA, para orientar aspectos relacionados ao contraste, à identificação dos elementos, à legibilidade, à navegação por teclado, à visibilidade do foco e às dimensões dos elementos interativos.

Essas diretrizes deverão orientar o desenvolvimento e a avaliação dos componentes da interface, considerando tanto a utilização em computadores quanto em dispositivos móveis.

## 6. Restrições de Projeto (Design)

O desenvolvimento do Backlog Manager deverá respeitar as regras de negócio, as decisões arquiteturais e as tecnologias estabelecidas nos documentos do projeto.

As restrições descritas nesta seção deverão ser consideradas durante a implementação das funcionalidades, da interface, da lógica de negócios e da persistência dos dados.

### 6.1. Tecnologias e Ferramentas

O sistema deverá utilizar as tecnologias e ferramentas estabelecidas no Caderno de Arquitetura e nos documentos de implementação.

**Backend:**

- **Python 3.10 ou superior:** linguagem utilizada no desenvolvimento da aplicação.
- **Flask 3.1.3:** framework utilizado para implementar o backend.
- **Flask-SQLAlchemy 3.1.1:** extensão utilizada para integrar o Flask ao SQLAlchemy.
- **SQLAlchemy 2.0.54:** ferramenta utilizada para mapeamento objeto-relacional e acesso ao banco de dados.
- **Flask-Login:** extensão utilizada para gerenciamento das sessões e autenticação dos usuários.
- **Werkzeug 3.1.8:** biblioteca utilizada, entre outras finalidades, para recursos relacionados à segurança e ao tratamento de senhas.
- **Pytest:** ferramenta utilizada para execução dos testes automatizados.

**Frontend:**

- **HTML5:** utilizado para estruturar as páginas e os componentes da interface.
- **CSS3:** utilizado para definir a apresentação visual e a organização dos elementos.
- **JavaScript:** utilizado para implementar interações dinâmicas no navegador.
- **Jinja2:** utilizado para renderizar os templates HTML no servidor.
- **Google Fonts (Inter):** recurso utilizado para disponibilizar a tipografia principal da interface.

As dependências utilizadas deverão permanecer registradas no arquivo `requirements.txt`, permitindo a configuração e a reprodução do ambiente de execução.

### 6.2. Organização da Arquitetura

O backend deverá seguir a arquitetura em três camadas definida pelo grupo:

- **Rotas (routes):** responsáveis pelo recebimento das requisições, extração dos dados e encaminhamento das operações aos serviços.
- **Serviços (services):** responsáveis pela implementação das regras de negócio, validações, cálculos e tratamento das operações.
- **Modelos (models):** responsáveis pela representação das entidades e pela persistência dos dados no banco de dados.

As regras de negócio deverão permanecer concentradas na camada de serviços, evitando que sejam implementadas diretamente nas rotas ou na interface.

O frontend deverá manter a organização entre templates HTML, arquivos CSS e arquivos JavaScript, permitindo a separação entre estrutura, apresentação e interações.

A renderização das páginas deverá utilizar Jinja2, mantendo a abordagem de aplicação web baseada em páginas servidas pelo backend, sem exigir a estruturação do sistema como uma SPA.

### 6.3. Banco de Dados e Persistência

O sistema deverá utilizar um banco de dados relacional para armazenar as informações dos usuários, projetos e demais entidades do Backlog Manager.

No ambiente de desenvolvimento e no protótipo acadêmico, será utilizado SQLite, integrado à aplicação por meio do Flask-SQLAlchemy e do SQLAlchemy.

A utilização do ORM deverá permitir que as entidades sejam representadas por classes Python, reduzindo a dependência da aplicação em relação a comandos específicos de um único sistema gerenciador de banco de dados.

A arquitetura deverá permitir a utilização de outros SGBDs relacionais, como PostgreSQL ou MySQL, mediante alteração da configuração da URI de conexão.

O acesso aos dados deverá ocorrer por meio da camada de modelos e das operações organizadas nos serviços da aplicação.

Os testes automatizados deverão utilizar uma configuração de banco de dados separada da base utilizada na execução normal, evitando que operações de teste interfiram nos dados do protótipo.

### 6.4. Regras de Acesso e Gerenciamento

O sistema deverá respeitar as seguintes regras:

- Cada usuário deverá ter acesso somente aos projetos vinculados à sua própria conta.
- Todos os usuários autenticados deverão possuir acesso às mesmas funcionalidades, sem distinção de tipos ou níveis de usuário.
- Cada projeto poderá possuir, no máximo, um Product Backlog.
- Um projeto poderá possuir vários Sprint Backlogs.
- Uma nova história de usuário deverá ser inicialmente associada ao Product Backlog do projeto correspondente.
- Uma história de usuário deverá estar vinculada a apenas um backlog por vez, podendo ser movimentada entre o Product Backlog e os Sprint Backlogs do mesmo projeto.
- Os vínculos entre histórias de usuário e épicos deverão respeitar a organização definida para os requisitos do projeto.
- Os critérios de aceitação deverão permanecer associados às respectivas histórias de usuário.

### 6.5. Exclusão de Registros

A exclusão de registros deverá ser permanente. Os registros excluídos serão removidos do banco de dados e não poderão ser recuperados por meio de uma funcionalidade de restauração.

Caso um registro excluído seja necessário novamente, deverá ser criado um novo registro.

Para preservar a integridade dos dados e evitar exclusões acidentais, o sistema não deverá excluir automaticamente registros dependentes quando um registro principal for removido.

Quando um registro possuir outros registros vinculados, sua exclusão deverá ser bloqueada até que os registros dependentes sejam removidos pelo usuário.

Por exemplo, um projeto que possua backlogs e histórias de usuário vinculados somente poderá ser excluído depois da remoção desses registros relacionados.

### 6.6. Estimativa por Story Points

O sistema deverá aceitar somente os valores de Story Points definidos para o projeto:

**0, 1, 2, 3, 5, 8, 13, 21, 34 e 55.**

Valores diferentes dos apresentados não deverão ser aceitos para a estimativa das histórias de usuário.

As validações deverão ocorrer na camada de serviços, garantindo que as regras sejam respeitadas independentemente da forma de interação com a interface.

### 6.7. Priorização MoSCoW

O sistema deverá utilizar as seguintes categorias para classificação das histórias de usuário:

- **M — Must Have:** requisito indispensável.
- **S — Should Have:** requisito importante, mas que não é indispensável.
- **C — Could Have:** requisito desejável, cuja ausência não compromete o funcionamento principal.
- **W — Won't Have:** requisito que não será desenvolvido no escopo da entrega ou do ciclo considerado.

As classificações deverão respeitar os valores definidos para o método MoSCoW, não permitindo categorias diferentes das estabelecidas.

### 6.8. Priorização RICE

O sistema deverá utilizar os seguintes parâmetros para o cálculo da pontuação RICE:

- **Reach:** quantidade de usuários alcançados.
- **Impact:** valores possíveis de 3, 2, 1, 0.5 e 0.25.
- **Confidence:** valores possíveis de 100%, 80% e 50%.
- **Effort:** esforço estimado em Story Points.

A fórmula utilizada deverá ser:

**RICE = (Reach × Impact × Confidence) / Effort**

As validações e o cálculo deverão ser realizados na camada de serviços do backend. A interface poderá utilizar JavaScript para apresentar uma prévia dinâmica do resultado ao usuário, mantendo o cálculo definitivo e suas validações sob responsabilidade do backend.

O valor zero continuará permitido como estimativa de Story Points. Entretanto, como a fórmula RICE não permite divisão por zero, histórias com Effort igual a zero não deverão receber uma pontuação RICE calculada.

Nessa situação, o sistema deverá informar ao usuário que é necessário utilizar um valor de esforço maior que zero para realizar o cálculo.

## 7. Aspectos de Licenciamento

O desenvolvimento do Backlog Manager deverá respeitar as condições de licenciamento dos componentes de software utilizados, incluindo frameworks, bibliotecas, ferramentas, dependências e recursos visuais.

As tecnologias utilizadas no projeto possuem as seguintes licenças:

| Componente | Licença |
|---|---|
| Python | Python Software Foundation License (PSF-2.0) |
| Flask | BSD 3-Clause |
| Flask-SQLAlchemy | BSD 3-Clause |
| SQLAlchemy | MIT |
| Flask-Login | MIT |
| Werkzeug | BSD 3-Clause |
| Jinja2 | BSD 3-Clause |
| Pytest | MIT |
| SQLite | Domínio público |
| Fonte Inter | SIL Open Font License 1.1 |

O código original desenvolvido pelos integrantes da equipe permanecerá sob autoria de seus respectivos autores. Para a entrega acadêmica, sua utilização estará vinculada à avaliação e ao desenvolvimento do trabalho da disciplina, sem atribuição de uma licença aberta de redistribuição ao projeto.

Os componentes de terceiros deverão manter suas respectivas condições de licenciamento. Quando houver redistribuição de bibliotecas ou recursos externos, deverão ser preservados os avisos de direitos autorais e as condições de atribuição exigidas por suas licenças.

Os arquivos SVG de identidade visual desenvolvidos especificamente para o Backlog Manager serão considerados recursos próprios do projeto. Materiais visuais externos eventualmente utilizados deverão respeitar as respectivas condições de uso.

## 8. Requisitos de Documentação

A documentação do Backlog Manager deverá permitir que os integrantes da equipe compreendam o funcionamento do sistema, sua organização, seus requisitos e os procedimentos necessários para sua utilização, manutenção e implantação.

A documentação deverá manter uma organização padronizada, com identificação dos artefatos, responsáveis pela elaboração e informações suficientes para sua compreensão.

### 8.1. Documentação do Projeto

O projeto deverá possuir os seguintes artefatos:

1. **Descrição do processo de gerenciamento:** documento contendo informações sobre o quadro Kanban, suas colunas, os cartões utilizados, os responsáveis e o fluxo de gerenciamento das atividades.
2. **Documento de visão e escopo (Vision):** documento que apresenta o problema, os objetivos, as partes interessadas, as funcionalidades e os limites do Backlog Manager.
3. **Requisitos não funcionais (System-wide Requirements):** documento que apresenta os atributos de qualidade, interfaces, restrições, normas e características gerais do sistema.
4. **Histórias de usuário (User Stories):** documento que especifica os requisitos funcionais sob a perspectiva dos usuários.
5. **Caderno de arquitetura (Architecture Notebook):** documento que apresenta as decisões arquiteturais, tecnologias, dependências, mecanismos, abstrações e perspectivas do sistema.
6. **Projeto de interface com o usuário:** documento visual composto por storyboards e wireframes que representam os cenários de utilização e as telas da aplicação.
7. **Projeto físico do banco de dados:** documento composto por diagrama e descrição textual das tabelas, colunas, tipos, chaves, relacionamentos e restrições.
8. **Protótipo e vídeo de demonstração:** aplicação funcional acompanhada de vídeo que demonstre testes de sistema e cenários de sucesso das funcionalidades implementadas.
9. **Infraestrutura de implantação:** documento que apresenta os requisitos de hardware, software e serviços necessários à execução e disponibilização do sistema.

### 8.2. Documentação Técnica

Além dos artefatos do projeto, deverão ser disponibilizadas instruções suficientes para orientar a configuração, execução e manutenção da aplicação.

A documentação técnica deverá contemplar:

- **Instalação do ambiente:** instruções para instalar Python, criar e ativar o ambiente virtual e instalar as dependências registradas no `requirements.txt`.
- **Execução da aplicação:** instruções para iniciar o servidor Flask e acessar o sistema pelo navegador.
- **Dependências:** descrição das tecnologias, bibliotecas, frameworks e respectivas versões utilizadas.
- **Backend:** descrição da organização das rotas, serviços, modelos, regras de negócio e mecanismos de tratamento de erros.
- **Frontend:** descrição da organização dos templates, arquivos CSS, JavaScript e principais componentes da interface.
- **Banco de dados:** descrição das tabelas, relacionamentos, mecanismos de persistência e procedimentos de configuração do SQLite.
- **Testes:** instruções para executar a suíte de testes automatizados utilizando Pytest.
- **Implantação:** instruções necessárias para executar o protótipo e configurar o ambiente de hospedagem definido para o sistema.
- **Utilização do sistema:** orientações para criação de conta, autenticação, gerenciamento de projetos, backlogs e histórias de usuário.

### 8.3. Organização e Formato da Documentação

Os documentos deverão apresentar identificação do sistema, título do artefato, responsável pela elaboração e conteúdo organizado de forma a facilitar sua leitura e compreensão.

Os documentos textuais deverão seguir os modelos e orientações estabelecidos pelo professor.

Para a entrega do trabalho, os documentos textuais deverão ser disponibilizados em formato PDF, acompanhados dos demais materiais necessários, incluindo arquivos do projeto, protótipo e vídeo de demonstração.

O código-fonte deverá permanecer organizado em diretórios que identifiquem suas responsabilidades, enquanto os arquivos de configuração e dependências deverão permitir a reprodução do ambiente de execução.

## 9. Considerações sobre a Infraestrutura de Implantação

O protótipo acadêmico do Backlog Manager será executado utilizando o servidor de desenvolvimento disponibilizado pelo Flask, acessível localmente por meio do endereço `http://127.0.0.1:5000`.

O ambiente de desenvolvimento utilizará SQLite como banco de dados, dispensando a instalação de um serviço separado de banco de dados para o funcionamento local.

A execução deverá utilizar um ambiente virtual Python, com as dependências instaladas a partir do arquivo `requirements.txt`.

Os testes automatizados deverão ser executados por meio do Pytest, utilizando uma configuração de banco de dados separada daquela utilizada pelo protótipo.

O servidor embutido do Flask será utilizado exclusivamente para o desenvolvimento e a demonstração acadêmica. Uma implantação pública deverá utilizar um servidor WSGI apropriado, como Gunicorn ou uWSGI, acompanhado de um servidor de proxy reverso, como Nginx, e comunicação HTTPS.

Para uma implantação em produção, o banco SQLite poderá ser substituído por PostgreSQL ou MySQL por meio da alteração da URI de conexão do SQLAlchemy, mantendo a organização da aplicação baseada no ORM.

## 10. Considerações Finais

Os requisitos e critérios apresentados neste documento deverão ser considerados durante o desenvolvimento, a integração e a avaliação do Backlog Manager.

As métricas estabelecidas servirão como referência para verificar se o sistema atende às condições esperadas de utilização, segurança, desempenho, confiabilidade, manutenção, compatibilidade, acessibilidade e integridade dos dados.

As restrições e decisões descritas deverão ser respeitadas nas implementações do frontend, backend e banco de dados, mantendo a consistência entre as funcionalidades implementadas e os requisitos definidos pelo projeto.

Este documento deverá ser utilizado em conjunto com o documento de visão e escopo, as histórias de usuário, o Caderno de Arquitetura, a documentação da implementação do frontend, o projeto físico do banco de dados e a descrição da infraestrutura de implantação.
