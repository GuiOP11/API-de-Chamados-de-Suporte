# API-de-Chamados-de-Suporte
Abrir chamado Listar chamados Alterar status Fechar chamado

git push origin main
pip install sqlmodel

# API de Chamados de Suporte

API REST desenvolvida em **Python** com **FastAPI** para gerenciamento de chamados de suporte técnico. Permite criar, listar, consultar, atualizar o status e excluir chamados, com persistência de dados em banco **SQLite**.

##  Tecnologias utilizadas

- [Python 3.14](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) — framework para criação de APIs
- [SQLModel](https://sqlmodel.tiangolo.com/) — ORM que une SQLAlchemy + Pydantic
- [SQLite](https://www.sqlite.org/) — banco de dados relacional leve
- [Uvicorn](https://www.uvicorn.org/) — servidor ASGI

##  Funcionalidades

-  Criar chamado
-  Listar todos os chamados
-  Buscar chamado por ID
-  Atualizar status do chamado (Aberto, Em andamento, Fechado)
-  Excluir chamado
-  Persistência de dados em banco SQLite
-  Validação automática de dados de entrada
-  Documentação interativa automática (Swagger)

##  Como executar o projeto

### Pré-requisitos
- Python 3.10 ou superior instalado

### Passo a passo

1. Clone o repositório
```bash
git clone https://github.com/GuiOP11/API-de-Chamados-de-Suporte.git
cd API-de-Chamados-de-Suporte
```

2. Crie e ative um ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Execute a aplicação
```bash
uvicorn main:app --reload
```

5. Acesse a documentação interativa no navegador
```
http://127.0.0.1:8000/docs
```

##  Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Verifica se a API está funcionando |
| POST | `/chamados` | Cria um novo chamado |
| GET | `/chamados` | Lista todos os chamados |
| GET | `/chamados/{id}` | Busca um chamado específico |
| PUT | `/chamados/{id}` | Atualiza o status de um chamado |
| DELETE | `/chamados/{id}` | Exclui um chamado |

### Exemplo de requisição — Criar chamado

**POST** `/chamados`
```json
{
  "usuario": "Guilherme de Oliveira Padilha",
  "problema": "Computador não liga",
  "status": "Aberto"
}
```

**Resposta**
```json
{
  "id": 1,
  "usuario": "Guilherme de Oliveira Padilha",
  "problema": "Computador não liga",
  "status": "Aberto"
}
```

##  Estrutura do projeto

```
api-chamados/
├── main.py            # Código principal da API
├── requirements.txt   # Dependências do projeto
├── chamados.db         # Banco de dados SQLite (gerado automaticamente)
└── README.md
```

##  Próximas melhorias planejadas

- [ ] Autenticação de usuários (JWT)
- [ ] Deploy em ambiente de produção
- [ ] Testes automatizados
- [ ] Filtro de chamados por status

##  Autor

**Guilherme de Oliveira Padilha**
Técnico em Informática pelo IFC Videira (2023–2025) | Estagiário na BRDrive (2025) | Estudante de Ciência da Computação na UNOESC

[LinkedIn](https://www.linkedin.com/in/guilherme-de-oliveira-1ab903396/) · [GitHub](https://github.com/GuiOP11)