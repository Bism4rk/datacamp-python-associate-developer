'''

# ...existing code...

def summarize_history(history, llm_config, requests):
    """
    Summarizes the chat history using the LLM.
    Returns a summary string.
    """
    # You can adjust the prompt as needed
    summary_prompt = [
        {"role": "system", "content": "Resuma a seguinte conversa entre usuário e IA de forma concisa, mantendo o contexto importante para futuras respostas."},
        *history
    ]
    headers, payload, llm_api_url = llm_config.get_llm_client(summary_prompt)
    payload['max_tokens'] = 256  # Limit summary length
    response = requests.post(llm_api_url, headers=headers, json=payload)
    summary = response.json()['choices'][0]['message']['content']
    return summary

@app.route('/api', methods=['GET'])
def search():
    # ...existing code...

    save_user_input = unicodedata.normalize('NFC', user_input)
    history.append({"role": "user", "content": save_user_input})

    # --- Summarization logic ---
    MAX_HISTORY = 10
    KEEP_LAST = 2  # Number of latest messages to keep after summary

    if len(history) > MAX_HISTORY:
        try:
            # Exclude system prompt and keep only user/assistant messages for summary
            to_summarize = history[1:-KEEP_LAST] if len(history) > (KEEP_LAST + 1) else history[1:]
            summary = summarize_history(to_summarize, llm_config, requests)
            # New history: system prompt (summary), plus last KEEP_LAST messages
            history = [
                {"role": "system", "content": f"Resumo da conversa até aqui: {summary}"},
                *history[-KEEP_LAST:]
            ]
        except Exception as e:
            print(f"Error summarizing history: {e}")
            # Optionally, continue with full history or handle error

    try:
        with open(history_file_path, "w", encoding="utf-8") as file:
            json.dump({'chat_history': history, 'business': business, 'profile': profile}, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing history file: {e}")
        return "Error saving history", 500

    # ...existing code...

'''