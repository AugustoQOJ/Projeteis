As bibliotécas necessárias são matplotlib, e math

A biblioteca de interface escolhida foi Matplotlib, o principal motivo foi devido a sua facilidade de uso, e principalmente pelos seus widgets que já estavam incluídos na biblioteca. Assim como permitindo integração mais simplificada.

Os controles implementados foram slides exclusivamente para o controle de variáveis da trajetória, exceto o botão de lançamento. As caixas de texto são apenas para mostrar informações calculadas de interesse para o usuário.

Exemplo de entrada testada:
Velocidade inicial: 77.5 m/s
Angulo de lançamento: 44.5 m/s
Altura inicial: 25 m
g: 9.8 m/s²

Saídas:
Alcance máximo = 205.57 m
Altura máxima = 175.55 m
Tempo de voo = 11.53 s

As principais dificuldades foram na criação da GUI, primariamente foi problemas de formatação nas saídas de funções, que quando formatada de forma errada acabava gerando error e conflitos no código. Outro problema foi a animação do lançamento, porque na documentação a variável que determina o final da animação ("frames") não foi muito clara e deixou a entender que era só uma entrada para a função que seria repetida por "animação".
