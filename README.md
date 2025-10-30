# Sistema Django - Projeto do Tutorial

Este é um sistema web feito com Django, desenvolvido com base no seguinte curso do YouTube:

📺 (https://www.youtube.com/watch?v=MsUL3Pgofl4)

## 📚 Sobre o projeto

Este projeto foi construído acompanhando o vídeo acima. Ele cobre desde a criação de um ambiente Django até a construção de funcionalidades básicas de um sistema web.

## ✨ Funcionalidades

Este é um sistema de lista de tarefas (To-Do List) com as seguintes operações:

* **Criação, Leitura, Atualização e Exclusão (CRUD)** de tarefas.
* **Marcação de Tarefas como Concluídas**, registrando a data de finalização.
* **Organização de tarefas** por prazo de entrega (`deadline`).

## 🚀 Tecnologias usadas

* **Python**
* **Django**
* **HTML**
* **CSS**
* **Django Template Language (DTL)** e **Bootstrap 5** para a interface.
* **Django Crispy Forms** para renderização otimizada de formulários.
* **SQLite** (banco de dados padrão do Django)

## 📦 Como rodar o projeto

> É necessário ter o Python e o Django instalados.

1. Clone o repositório ou baixe os arquivos.
2. No terminal, vá até a pasta do projeto e ative seu ambiente virtual (se houver).
3. Rode as migrações:

```bash
python manage.py migrate

python manage.py runserver

Acesse em http://127.0.0.1:8000/
