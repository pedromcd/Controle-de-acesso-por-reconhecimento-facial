# 🔐 Sistema de Controle de Acesso com Reconhecimento Facial

Projeto acadêmico da disciplina de **Processamento de Imagens e Sinais** (Ciência da Computação), desenvolvido em Python.  
O sistema utiliza **OpenCV** e **InsightFace (ArcFace)** para reconhecimento facial, controlando o acesso de pessoas cadastradas.

---------------------------------------------------------

## 🚀 Funcionalidades
- 📸 **Cadastro de usuários (enroll.py):**
  - Captura imagens da câmera.
  - Extrai embeddings faciais.
  - Salva no banco SQLite (`face_access.db`).
- 👤 **Reconhecimento em tempo real (recognize.py):**
  - Detecta faces pela câmera.
  - Compara embeddings cadastrados.
  - Exibe **ACESSO (verde)** ou **NEGADO (vermelho)**.
- 🗄 **Banco de dados local:**  
  - Armazena embeddings em SQLite.
- ⚙️ **Configurações:**  
  - Alteração de câmera e threshold em `config.py`.

---------------------------------------------------------

## 🛠 Tecnologias
- [Python 3.10+](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [InsightFace](https://github.com/deepinsight/insightface)
- [ONNX Runtime](https://onnxruntime.ai/)
- [SQLite](https://www.sqlite.org/)

---------------------------------------------------------

## 📦 Instalação

Clone o repositório:

bash
git clone https://github.com/seu-usuario/face-access-control.git
cd face-access-control

---------------------------------------------------------

Crie e ative um ambiente virtual:

python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Windows (CMD)
.\.venv\Scripts\activate.bat

# Linux/Mac
source .venv/bin/activate


Instale as dependências:

pip install -r requirements.txt

---------------------------------------------------------

## ▶️ Como Usar

1. Cadastro de usuário (enroll.py)

Esse script serve para cadastrar novas pessoas no banco de dados.

python enroll.py


Digite o nome da pessoa.

A câmera será aberta.

Pressione C para capturar uma foto do rosto.

Repita 5 vezes, mudando levemente a posição/expressão para aumentar a precisão.

Pressione Q para sair.

O sistema salva os embeddings no banco face_access.db.

---------------------------------------------------------

2. Reconhecimento em tempo real (recognize.py)

Esse script serve para verificar quem tem acesso.

python recognize.py

A câmera será aberta e começará a detectar rostos.

Se a pessoa estiver cadastrada:
A face aparecerá com um retângulo verde e a mensagem ACESSO.

Se a pessoa não estiver cadastrada:
A face aparecerá com um retângulo vermelho e a mensagem NEGADO.

Pressione Q para sair.

---------------------------------------------------------

## ⚙️ Configurações

Arquivo config.py:

THRESHOLD = 0.38   # ajuste de sensibilidade
CAM_INDEX = 0      # índice da câmera (0 = webcam padrão)

Se o sistema estiver reconhecendo errado:
Aumente o threshold (ex.: 0.45) → mais rígido (menos falsos positivos).
Diminua o threshold (ex.: 0.33) → mais permissivo (menos falsos negativos).

---------------------------------------------------------

## 📚 Estrutura do Projeto
face-access-control/
├── config.py         # Configurações gerais
├── db_utils.py       # Funções de banco de dados (SQLite)
├── face_utils.py     # Utilidades de reconhecimento facial
├── enroll.py         # Cadastro de usuários
├── recognize.py      # Reconhecimento em tempo real
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação

---------------------------------------------------------

## 📊 Demonstração Esperada

Usuário cadastrado → caixa verde + "ACESSO".
Usuário não cadastrado → caixa vermelha + "NEGADO".

---------------------------------------------------------
https://github.com/pedromcd/appMaterna/issues/1#issue-2317952478

## 👨‍🎓Autor

Projeto desenvolvido por Pedro Marques Correa Domingues

<div align="left">
<img src="https://github.com/user-attachments/assets/57ec7a4c-1cea-4ceb-ba17-042f896d27c3" alt="Pedro Marques Correa Domingues width="350px"/>
</div>
