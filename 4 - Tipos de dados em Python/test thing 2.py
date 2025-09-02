'''
# ...existing code...

def summarize_history(history, llm_config, requests, llm_api_url):
    # Gera um prompt para resumir o histórico
    prompt = "Resuma em poucas frases o seguinte histórico de conversa:\n"
    for msg in history:
        prompt += f"{msg['role']}: {msg['content']}\n"
    # Monta payload para o LLM
    headers, payload, _ = llm_config.get_llm_client([{"role": "user", "content": prompt}])
    response = requests.post(llm_api_url, headers=headers, json=payload)
    summary = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
    return [{"role": "system", "content": summary}]

@app.route('/api', methods=['GET'])
def search():
    # ...existing code...

    save_user_input = unicodedata.normalize('NFC', user_input)
    history.append({"role": "user", "content": save_user_input})

    # Limite de histórico: se exceder 10 mensagens, faz resumo
    MAX_HISTORY = 10
    if len(history) > MAX_HISTORY:
        # Mantém as últimas 2 mensagens do usuário e do modelo
        last_msgs = history[-2:]
        summarized = summarize_history(history[:-2], llm_config, requests, llm_api_url)
        history = summarized + last_msgs

    try:
        with open(history_file_path, "w", encoding="utf-8") as file:
            json.dump({'chat_history': history, 'business': business, 'profile': profile}, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing history file: {e}")
        return "Error saving history", 500

    headers, payload, llm_api_url = llm_config.get_llm_client(history)

    return new_request(headers, payload, history, history_file_path, user_input, user_token, requests, llm_api_url, Response, confirmation, atlas_api)

# ...existing code...
'''