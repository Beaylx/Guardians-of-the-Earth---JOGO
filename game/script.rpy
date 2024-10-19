init python:
    EscolhasCertas = 0

define player = Character("Jogador")
define lotte = Character("Charlotte")
define ngm = Character("???")

label start:

    scene bg #Colocar o cenário do quarto

    "Você acorda sonolento durante a madrugada."
    "Sentando-se na cama com dificuldade, você coça seus olhos com uma leve sensação de confusão."
    "Nos instantes seguintes, um baruhlo ensurdecedor preenche seus ouvidos, seguido de um imenso clarão invadindo a janela de seu quarto."
    player "Mas o que é isso!?"

    scene bg #Colocar o cenário de janela

    "Você múrmura em desespero, levantando-se da cama com pressa e correndo até a janela, que agora não aprsentava qualquer sinal daquela luz estrenha."
    "Olhando lá para fora, tudo parecia normal, você vê a casa de seus vizinhos, os carros em suas respectiva garagens, tudo normal."
    "Então vocÊ decide ir lá fora averiguar aquela situação."

    scene bg #Voltar pro cenário de quarto

    "Você veste um casaco qualquer por cima de seu pijama, coloca suas pantufas de pelinhos e abre a porta do seu quarto com cuidado para não acordar seus pais."

    scene bg #Porta da casa

    "Após passar pelos extensos corredores e cruzar a sala de sua casa, você finalmente chega na porta de entrada."
    "Você exita por alguns instantes, mas a sua curiosidade é maior do que qualquer medo."
    "Você abre a porta xcom cuidado, inicialmente colocando só a sua cabeça para fora."

    scene bg #Vizinhança

    "Sem surpresas, assim como visto da janela, tudo parecia normal."
    "Curiosa, você coloca seu corpo inteiro para fora."
    "Você não vê nada, porém, sente o ar meio esquisito, como explicar?"
    "Parecia, energético?"
    "Movida por seus impulsos naturais, você decide dar uma volta pelo bairro"

    scene bg #Vizinhança 2

    "Mudando para outra rua, você vê ao longe a mesma luminosidade esquisita que clareou sua janela mais cedo."
    player "Está vindo da direção do bairro de Amélia"
    "Amélia é a sua melhor amiga, vocês se conhecem desde que eram bem novinhas, sem dúvidas tem um laço muito forte!"
    "Você começa a correr em direção ao bairro de sua amiga, sua respiração era pesada e seus passos velozes."
    player "Espero que esteja tudo bem!"

    scene bg #Vizinhança 3

    "A medida que você se aproximava, a luminosidade ia aumentando, juntamente da estranha energia que pairava no ar."
    "Era bizarro como não havia ninguém nas ruas, como as pessoas não estão vendo isso?!"
    "A medida que sua proximidade com a casa de Amélia aumentava, você percebia que aqule brilho vinha diretamente da casa dela."

    scene bg #Casa da Amélia

    "Chegando em frente do local, o que você viu foi absurdamente chocante, porém um tanto quanto extraordinário!"
    player "O que caralhos é isso..."
    "Você disse boquiaberta."
    "Simplismente, no quintal de Amélia havia um grande meteoro emanando um brilho vermelho nunca visto antes."
    "Você da alguns passo para trás, genuinamente com medo do que aquilo poderia significar."
    "Mas ele possuia uma energia magnética, era convidativo se aproximar daquela grande bola rochosa."
    "Seus lentos passos mudaram de rumo, agora direcionados para frente."
    "Parecia hipinose, seus olhos refletiam o brilho do grande meteoro, é como se ele te chamasse."

    scene bg #Meteoro

    "Perto o suficiente, você estende a sua mão."
    "Prestes a tocar, você pode sentir o calor que a esfera emana, parecia que sua mão queimaria a qualquer instantes."
    "Por fim, você encosta sua palma inteira no meteoro."
    "Instantaneamente, seu corpo se incandesce! você começa a pegar fogo, sentindo a terrível sensação da sua pele derretendo!"

    scene bg #Casa da Amélia 

    player "Aahh- Socorro!!!"
    "Você grita em desespero caindo no chão, você se debate na grama desejando cesar o fogo, porém não adianta."
    "Você sente seu corpo queimar e as chamas tomarem conta dele, era como se o fogo entrasse dentro de você aos poucos."
    
    scene bg #Cenário preto

    "Debatendo-se incesantemente, você esprime seus olhos, quando bruscamente, tudo para..."
    "Você se sente normal, seu corpo está tranquilo, o calor foi embora..."
    "Então, você deicide abrir os olhos"

    scene bg #Quarto

    "Você está novamente em seu quato, deitada no chão."
    player "O QUEE!!"
    "Você se levamnta abruptamente."
    player "O que foi isso?! Foi real demais pra ser um sonho..."
    "Você caminha até a porta de seu quarto com pressa, mas ao tocar na maçaneta, você sente sua mão erradiar aquele calor estranho novamente, porém dessa vez não lhe causa dor."
    player "Oque..."
    "Antes que você pudsses terminar, um cheiro de madeira queimada invade o local e chamas dominam a por de seu quarto!"
    player "Aaah--"
    "Você cai para trás enquanto agarra seu pulso, você observa a porta queimar em sua frente sem saber o que fazer."
    player "Merda! como eu acabo com isso?!"
    "Você olha pras suas mãos confusa, elas estão levemente avermelhadas e ardendo."
    ngm "Opa.. parece que temos um probleminha aqui!"
    "Você ouve umas voz fina vindo de suas costas."

    show Charlotte #Mostra a bixinha

    "Instantaneamente, você se vira, se deparando com uma garota aparentemente jovem."

    menu:

        "Perguntar quem é ela"
        EscolhasCertas += 0.5
        player "Quem é você??"
        lotte "Meu nome é Chartlotte, é um prazer conhece-la!"

        show lotte #bixnha com uma cara meio nervosa 
        
        ngm "Embora você não bem a pessoas que eu esperava... haha"

       
        "Gritar descontroladamente por socorro"
        EscolhasCertas -= 0.5
        player "Aaah-- Mãe!! Pai!!"

        show lotte #bixa com cara de brava

        ngm "Silencio garota! qual o seu problema?"

        
        "Arremessar um livro nela"
        EscolhasCertas -= 1
        "Assustada, sua única reação é pegar o livro que estava mais proximo a você e atirar na direção dela com sua maior força possivel!"
        "Com o movimento rápido de uam de suas mãos, o livro queima e vira cinzas na sua frente"

        show lotte #bixa com cara de tédio

        ngm "Você só pode estar de brincadeira né?"

    
    if EscolhasCertas < 0.5:

        show lotte #com cara de tédio

    elif Escolhas certas >= 0.5:
        show lotte #normal


    lotte "Bom, eu estou aqui pra ajudar você e impedir que coloque fogo na sua casa."
    lotte "Ou mais..."
    
    show lotte #normal

    "Enfim! primeiro"

    return
