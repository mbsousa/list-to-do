

# Projeto: Lista de Tarefas 📑
![exemplo2](https://github.com/user-attachments/assets/5b2e3691-e82e-4ba7-a4f4-dfb304c02d58)

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


