import google.generativeai as genai

def configure_gemini(api_key):
    """
    Configura a conexão com a API do Gemini.

    Args:
        api_key (str): Sua chave de API do Gemini.

    Returns:
        gemini.GeminiClient: O cliente do Gemini configurado.
    """
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    return model

def generate_story(model, prompt):
    """
    Gera uma história usando o Gemini.

    Args:
        client (gemini.GeminiClient): O cliente do Gemini configurado.
        prompt (str): O prompt inicial para a história.
        parameters (dict): Parâmetros opcionais para controlar a geração da história.

    Returns:
        str: O texto da história gerada.
    """

    response = model.generate_content(prompt)
    story = response.text
    return story

def historia_gemini(prompt):
    """
    Gera uma história usando o Gemini.

    Args:
        prompt (str): O prompt inicial para a história.
        parameters (dict, opcional): Parâmetros opcionais para controlar a geração da história.

    Returns:
        str: O texto da história gerada.
    """
    # Substitua "sua_chave_de_api_aqui" pela sua chave de API do Gemini
    api_key = "AIzaSyDXij5Fb_WoIseBzXD_7j4_T6qOyoWM8cg"
    model = configure_gemini(api_key)
    historia_gpt = generate_story(model, prompt)
    return historia_gpt

# # Exemplo de uso
# prompt = "Era uma vez uma princesa que..."
# story = historia_gemini(prompt)
# print(story)
