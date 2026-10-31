Para rodar o código você primeiro precisa executar o server.py e depois executar quantos clients quiser utilizando o client.py em terminais diferentes.

Os códigos funcionam da seguinte maneira: O server.py fica permanentemente em modo listening para aguardar as possíveis tentativas de conexão dos clients. Quando um client tenta se conectar com o server, o server cria uma thread 
para se conectar com o client. Dessa maneira, o server "mãe" não precisa parar de escutar por novos clients.

Quando conectado, o server espera requisições do client, nós definimos 3 tipos padrões de mensagens de requisição: "BID 'valor'" para dar um lance, "STATUS" para conferir a quantidade de participantes junto com o valor mais
alto de lance e "SAIR" para fechar a conexão.

Além disso, o client por meio da thread receive_message consegue receber mensagens do server sem tê-las requisitadas, o que se provou útil quando quisemos que o server atualizasse os clients quando um novo valor máximo 
de lancefoi definido.





Known Issues:

Infelizmente, por mais que tenhamos tentado, não conseguimos implementar um timer que acabasse o leilão depois de um tempo e anunciasse um vencedor. No entanto, aprendemos bastante a utilizar sockets e como fazer (na nossa opinião)
os principais usos deles (conectar, escutar ativamente e passivamente, fazer possível com threads o envio e recebimento simultâneo de dados e a conexão de múltiplos clientes). Dito isso, vamos nos empenhar muito mais para a próxima
 APS.
