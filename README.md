# 🎬 Movie System

> Projeto acadêmico desenvolvido para a disciplina de **Integração de Sistemas** da
> **Universidade de Pernambuco**

---

## 📚 Informações Acadêmicas

* **Disciplina:** Integração de Sistemas
* **Professor:** Caio Bruno Bezerra de Souza

### 👨‍💻 Alunos

* Gabriel Couto
* Gabriel Lopes
* Joserlan Gonçalves
* Pedro Martins

----

# 📌 Visão Geral

O **Movie System** é uma arquitetura baseada em microsserviços para uma plataforma de streaming de filmes e séries, inspirada em soluções modernas utilizadas por grandes empresas do setor.

O sistema foi projetado com foco em:

* Escalabilidade
* Separação de responsabilidades
* Integração entre serviços
* Segurança e autenticação
* Processamento multimídia
* Inteligência Artificial
* Modularização de domínio

---

# 🏗️ Arquitetura do Sistema

A aplicação está dividida em múltiplos serviços independentes, organizados por domínio de negócio.

## 🔗 Diagrama da Arquitetura

[Visualizar Diagrama no Miro](https://miro.com/app/board/uXjVJ7R0wBA=/?utm_source=chatgpt.com)

---

# 🧩 Estrutura dos Módulos

---

# 🔐 Módulo de Acesso

Responsável pela autenticação, gerenciamento de perfis e notificações da plataforma.

---

## 🔑 Serviço de Identidade e Acesso (`/auth`)

Gerencia autenticação e autorização utilizando JWT.

### Endpoints

| Método | Rota             | Descrição                             |
| ------ | ---------------- | ------------------------------------- |
| POST   | `/auth/register` | Cria uma nova conta                   |
| POST   | `/auth/login`    | Realiza autenticação e gera token JWT |
| POST   | `/auth/refresh`  | Renova o token de sessão              |

---

## 👤 Serviço Central de Usuários (`/users`)

Responsável pelos perfis vinculados à conta do usuário.

### Endpoints

| Método | Rota                 | Descrição                |
| ------ | -------------------- | ------------------------ |
| GET    | `/users/me/profiles` | Lista os perfis da conta |
| POST   | `/users/me/profiles` | Cria um novo perfil      |

---

## 🔔 Serviço de Notificações (`/notifications`)

Centraliza notificações e alertas do sistema.

### Endpoints

| Método | Rota                     | Descrição                                                     |
| ------ | ------------------------ | ------------------------------------------------------------- |
| GET    | `/notifications`         | Busca notificações recentes                                   |
| POST   | `/notifications/webhook` | Endpoint interno para disparo de e-mails e push notifications |

---

# 💳 Módulo Financeiro

Responsável pelo gerenciamento de assinaturas e pagamentos.

---

## 💰 Serviço de Assinaturas (`/subscriptions`)

### Endpoints

| Método | Rota                       | Descrição                    |
| ------ | -------------------------- | ---------------------------- |
| GET    | `/subscriptions/plans`     | Lista planos disponíveis     |
| POST   | `/subscriptions/checkout`  | Processa pagamento           |
| GET    | `/subscriptions/me/status` | Retorna status da assinatura |

### 📦 Planos Disponíveis

* Básico
* Padrão
* Premium

### 📄 Status possíveis

* Ativa
* Inadimplente
* Cancelada

---

# 🎥 Camada de Negócio

Camada principal da aplicação responsável pela experiência do usuário.

---

## 🎞️ Serviço de Catálogo (`/catalog`)

Consulta conteúdos disponíveis por região.

### Endpoints

| Método | Rota                        | Descrição                                      |
| ------ | --------------------------- | ---------------------------------------------- |
| GET    | `/catalog/home`             | Retorna trilhas e carrosséis da página inicial |
| GET    | `/catalog/search?q={query}` | Busca filmes e séries                          |

---

## ▶️ Serviço de Reprodução e Legendas (`/player`)

Responsável pela reprodução de mídia e gerenciamento de legendas.

### Endpoints

| Método | Rota                                           | Descrição                    |
| ------ | ---------------------------------------------- | ---------------------------- |
| GET    | `/player/{title_id}/manifest`                  | Retorna manifesto HLS/DASH   |
| GET    | `/player/{title_id}/subtitles?lang={language}` | Retorna legendas do conteúdo |

### 📺 Tecnologias relacionadas

* HLS
* DASH
* VTT
* SRT

---

## 🤖 Serviço de Inteligência Artificial (`/ai`)

Serviço responsável pela geração automática de legendas.

### Endpoints

| Método | Rota             | Descrição                             |
| ------ | ---------------- | ------------------------------------- |
| POST   | `/ai/transcribe` | Recebe áudio e retorna legenda gerada |

### 📥 Entrada

* Arquivos MP3

### 📤 Saída

* Arquivos VTT
* Arquivos SRT

---

## 📢 Serviço de Propagandas (`/ads`)

Sistema integrado a empresas parceiras para anúncios durante reprodução.

### Endpoints

| Método | Rota             | Descrição                           |
| ------ | ---------------- | ----------------------------------- |
| GET    | `/ads/placement` | Retorna anúncio a ser exibido       |
| POST   | `/ads/campaigns` | Cadastro de campanhas publicitárias |

---

# 💾 Módulo de Armazenamento (Backoffice)

Responsável pelo upload, processamento e gerenciamento de mídia.

---

## ☁️ Serviço de Armazenamento (`/storage`)

### Endpoints

| Método | Rota                          | Descrição                        |
| ------ | ----------------------------- | -------------------------------- |
| POST   | `/storage/upload/video`       | Upload de vídeo bruto            |
| POST   | `/storage/upload/metadata`    | Upload de capas e metadados      |
| GET    | `/storage/status/{upload_id}` | Consulta status do processamento |

---

# 🔄 Fluxo Geral do Sistema

```text
Usuário → Auth → Assinatura → Catálogo → Reprodução → Storage
                                    ↓
                                   IA
                                    ↓
                                Legendas
```

---

# 🛡️ Segurança

O sistema utiliza:

* JWT para autenticação
* Tokens de renovação (Refresh Token)
* Comunicação entre microsserviços
* Controle de acesso baseado em sessão

---

# 🚀 Objetivos do Projeto

* Demonstrar integração entre microsserviços
* Simular arquitetura real de streaming
* Aplicar conceitos de APIs REST
* Trabalhar autenticação distribuída
* Explorar escalabilidade modular
* Integrar IA em sistemas multimídia

---

# 🧠 Conceitos Aplicados

* Microsserviços
* APIs REST
* JWT Authentication
* Processamento assíncrono
* Streaming de mídia
* Integração entre serviços
* Inteligência Artificial
* Armazenamento distribuído

---

# 🛠️ Possíveis Tecnologias

## Backend

* Node.js
* NestJS
* Express

## Banco de Dados

* PostgreSQL
* MongoDB
* Redis

## Infraestrutura

* Docker
* Kubernetes
* NGINX

## Streaming

* FFmpeg
* HLS
* DASH

---

# 📌 Considerações Finais

O projeto busca representar uma arquitetura moderna de plataforma de streaming, aplicando conceitos de integração de sistemas, modularização e comunicação distribuída entre serviços independentes.

Além disso, o sistema explora o uso de inteligência artificial para automação de legendas e personalização da experiência do usuário.

---

# 📄 Licença

Projeto acadêmico desenvolvido exclusivamente para fins educacionais na disciplina de Integração de Sistemas da Universidade de Pernambuco.
