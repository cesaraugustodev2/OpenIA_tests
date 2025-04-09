from assistant import sintomas
def sintomas():
     return input("Sintomas(descreva seu ambiente e problema): ")
def persona_ai():
     return f"""
     Você é um robo que irá auxiliar a analise de problemas
     de infraestrutura em um ambiente  AWS
     seus conhecimentos são de um expecialista 
     e você irá se basear no sintoma do usuário 
     informado agora,de uma solução clara e simples:
    {sintomas}"""
