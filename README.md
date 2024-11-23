# EcoGuard_Backend
Backend desenvolvido para o Hackathon do CEPEDI.

# Como Rodar o Projeto Django

Este guia explica como configurar e executar o projeto Django em sua máquina.

## Pré-requisitos

- **Python 3.8 ou superior** instalado na sua máquina.
- **pip** (gerenciador de pacotes do Python) instalado.
- **Virtualenv** (opcional, mas recomendado para isolar dependências).

---

## Passos para Executar o Projeto

### 1. Clone o Projeto ou Extraia os Arquivos

Certifique-se de que os arquivos do projeto estão no seu computador.

---

### 2. Configure um Ambiente Virtual

Crie um ambiente virtual para evitar conflitos de dependências.

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

---

### 3. Instale as Dependências

Verifique se existe um arquivo `requirements.txt` no diretório do projeto. Se ele existir, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

---

### 4. Configure o Banco de Dados

- **SQLite**: O projeto pode incluir um arquivo `db.sqlite3`. Se ele estiver presente, nenhuma configuração adicional é necessária.
- **Outros Bancos de Dados**: Verifique o arquivo `settings.py` ou um arquivo `.env` para configurar as credenciais de conexão.

Se necessário, configure suas credenciais no arquivo `.env` ou diretamente no arquivo de configurações.

---

### 5. Realize as Migrações

Execute as migrações para configurar as tabelas no banco de dados:

```bash
python manage.py migrate
```

---

### 6. (Opcional) Crie um Superusuário

Se você precisar acessar o painel administrativo, crie um superusuário:

```bash
python manage.py createsuperuser
```

---

### 7. Inicie o Servidor

Rode o servidor de desenvolvimento para testar o projeto:

```bash
python manage.py runserver
```

O servidor estará disponível no navegador em:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Resolvendo Problemas

Se encontrar problemas durante a execução, verifique os logs exibidos no terminal ou entre em contato com o autor do projeto para mais informações.

---
