# 📧 Email Automation Microservice

Microserviço responsável por automatizar o envio de e-mails de confirmação a partir de requisições recebidas via **API REST**. 

O projeto foi desenvolvido com foco em organização modular, separação de responsabilidades e escalabilidade futura, simulando um cenário real de melhoria de processos operacionais.

---

## 🎯 Contexto

Em muitos ambientes corporativos, solicitações recebidas por formulários exigem um fluxo manual ineficiente:
* **Leitura manual** de e-mails.
* **Cópia e colagem** de dados entre sistemas.
* **Envio de respostas** padronizadas de forma artesanal.

Este fluxo, além de consumir tempo operacional valioso, é suscetível a erros humanos. Este microserviço automatiza esse processo, reduzindo o esforço manual e aumentando a confiabilidade da operação.

---

## 🧱 Arquitetura

A aplicação segue uma estrutura modular simples e extensível:

**Fluxo de Dados:**
`API Layer (Flask)` ➔ `Service Layer (Email Service)` ➔ `SMTP Provider`

### Separação de Responsabilidades:
* `app.py`: Camada de exposição HTTP (API REST).
* `email_service.py`: Regras de negócio e lógica de envio de e-mail.
* `config.py`: Centralização de configurações e variáveis de ambiente.
* `.env`: Segregação segura de credenciais sensíveis.

---

## 🚀 Tecnologias

* **Python 3**
* **Flask** (Framework Web)
* **SMTP** (Protocolo de envio)
* **python-dotenv** (Gestão de variáveis de ambiente)
* **Git** (Versionamento)

---

## 🔐 Segurança

* Credenciais sensíveis armazenadas exclusivamente em variáveis de ambiente.
* Arquivo `.env` devidamente ignorado via `.gitignore`.
* Estrutura preparada para integração futura com *Secrets Managers* (AWS Secrets Manager, HashiCorp Vault, etc).

---

## 📡 Endpoint

### `POST /submit`

**Corpo da Requisição (JSON):**
```json
{
  "name": "User Name",
  "email": "user@email.com"
}
```
### 📡 Responsabilidades da API
* **Validação básica:** Verificação da integridade dos dados de entrada.
* **Delegação:** Repasse do processamento para a camada de serviço (Email Service).
* **Resposta HTTP:** Retorno de status adequado (Ex: `201 Created` para sucesso ou `400 Bad Request` para erros).

---

## ⚙️ Execução

Para configurar e rodar o projeto em seu ambiente local:

1. **Criar ambiente virtual:**
   ```bash
   python -m venv venv
   ```
2. **Ativar o ambiente:**

- Linux/Mac: source venv/bin/activate

- Windows: venv\Scripts\activate

3. **Instalar dependências:**

```bash
pip install -r requirements.txt
```
3. **Iniciar servidor:**

```Bash
python app.py
```
A aplicação será iniciada em: http://127.0.0.1:5000

## 🧪 Teste Rápido

Você pode validar o funcionamento da API instantaneamente utilizando o `curl` no seu terminal:

```bash
curl -X POST [http://127.0.0.1:5000/submit](http://127.0.0.1:5000/submit) \
-H "Content-Type: application/json" \
-d '{"name":"Teste Operacional","email":"usuario@exemplo.com"}'
```

## 📈 Evoluções Planejadas

Este projeto foi estruturado para permitir expansão sem refatorações drásticas, como:

* **Persistência em banco de dados:** Armazenamento de logs e status de cada envio.
* **Processamento assíncrono (fila):** Integração com Celery ou RabbitMQ para disparos em segundo plano.
* **Logs estruturados:** Implementação de bibliotecas para melhor rastreabilidade.
* **Observabilidade:** Monitoramento de saúde da aplicação (Health Checks).
* **Containerização:** Criação de Dockerfile para padronização de ambiente.
* **Deploy em ambiente cloud:** Preparação para publicação em plataformas como AWS ou Heroku.

---

## 🧠 Decisões Técnicas

* **Estrutura modular:** Organização que facilita a manutenção e evolução do código.
* **Camada de serviço isolada:** A lógica de e-mail é independente da camada HTTP, permitindo testes isolados.
* **Segurança de credenciais:** Uso obrigatório de variáveis de ambiente para proteger dados sensíveis.
* **Prontidão para eventos:** Base técnica preparada para evoluir para uma arquitetura orientada a eventos.

---

## 💼 Valor de Negócio

A automação proposta entrega resultados diretos para a organização:

* **Redução de tempo operacional:** Libera a equipe para focar em tarefas analíticas.
* **Minimização de erro humano:** Garante que os dados do formulário cheguem corretamente ao destinatário.
* **Padronização de comunicação:** Mantém a consistência nas respostas enviadas aos clientes.
* **Escalabilidade:** Capacidade de lidar com aumentos repentinos de demanda sem esforço manual adicional.


