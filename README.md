PROGRAMAÇÃO BACK-END (ADS6-EAD - 2/24ED)

## **Controle de Equipamentos de TI**

### **Descrição**
O **Controle de Equipamentos de TI** é uma aplicação web desenvolvida com Django que permite gerenciar um inventário de equipamentos de TI. O sistema implementa funcionalidades de CRUD (Create, Read, Update, Delete) para facilitar o cadastro, consulta, atualização e exclusão de equipamentos como notebooks, monitores, impressoras, entre outros.

---

### **Funcionalidades**
- **Cadastrar Equipamentos**: Adicionar novos equipamentos ao inventário.
- **Listar Equipamentos**: Visualizar todos os equipamentos cadastrados.
- **Editar Equipamentos**: Atualizar informações dos equipamentos existentes.
- **Excluir Equipamentos**: Remover equipamentos do sistema.
- **Campos Disponíveis**:
  - Nome do equipamento
  - Descrição
  - Número de patrimônio
  - Data de aquisição
  - Status (disponível, em uso, em manutenção, descartado)

---

### **Tecnologias Utilizadas**
- **Backend**: Django 4.x
- **Frontend**: Bootstrap 5
- **Banco de Dados**: SQLite (padrão do Django, mas pode ser configurado para outros bancos como PostgreSQL ou MySQL)
- **Linguagem**: Python 3.x

---

### **Requisitos para Instalação**
Certifique-se de que você tem os seguintes itens instalados:
- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, para criar ambientes virtuais isolados)

---

### **Como Instalar e Executar o Projeto**
Siga os passos abaixo para configurar o projeto em sua máquina:

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/controle-equipamentos-ti.git
   cd controle-equipamentos-ti
   ```

2. **Crie um Ambiente Virtual (Opcional, mas Recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

3. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as Migrações do Banco de Dados**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o Servidor**:
   ```bash
   python manage.py runserver
   ```
   Acesse a aplicação no navegador: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### **Como Usar**
1. **Acessar a Aplicação**: Abra o navegador e acesse o link fornecido pelo servidor local.
2. **Cadastrar Equipamentos**: Clique no botão **"Novo Equipamento"** e preencha as informações.
3. **Editar ou Excluir Equipamentos**: Use os botões **"Editar"** ou **"Excluir"** na lista de equipamentos.

---

### **Estrutura de Arquivos**
```plaintext
controle-equipamentos-ti/
├── app_crud/                # Aplicativo do Django que gerencia os equipamentos
│   ├── migrations/          # Migrações do banco de dados
│   ├── templates/           # Arquivos HTML
│   ├── models.py            # Modelos de dados
│   ├── views.py             # Lógica das páginas
│   └── urls.py              # Rotas do app
├── projeto_crud/            # Configurações do projeto Django
│   ├── settings.py          # Configurações globais
│   ├── urls.py              # Rotas do projeto
│   └── wsgi.py              # Arquivo para o servidor web
├── db.sqlite3               # Banco de dados SQLite (gerado após migração)
├── manage.py                # Gerenciador de comandos do Django
├── README.md                # Este arquivo
├── requirements.txt         # Dependências do projeto
└── venv/                    # Ambiente virtual (se criado)
```

---

### **Contribuição**
Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Criar pull requests
