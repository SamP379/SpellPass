from langchain_ollama import OllamaLLM


def get_llama_response(prompt : str) -> str:
    """Generates a response from the llama3.2 LLM using a given prompt."""
    try:
        model = OllamaLLM(model = "llama3.2")
        response = model.invoke(input = prompt)
        return response
    except Exception as error:
        print(f"An error occured: {error}")
        return None