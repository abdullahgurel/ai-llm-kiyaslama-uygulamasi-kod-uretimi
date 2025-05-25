# helper.py
import ollama

def initialize_clients():
    return {
        'llama': 'llama3',      # Ollama'da `ollama pull llama3` ile yüklenmeli
        'mistral': 'mistral'    # Ollama'da `ollama pull mistral` ile yüklenmeli
    }

def ollama_generate_response(prompt, model_name):
    try:
        response = ollama.chat(
            model=model_name,
            messages=[
                {"role": "system", "content": "Sen uzman bir Python asistanısın."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"{model_name} Hatası: {str(e)}"