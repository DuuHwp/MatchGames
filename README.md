# MatchGames
Trabalho Projeto Integrador 2024

Apresentação Breve

  Uma aplicação web desenvolvida em Pyhton, HTML e CSS. Feito para ajudar o usuário a descobrir os requisitos mínimos e recomendados de um jogo e saber se roda ou não em seu computador. Além de fornecer um canal de ajuda para comunicação com o usuário via e-mail

Objetivo

  Evitar que o usuário adquira um jogo no qual o computador dele não tenha o hardware necessário para rodá-lo.

Funcionalidades

 - Escolha um jogo da lista no menu principal.
 - Descubra as requisições mínimas e recomendadas do jogo escolhido.
 - Envie uma mensagem via e-mail para tirar suas dúvidas.

   Passo a passo para rodar a aplicação

Instalação de Dependências

  - Utilize o git do seu computador para poder começar o acesso. Agora insira a seguinte linha no terminal
  - Após isso clone o diretório no git:
```bash
git clone https://github.com/DuuHwp/MatchGames.git
```
 ```bash
ssh -i <caminho>/MatchGames/MGKey.pem ec2-user@52.54.104.182
```
  - Certifique-se de que seu sistema esteja atualizado:
 ```bash
sudo yum update -y
```
  - Instale o pip e o python se necessário:
```bash
sudo yum install python3 python3-pip -y
```
  - Instale o git
```bash
sudo yum install git -y
```
  - Navegue até o diretório do projeto:
```bash
cd MatchGames
```

```bash
cd "Trabalho de Sexta-Feira"
```
  - Certifique-se de que o pip esteja instalado e/ou atualizado
```
python3 -m pip install --upgrade pip
```
  - Instale as dependências necessárias com:
```bash
pip3 install -r requirements.txt
```
  - Execute a aplicação localmente:
```bash
python3 app.py
```
  - A aplicação será carregada no navegador, e você poderá usufruir de suas funcionalidades.
