
# To-Do List Manager

Este é um simples gerenciador de tarefas desenvolvido em Python, ideal para estudos e que não depende de bibliotecas externas. A aplicação permite ao usuário gerenciar suas tarefas diárias com as seguintes funcionalidades básicas: adicionar, atualizar, visualizar, completar e deletar tarefas completadas.


## Funções

**1 - Adicionar Tarefa:**
```
    add_task(<lista_de_tarefas>, <nome_da_nova_tarefa>)
```
**2 - Visualizar Tarefas:**
```
    view_tasks(<lista_de_tarefas>)
```
**3 - Atualizar Tarefa:**
```
    update_task(<lista_de_tarefas>, <indice_da_tarefa>, <nome_nome_da_tarefa>)
```
**4 - Completar Tarefa:**
```
    complete_task(<lista_de_tarefas>, <indice_da_tarefa>)
```
**5 - Deletar tarefas completadas:**
```
    delete_completed_tasks(<lista_de_tarefas>)
```


## Como usar

- **Clone o repositório:**
```bash
    git clone https://github.com/brunosenadev/to-do-manager.git
```
- **Navegue até o diretório do projeto:**
```bash
    cd to-do-manager
```
- **Execute o projeto:**
```bash
    python manager.py
```
