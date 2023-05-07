from dados import dadosPerguntas
from pergunta import Pergunta
from quiz import Quiz


def main():
    bancoDePerguntas = []

    for dados in dadosPerguntas:
        dadosTexto = dados["texto"]
        dadosResposta = dados["resposta"]
        novaPergunta = Pergunta(dadosTexto, dadosResposta)
        bancoDePerguntas.append(novaPergunta)

    quiz = Quiz(bancoDePerguntas)

    while quiz.perguntaRestando():
        quiz.proximaPergunta()

    print("Você completou o Quiz!")
    print(f"Sua pontuação final foi {quiz.pontos}/{quiz.numeroPergunta}")


if __name__ == "__main__":
    main()
