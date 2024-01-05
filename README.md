# Django To-Do List CRUD Project

Este projeto é uma implementação básica de operações CRUD (Create, Read, Update, Delete) desenvolvido utilizando Django, HTML e Bootstrap, com o objetivo educacional. Ele foi inspirado no tutorial da TreinaWeb, disponível em [Como criar e executar um projeto Django](https://www.youtube.com/watch?v=rwSHQqQWGnI&list=PLZ5WLsqE1WPGPA0Z0H1XB8P6UwgTHOSaf).


<details>
<summary>

## Funcionalidades

</summary>

1. **Listagem de Tarefas:**
   - Página de listagem exibe todas as tarefas, destacando as concluídas.
   - Implementado com `TodoListView`.

2. **Adição de Nova Tarefa:**
   - Página de criação permite adicionar tarefas com título e data limite.
   - Implementado com `TodoCreateView`.

3. **Atualização de Tarefa:**
   - Página de edição permite modificar título e data limite.
   - Implementado com `TodoUpdateView`.

4. **Remoção de Tarefa:**
   - Página de exclusão com confirmação antes de remover a tarefa.
   - Implementado com `TodoDeleteView`.

5. **Marcar Tarefa como Concluída:**
   - URL específica permite marcar tarefa como concluída, registrando data.
   - Implementado com `TodoCompleteView`.

</details>

## Estrutura do Projeto

A estrutura do projeto segue a organização padrão de um projeto Django, com os principais diretórios e arquivos listados abaixo:

    .
    ├── .venv/
    ├── .vscode/
    ├── setup/
    ├── todos/
    │   ├── migrations/
    │   ├── templates/
    │   │   └── todos/
    │   │       ├── base.html
    │   │       ├── todo_confirm_delete.html
    │   │       ├── todo_form.html
    │   │       └── todo_list.html
    │   ├── __pycache__/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── views.py
    │   └── __init__.py
    ├── .env
    ├── .gitattributes
    ├── .gitignore
    ├── db.sqlite3
    ├── estrutura_projeto.txt
    ├── manage.py
    └── README.md

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para fazer um fork do projeto, implementar melhorias e enviar um pull request.
