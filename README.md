# **Objetivo**
**Criar uma Azure Function HTTP em Python que recebe uma URL de imagem, processa para grayscale ou PNG e retorna o resultado.**

## **Pré-requisitos**
- **Azure Functions Core Tools v4**
- **Python 3.12+**
- **VS Code com extensões: Python e Azure Functions**
- **pip instalado**
- **GitHub CLI (gh) opcional para criar repositório)**

## **Criar projeto**
Caminho exemplo:
```bash
cd /mnt/c/Users/tavar/Documents/github/img-to-png-func
func init . --python
```
## **Dependências**

Edite requirements.txt e deixe:
```bash
azure-functions
pillow
requests
```

## **Criar template de função HTTP**
```bash
func new --name process_image --template "HTTP trigger"
Auth level: ANONYMOUS
```
## **Estrutura final esperada:**
```bash
.
├── .gitignore
├── .vscode/extensions.json
├── function_app.py
├── host.json
├── local.settings.json
└── requirements.txt
```

## **Executar local**
```bash
func start
```

## **Teste a função no navegador ou Postman:**
Copiar código
```bash
http://localhost:7071/api/process_image?url=<URL_da_imagem>
```

## **Resultado esperado**
- Imagem retornada em PNG ou grayscale, dependendo do código da function.
- HTTP 400 se a URL não for fornecida ou houver erro no download

<img width="1339" height="456" alt="image" src="https://github.com/user-attachments/assets/8fbea184-ef8e-4978-b2c0-092daf13cabe" />
