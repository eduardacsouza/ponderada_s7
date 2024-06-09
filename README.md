# ponderada_s7

## Projeto de Implementação de API para Gestão de Histórias Integrada com ChatGPT
&emsp;Este projeto visa a criação de uma API para a gestão de histórias, com integração à API do ChatGPT para geração automática de conteúdo textual. Abaixo estão os detalhes de cada aspecto do projeto conforme o barema proposto:

### 1. CRUD de Histórias
&emsp; A aplicação oferece operações CRUD (Create, Read, Update, Delete) para gerenciar histórias. Cada história é representada por um modelo que inclui campos como ID e Conteúdo. As operações possibilitam:

**Criação:** Adicionar novas histórias

**Recuperação:** Buscar e visualizar histórias existentes.

**Atualização:** Modificar o conteúdo de histórias existentes.

**Exclusão:** Remover histórias do sistema.

### 2. Integração com a API do ChatGPT
&emsp; A API integra-se à API do ChatGPT para gerar histórias de forma dinâmica. A função create_historia_from_gpt é responsável por utilizar a API do ChatGPT para gerar automaticamente o conteúdo das histórias, facilitando a criação de textos únicos e personalizados.
