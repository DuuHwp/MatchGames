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

Instalação de Dependências

  - Certifique-se de que o Pyhton esteja instalado no seu computador. (De preferência, baixe-o pelo microsoft store)
  - Após isso clone o diretório ->
  - Navegue até o diretório do projeto:
      cd Trabalho-Integrador

  - Crie um ambiente virtual para o projeto e ative-o:
      python -m venv venv
      *source venv/bin/activate # no Linux/macOS
      *venv\Scripts\activate # no Windows

  - Instale as dependências necessárias com:
      pip install -r requirements.txt

Passo a Passo para Rodar a Aplicação

  - Utilize a seguinte URI para conectar com o banco de dados:
      postgresql://postgresaula:PostgresAula123!@postgres-aula.cuebxlhckhcy.us-east-1.rds.amazonaws.com:5432/postgresaula
  - Execute a aplicação localmente:
      python app.py
  - Abra o navegador e acesse github.com/
  - A interface será carregada, e você poderá selecionar o jogo desejado para verificar se a configuração roda em seu computador.
