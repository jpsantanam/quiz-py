class Quiz:

    def __init__(self, listaPergunta):
        self.numeroPergunta = 0
        self.pontos = 0
        self.listaPergunta = listaPergunta

    def perguntaRestando(self):
        return self.numeroPergunta < len(self.listaPergunta)

    def proximaPergunta(self):
        perguntaAtual = self.listaPergunta[self.numeroPergunta]
        self.numeroPergunta += 1
        respostaUsuario = input(f"Pergunta {self.numeroPergunta}: {perguntaAtual.texto}? (Verdadeiro/Falso): ")
        self.verificaResposta(respostaUsuario, perguntaAtual.resposta)

    def verificaResposta(self, respostaUsuario, respostaPergunta):
        if respostaUsuario.lower() == respostaPergunta:
            print("Você acertou!")
            self.pontos += 1
        else:
            print("Você errou!")
        print(f"Sua pontuação: {self.pontos}/{self.numeroPergunta}\n")