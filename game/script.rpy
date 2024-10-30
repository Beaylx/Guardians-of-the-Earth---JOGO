init python:
    CanalizaçãoDePoder = 0
    EscolhasCertas = 0
    SituacaoR = 0

    def addPontos(pontos):
        global EscolhasCertas
        EscolhasCertas += pontos
    
    def Situacao(situacao):
        global SituacaoR
        SituacaoR = situacao
    

define player = Character("Jogador")
define lotte = Character("Charlotte")
define ngm = Character("???")

image lotte normal= "images/Charlotte.png"
image lotte feliz="images/lotte_feliz.png"

image bg1 = "images/quarto.jpeg"
image bg2 =  "images/janela.jpg"
image bg3 =  "images/porta.jpg"
image bg4 =  "images/vizinhanca1.jpg"
image bg4_1 =  "images/vizinhanca2.jpg"
image bg4_2 =  "images/vizinhanca3.jpg"
image bg5 = "images/casa.jpg"
image bg6 = "images/meteoro.jpg"
image bg7 = "images/preto.png"

label start:

    scene bg7 #Colocar o cenário do quarto
    show bg7:
        zoom 9
    with dissolve

    "Você acorda sonolento durante a madrugada."

    scene bg1 #Colocar o cenário do quarto
    show bg1:
        zoom 3
    with dissolve

    "Sentando-se na cama com dificuldade, você coça seus olhos com uma leve sensação de confusão."
    "Nos instantes seguintes, um baruhlo ensurdecedor preenche seus ouvidos, seguido de um imenso clarão invadindo a janela de seu quarto."
    player "Mas o que é isso!?"

    scene bg2 #Colocar o cenário de janela
    show bg2:
        zoom 2.61

    "Você múrmura em desespero, levantando-se da cama com pressa e correndo até a janela, que agora não aprsentava qualquer sinal daquela luz estrenha."
    "Olhando lá para fora, tudo parecia normal, você vê a casa de seus vizinhos, os carros em suas respectivas garagens, tudo normal."
    "Então vocÊ decide ir lá fora averiguar aquela situação."

    scene bg #Voltar pro cenário de quarto
    show bg1:
        zoom 3

    "Você veste um casaco qualquer por cima de seu pijama, coloca suas pantufas de pelinhos e abre a porta do seu quarto com cuidado para não acordar seus pais."

    scene bg3 #Porta da casa
    show bg3:
        zoom 3
    with dissolve

    "Após passar pelos extensos corredores e cruzar a sala de sua casa, você finalmente chega na porta de entrada."
    "Você exita por alguns instantes, mas a sua curiosidade é maior do que qualquer medo."
    "Você abre a porta com cuidado, inicialmente colocando só a sua cabeça para fora."

    scene bg4 #Vizinhança
    show bg4:
        zoom 3
    "Sem surpresas, assim como visto da janela, tudo parecia normal."
    "Curiosa, você coloca seu corpo inteiro para fora."
    "Você não vê nada, porém, sente o ar meio esquisito, como explicar?"
    "Parecia, energético?"
    "Movida por seus impulsos naturais, você decide dar uma volta pelo bairro"

    scene bg4_1 #Vizinhança 2
    show bg4_1:
        zoom 3
    "Mudando para outra rua, você vê ao longe a mesma luminosidade esquisita que clareou sua janela mais cedo."
    player "Está vindo da direção do bairro de Amélia"
    "Amélia é a sua melhor amiga, vocês se conhecem desde que eram bem novinhas, sem dúvidas tem um laço muito forte!"
    "Você começa a correr em direção ao bairro de sua amiga, sua respiração era pesada e seus passos velozes."
    player "Espero que esteja tudo bem!"

    scene bg4_2 #Vizinhança 3
    show bg4_2:
        zoom 3
    "A medida que você se aproximava, a luminosidade ia aumentando, juntamente da estranha energia que pairava no ar."
    "Era bizarro como não havia ninguém nas ruas, como as pessoas não estão vendo isso?!"
    "A medida que sua proximidade com a casa de Amélia aumentava, você percebia que aqule brilho vinha diretamente da casa dela."

    scene bg5 #Casa da Amélia
    show bg5:
        zoom 3.2 
    "Chegando em frente do local, o que você viu foi absurdamente chocante, porém um tanto quanto extraordinário!"
    player "O que diabos é isso..."
    "Você disse boquiaberta."
    "Simplismente, no quintal de Amélia havia um grande meteoro emanando um brilho vermelho nunca visto antes."
    "Você da alguns passo para trás, genuinamente com medo do que aquilo poderia significar."
    "Mas ele possuia uma energia magnética, era convidativo se aproximar daquela grande bola rochosa."
    "Seus lentos passos mudaram de rumo, agora direcionados para frente."
    "Parecia hipinose, seus olhos refletiam o brilho do grande meteoro, é como se ele te chamasse."
    "Perto o suficiente, você estende a sua mão."
    "Prestes a tocar, você pode sentir o calor que a esfera emana, parecia que sua mão queimaria a qualquer instantes."
    "Por fim, você encosta sua palma inteira no meteoro."
    "Instantaneamente, seu corpo se incandesce! você começa a pegar fogo, sentindo a terrível sensação da sua pele derretendo!"
    player "Aahh- Socorro!!!"
    "Você grita em desespero caindo no chão, você se debate na grama desejando cesar o fogo, porém não adianta."
    "Você sente seu corpo queimar e as chamas tomarem conta dele, era como se o fogo entrasse dentro de você aos poucos."
    
    scene bg7 #Cenário preto
    show bg7:
        zoom 9
    with dissolve
    "Debatendo-se incesantemente, você esprime seus olhos, quando bruscamente, tudo para..."
    "Você se sente normal, seu corpo está tranquilo, o calor foi embora..."
    "Então, você deicide abrir os olhos"

    scene bg1 #Quarto
    show bg1:
        zoom 3
    with dissolve

    "Você está novamente em seu quato, deitada no chão."
    player "O QUEE!!"
    "Você se levamnta abruptamente."
    player "O que foi isso?! Foi real demais pra ser um sonho..."
    "Você caminha até a porta de seu quarto com pressa, mas ao tocar na maçaneta, você sente sua mão erradiar aquele calor estranho novamente, porém dessa vez não lhe causa dor."
    player "Oque..."
    "Antes que você pudsses terminar, um cheiro de madeira queimada invade o local e chamas dominam a porta de seu quarto!"
    player "Aaah--"
    "Você cai para trás enquanto agarra seu pulso, você observa a porta queimar em sua frente sem saber o que fazer."
    player "Merda! como eu acabo com isso?!"
    "Você olha pras suas mãos confusa, elas estão levemente avermelhadas e ardendo."
    ngm "Opa... parece que temos um probleminha aqui!"
    "Você ouve umas voz fina vindo de suas costas."


    show lotte feliz: 
        zoom 0.25
        xalign 0.0
        yalign 0.2      #Mostra a bixinha

    with dissolve
    "Instantaneamente, você se vira, se deparando com uma garota aparentemente jovem."

    menu:
    
        "Perguntar quem é ela":
            $ addPontos(0.5)
            
            player "Quem é você??"
            lotte "Meu nome é Chartlotte, é um prazer conhece-la!"

            show lotte #bixnha com uma cara meio nervosa 
        
            lotte "Embora você não seja bem a pessoas que eu esperava... haha"
            lotte "Eu vou ser sua guia, acredite, você vai precisar!"

       
        "Gritar descontroladamente por socorro":
            $ addPontos(-0.5)
            
            player "Aaah-- Mãe!! Pai!!"

            show lotte #bixa com cara de brava

            ngm "Silencio garota! qual o seu problema?"

        
        "Arremessar um livro nela":
            $ addPontos(-1)
            
            "Assustada, sua única reação é pegar o livro que estava mais proximo a você e atirar na direção dela com sua maior força possivel!"
            "Com o movimento rápido de uam de suas mãos, o livro queima e vira cinzas na sua frente"

            show lotte #bixa com cara de tédio

            ngm "Você só pode estar de brincadeira né?"

    
    if EscolhasCertas < 0.5:

        show lotte #com cara de tédio

        lotte "Aah, vamos lá..."
        "Charlotte bufa e revira os olhos tediosamente."
        lotte "Meu nome é Charlotte."
        lotte "E é melhor você ser mais simpática comigo daqui pra frente..."
        lotte "Sou eu que vou te ajudar a dar os primeiros passos com esse seu novo foguinho ai."
        
        show lotte #aqui com cara de brava

        lotte "E eu lhe garanto que eu posso ser bem detestável..."

    else:
        show lotte #normal


    show lotte #normal

    "Charlotte muda seu olhar para a sua porta que ainda está em chamas"
    lotte "Ok, você tem um probleminha ai..."
    "Ela coloca as duas palmas das mãos em seus ombros."

    if EscolhasCertas < 0.5:
        $ CanalizaçãoDePoder = 0
        
        lotte "Aponte suas mãos para o fogo, igual naqueles filmes de super-herói."
        lotte "Pense em uma memória feliz e imagine isso acalmando as chamas, mamão com açúcar!"
        "Você segue o que Charlotte diz, apontando suas mãos para o fogo e se cocentrando na sua melhor memória possível."

        scene bg1 #porta do quarto, apenas, a Lotte não apareçerá.
        show bg1:
            zoom 3 
        
        "Você vê..."

        menu:
        
            "Aquele dia em que você achou 10 reais no chão quando criança e comprou seu pirulito favorito.":
                $ addPontos(-0.5)
                $ Situacao(0)


                "Você se concentra nisso."
                "Foi um momento tão legal, você se lembra de ter voltado para casa tão feliz naquele dia!"
                "Você permanece concentrado nesta memória por um tempo, porém, nada acontece."
                "Você balança suas mãos esperançosamente, porém, o fogo segue ardente na porta de seu quarto."
                player "Não tá funcionando Charlotte!!"
                "Você diz desesperada"

                show lotte #Com cara de tédio

                "Charlotte revira os olhos em desgosto."
                lotte "Você deve ter pensando em algo super superficial! Por isso não funcionou..."
            
            
            "O dia em que você alimentou um animalzinho de rua e ele te seguiu até sua casa, sendo hoje em dia um grande companheiro seu.":
                $ addPontos(0.5)
                $ Situacao(1)

                "A doce memória vem em seus pensamentos."
                "Você lembra do quão grato seu pet parecia naquele momento."
                "Você pensa também em como ele se tornou um membro da família após isso, estabelecendo um grande laço com você e se tornando querido por todos."
                "Seu coração se acalma, se enchendo de amor e fofura."
                "Juntamente a isso, as chamas somem, deixando para trás um pouco de fumaça e um cheiro de madeira queimada no ar."
                
                show lotte #normal

                lotte "Eu falei que era facinho..."
                lotte "Mas devo admitir, você se saiu bem..."

        if SituacaoR == 0:

            show lotte #cara de brava

            lotte "Tenta de novo! To tentando fazer da maneira mais fácil pra você!"
            "Novamente, você vasculha suas memórias em busca de algo."
            "Desta vez, resolve tentar algo mais fofo, como o dia em que você alimentou um animalzinho de rua e ele te seguiu, atualmente sendo o queridinho da casa!"
            player "Tudo bem... lá vou eu!"

            #tira a lotte

            "A doce memória vem em seus pensamentos."
            "Você lembra do quão grato seu pet parecia naquele momento."
            "Você pensa também em como ele se tornou um membro da família após isso, estabelecendo um grande laço com você e se tornando querido por todos."
            "Seu coração se acalma, se enchendo de amor e fofura."
            "Juntamente a isso, as chamas somem, deixando para trás um pouco de fumaça e um cheiro de madeira queimada no ar."
            
            show lotte #normal

            lotte "É isso, você conseguiu!"
    
    else:
        $ CanalizaçãoDePoder = 1
        $ addPontos(0.5)

        lotte "Vamos lá campeã!!"
        "Charlotte coloca a palma das mãos em seus ombros, como se te desse apoio."
        lotte "Primeiro, aponte suas mãos na direção do fogo."
        "Você segue a instrução de Charlotte, estendendo as mãos com as palmas abertas para o fogo."
        lotte "Ok, muito bem!"
        lotte "Agora, fixe o seu olhar no fogo, imagine-se conversando com ele."
        lotte "Nessa conversa, tente convencer o fogo a se acalmar, manipule-o!"

        #A lotte sai de cena

        "Você se concentra, com o olhar fixo no fogo, era como se você falasse mentalmente para ele parar."
        "Você pode nota-lo reduzindo cada vez mais, estava dando certo!"

        show lotte #só para esta frase

        lotte "Muito bem! está dando certo, contínue!"
        "Você se sente encorajada pelas palavras de Charlotte, elas te davam a clareza de que você estava no caminho certo!"
        "Você continua ordenando que o fogo pare! Sem mais delongas, ele some da sua frente, deixando no ar apenas um cheiro de madeira queimada e fumaça."

        show lotte feliz #sorrindo

        lotte "Muito bem! Você acabou de aprender a canalizar o seu poder!"
        "Charlotte diz orgulhosa sorrindo largamente"
        player "Canalizar?"
        "Você pergunta confusa."
        lotte "Sim! Controlar, domar... como quiser chamar!"
        lotte "É o que faz você não encendiar as coisas por aí, haha!"

    scene bg1 #quarto
    show bg1:
        zoom 3
    show lotte #normal

    lotte "Bem, eu tenho muita coisa para te explicar!"
    player "De fato..."
    lotte "Vamos começar com você me dizendo o seu nome, que tal?"
    
    $ NomePlayer = renpy.input("Insira seu nome!")
    $ NomePlayer = NomePlayer.strip()

    if NomePlayer == "":
        $ NomePlayer = "Jogador"

    $ player = Character(NomePlayer)

    player "Meu nome é [NomePlayer], agradeço por me ajudar!"
    
    show lotte feliz #sorrindo

    lotte "Prazer em conhece-la [NomePlayer]!"

    show lotte #pensativa

    lotte "Bem... por onde eu começo?"
    "Charlotte parece pensar po alguns instantes, como se procurasse uma ponta para iniciar um longo assunto"

    show lotte #normal

    lotte "Ok, vamos começar pelo o que eu sou, ou melhor o que nós somos..."
    player "Nós?..."

    show lotte feliz #feliz

    lotte "As quardiãs da terra! minha esquipe!"

    show lotte #normal

    lotte "Nós somos as reponsáveis por proteger este planeta em segredo a muito tempo, existem gerações e gerações de guardiãs..."
    lotte "Bem... existem algumas criaturas alienígenas pelo cosmo, e eu lhe garanto que elas não curten muito os humanos..."
    player "Você tá me dizendo que aliens existem??"

    show lotte feliz #sorrindo

    lotte "Mas é claro que sim!"
    lotte "Eles são classificados em 3 tiers!"
    lotte "O tier 1, são os mais tranquilinhos, fracotes, até um não-guardião eliminaria um desses!"
    lotte "Porém, não são burros, os miseráveis só atacam em bando!"
    lotte "Falando dos tier 2, são os medianos, pra nós não são tão complicados, dependendo da sua habilidade especial podem até dar um trabalinho, mas nada preucupantes!"
            
    show lotte #séria

    lotte "Já para os não-guardiões, são completamente letais..."

    show lotte #normal

    lotte "Sobre os tier 3, são os mais difíceis, só as guardiãs mais fortes dão conta deles sózinhas!"
    player "Você consegue?"
    lotte "Bem... sózinha não! Mas já lidei com um juntamente de uma colega, e já lhe digo, não foi nada facíl, pelo contrário... "

    show lotte #triste

    "O semblante de Charlotte muda instantânemente."
    lotte "Me custou muito caro..."
            
    show lotte #normal

    lotte "Mas não vou entrar em detalhes!"
    lotte "Enfim, além desses três tiers, existem uma galerinha superior aí, os famosos Celestiais..."
    lotte "Um desses só veio para terra uma única vez, a séculos atrás, foi uma catástrofe extremamente destrutiva, muitas guardiãs foram mortas..."

    show lotte #pensativa
    "Charlotte para por alguns segundos, voltando novamente a ter uma expresão pensativa em sua face."

    menu:

        "Perguntar se ela está bem":
            $ addPontos(1)

            "Charlotte te encara com o leve sorriso"
            lotte "Estou sim, afinal, eu nem vivi nessa época..."
            lotte "É só meio triste pensar em todas que se forão, e isso pode acontecer novamente, e aí, é a geração atual que vai ruir..."

            show lotte #normal

            lotte "Enfim, obrigada por perguntar! Agora, onde estávamos?"
            player "VocÊ estava falando sobre os aliens celestias."
            lotte "Aah sim sim."


        "Não perguntar nada, melhor deixa-la quieta":
            $ addPontos(0)

            "Charlotte chacoalha a cabeça como se estivesse espantando seus pensamentos ruins."

            show lotte #normal

    show lotte #normal
    
    lotte "Certo! os Celestiais são terríveis, um deles faz estrago num planeta, dois podem até destruí-lo, já um grupo..."
    "Charlotte faz uma pausa."
    lotte "Um grupo deles dizima galáxias!"
    lotte "São raros eles andarem em bando, mas não é impossível!"
    lotte "Saindo um pouco sobre as gurdiãs, vamos falar de você!"
    player "De mim? o que quer saber sobre mim?"
    lotte "Haha! por enquanto só o seu nome basta [NomePlayer]!"
    lotte "Eu vou é lhe explicar a razão dessa sua nova habilidade ai."
    "Ela aponta para suas mãos."
    "Por um momento você chegou a esquecer do que tinha pra arcar, a preucupação enche seu corpo novamente."
    player "Eu sou uma de vocês agora?"
    lotte "Por enquanto não, mas já é bom ir pensando sobre isso!"
    lotte "Afinal, futuramente essa será uma escolha que você terá que fazer."

    menu: 

        "Espressar interesse em fazer parte das guardiãs":
            $ addPontos(0.5)

            player "Eu adoraria! Parece algo emocionante!"

            show lotte feliz #feliz

            lotte "Eu aprecio a sua coragem! mas é muito perigoso, por isso, pense bem..."

        "Espressar desisteresse em fazer parte das gurdiãs":
            $ addPontos(-0.2)    

            player "Bom, já adiantando, não é bem algo que eu gostaria..."

            show lotte feliz #normal

            lotte "Ah, não é pra qualquer um, então reconheço que pareça assutador."

    show lotte #normal
    
    lotte "Continuando... Você! jovem garotinha, adiquiriu um poder que não estava destinado a você, se bem que..."
    lotte "Na real, talvez estivesse, não pelas nossas superiores, mas pelo própio cosmo, destino..."
    player "Como eu fui acabar com isso então? E com quem essa coisa deveria ficar??"
    lotte "Bem, as gurdiãs superiores escolhem garotas todos os anos para recrutar, pra isso, elas precisam da aprovaçaõ do cosmo..."
    lotte "Aí, na noite da recepção, ele leva a garota escolhida para uma realidade alternativa, para que não haja probelmas."
    lotte "Essa realidade é idêntica a nossa, só que vazia, sem terceiros."
    lotte "Com isso feito, naquela realidade, o cosmo envia um meteoro radioativo, transimissor de dons mágicos elementais, para a casa do recptor."
    player "Então a Amélia..."
    "Você pensa por alguns segundos nessa loucura toda, concluindo que, de alguma forma, você roubou o poder que era pra ser da sua melhor amiga!"
    lotte "Isso! Acho que esse era o nome da outra garota! Você a conhece bem [NomePlayer]?"

    menu: 
    
        "Afirmar":
            $ addPontos(0.5)

            player "Sim, ela é a minha melhor amiga desta a infância, sem dúvida somos muito próximas!"
            
            show lotte #Pensativa

            lotte "Humm, essa conexão, talvez ela possa explicar como você foi parar da realidade de recepção ao invés dela..."

        "Negar":
            $ addPontos(0)

            player "Não, ela é só uma conhecida por morarmos na mesma região."

            show lotte #pensativa

            lotte "Estranho... não faz sentido você ter ido parar da realidade de recepção ao invés dela... " 

    show lotte #normal

    lotte "Bom, não era pra você estar lá de qualquer forma, nós vamos precisar resolver isso..."

    show lotte #séria

    lotte "Escuta [NomePlayer], vou precisar que você venha comigo pra estação das guardiãs."
    lotte "Uma das superiores deseja ver você, para assim decidir o que vai fazer diante a isso tudo."

    if EscolhasCertas >= 2:

        lotte "Como você foi uma pessoa gentíl e demonstrou que eu posso confiar em você, eu vou fazer isso da menira mais tranquila possível."
        lotte "Não vou te forçar a ir, mas se não for, uma hora as superiores irão te procurar..."
        lotte "E elas são bem barra pesada, principalmente quando se trata de falhas."
        lotte "A escolha é sua garota."

        menu:

            "Concordar em ir":
                $ addPontos(1)

                player "Eu vou Charlotte!"
                player "Quero resolver isso também!"

                show lotte feliz #feliz

                lotte "Ótimo!"
                lotte "Vou tentar te ajudar ao máximo nessa..."

                "Charlotte me da um sorriso tranquilizador, o que faz eu me sentir mais confiante enquanto a tudo."
                "Sinto que tenho uma longa aventura pela frente."
                "Continua..."

                scene bg7 #escuro preto
                show bg7:
                    zoom 9
                with dissolve


            "Recusar ir":
                $ addPontos(-0.5)

                player "Eu não posso ir, me desculpa..."

                show lotte #triste

                lotte "Tudo bem... não é algo tão simples de aceitar"
                lotte "Só saiba que, você vai ter que lidar com isso, mais cedo, ou mais tarde."
                lotte "Lhe desejo sorte [NomePlayer]!"
                "Pude sentir um ar de decepção na voz de Charlotte, porém, eu não estou pronta pra isso!"
                "Como eu poderia imaginar algo assim?"
                "Bem... agora só me resta esperar..."
                "Continua..."

                scene bg7 #escuro preto
                show bg7:
                    zoom 9
                with dissolve
    else:

        show lotte #cara séria

        lotte "Não gosto de lidar assim com as pessoas, mas você não me parece do tipo que coopera..."
        lotte "Eu não confio em você o suficiente para te levar de maneira legal, então..."
        lotte "Lamento por isso!"
        "Charlotte espirra um pó rosado e brilhante em seu rosto."
        "Rapidamente a substância invade suas narinas, lhe causado tonturas."
        player "Charlotte... o que é isso?"
        "Eu falo zonza sentido meus olhos pesarem."
        "Eles fecham lentamente, até que a minha ultíma visão seja a feiçaõ séria de Chartlotte."
        
        scene bg7 #escuro preto
        show bg7:
            zoom 9
        with dissolve
        
        "Contínua..."

    return
