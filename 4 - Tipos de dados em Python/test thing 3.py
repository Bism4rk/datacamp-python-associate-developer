
'''
# ...existing code...

def summarize_history(history):
    # Aqui você pode chamar seu modelo LLM para resumir as mensagens anteriores
    # Exemplo simples: concatenar os conteúdos das mensagens anteriores
    # Substitua por uma chamada real ao modelo se desejar
    messages_to_summarize = history[:-5]  # Resumir todas menos as últimas 5
    summary_content = "Resumo: " + " ".join([msg["content"] for msg in messages_to_summarize if msg["role"] == "user"])
    return {"role": "system", "content": summary_content}

@app.route('/api', methods=['GET'])
def search():
    # ...existing code...

    save_user_input = unicodedata.normalize('NFC', user_input)
    history.append({"role": "user", "content": save_user_input})

    # Limitar histórico e resumir se necessário
    if len(history) > 10:
        # Gera resumo das mensagens antigas
        summary_message = summarize_history(history)
        # Mantém o resumo + últimas 5 mensagens
        history = [history[0], summary_message] + history[-5:]

    try:
        with open(history_file_path, "w", encoding="utf-8") as file:
            json.dump({'chat_history': history, 'business': business, 'profile': profile}, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing history file: {e}")
        return "Error saving history", 500

    # ...existing code...
'''