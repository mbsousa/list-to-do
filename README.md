

## Lista de Tarefas

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

### Funcionalidades

- Lista de tarefas
- Adicionar tarefas
- Editar tarefas
- Excluir tarefas

### Contribuição

**Se você gostaria de contribuir, siga estas instruções.**

## Faça um fork do projeto

- Crie sua feature branch (git checkout -b feature/AmazingFeature)
- Faça o commit das suas alterações (git commit -m 'Add some AmazingFeature')
- Faça o push para a branch (git push origin feature/AmazingFeature)
- Abra um Pull Request

### Dicas

- **Mantenha claro e conciso**: Use linguagem simples e evite jargões desnecessários.
- **Formate o texto**: Use markdown para títulos, listas, e código para facilitar a leitura.
- **Atualize conforme necessário**: À medida que seu projeto evolui, não esqueça de atualizar o README.

