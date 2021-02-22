# chatbot

TensorFlow, Deep Learning e Python: Chatbot Chatboot usando rede neural recorrente

Base de dados para
treinamento: [Cornell Movie--Dialogs Corpus](https://www.cs.cornell.edu/~cristian/Cornell_Movie-Dialogs_Corpus.html)

As sequencias dos IDs indicam um dialogo, nesse caso o ID é representado pela primeira coluna e os separadores são
representados pelos "+++$+++":

    L872 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ Okay -- you're gonna need to learn how to lie.
    L871 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ No
    L870 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ I'm kidding.  You know how sometimes you just become this "persona"?  And you don't know how to quit?
    L869 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ Like my fear of wearing pastels?
    L868 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ The "real you".
    L867 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ What good stuff?
    L866 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ I figured you'd get to the good stuff eventually.
    L865 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ Thank God!  If I had to hear one more story about your coiffure...
    L864 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ Me.  This endless ...blonde babble. I'm like, boring myself.
    L863 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ What crap?
    L862 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ do you listen to this crap?
    L861 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ No...
    L860 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ Then Guillermo says, "If you go any lighter, you're gonna look like an extra on 90210."

No arquivo movie_lines, temos as conversas com seus testos:
    
    L1045 +++$+++ u0 +++$+++ m0 +++$+++ BIANCA +++$+++ They do not!
    L1044 +++$+++ u2 +++$+++ m0 +++$+++ CAMERON +++$+++ They do to!

No arquivo movie_lines, temos a representação dessas conversas utilizando os IDs:

    u0 +++$+++ u2 +++$+++ m0 +++$+++ ['L1044', 'L1045']

OBS: O TensorFlow só funciona no python 64bits e esse projeto foi testado com a versão 3.7 da linguagem.

### Configurações da GPU

Para quem tem placa de vídeo instalada em seu PC é recomentavel a instalação do CUDA
Toolkit: [nvidia cuda-downloads](https://developer.nvidia.com/cuda-downloads)