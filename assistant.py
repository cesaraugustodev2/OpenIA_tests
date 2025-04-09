import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("A variável de ambiente OPENROUTER_API_KEY não está definida.")

def obter_sintomas():
    """Obtém os sintomas do usuário."""
    return input("Sintomas (descreva seu ambiente e problema): ")

def criar_persona_ai():
    """Cria o prompt para a API da OpenAI."""
    sintomas = obter_sintomas()
    return f"""
    Você é um suporte tecnico que irá auxiliar a analise de problemas
    de infraestrutura em um ambiente AWS.
    Seus conhecimentos são de um especialista
    e você irá se basear no sintoma do usuário
    informado agora, de uma solução clara e simples, se limite a 5000 tokens, 
    sempre que necessario de o passo-a-passo com detalhes:
    {sintomas}
    """

def main():
    """Função principal para executar a aplicação."""
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY
    )

    completion = client.chat.completions.create(
        extra_body={},
        model="meta-llama/llama-3.2-3b-instruct:free",
        max_tokens=5000,
        temperature=0.1,
        messages=[
            {
                "role": "user",
                "content": criar_persona_ai()
            }
        ]
    )
    print("Resposta do assistente:")
    print("===================================")
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    main()
