

# Projeto: Lista de Tarefas 📑

https://github.com/user-attachments/assets/8d89b7d0-bae1-4ffa-8e53-59dd96a9a1af


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


