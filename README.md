

# Projeto: Lista de Tarefas 📑
Status: Finalizado ✅


![list](https://github.com/user-attachments/assets/9c4f6411-3aa3-4f7b-be8e-73f10dc874f8)

> Uma aplicação web desenvolvida para gerenciar tarefas de forma simples e eficiente.

## Tecnologias Usadas

- Django
- Python
- Bootstrap
- HTML/CSS

## Instalação e Detalhes

```bash

# Clone o Repositório
git clone https://github.com/mbsousa/listo-to-do.git
cd repositorio

# Crie um Ambiente Virtual
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

# Instale Dependências
pip install -r requirements.txt

# Configuração do Banco de Dados
python manage.py migrate

# Crie Superusuário
python manage.py createsuperuser

# Execute o Servidor
python manage.py runserver

# Acesse a aplicação em http://127.0.0.1:8000/.
```

## Funcionalidades

- Lista de tarefas
- Adicionar tarefas
- Editar tarefas
- Excluir tarefas


