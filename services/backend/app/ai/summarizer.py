import requests
OLLAMA_API_URL="http://host.docker.internal:11434/api/generate"
def summarizer(text:str,max_words:int=150,model:str="llama3.2:latest")-> str:
    if not text.strip():
        return "no content to summarize"

    prompt = f"""
        Summarize the following text into about {max_words} words.
        Keep the summary concise, clear, and in bullet points when possible.

        Text:
        {text[:4000]}  # truncate for token limit
        """

    try:
        response = requests.post(
            OLLAMA_API_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        data=response.json()
        return data.get("response","").strip()

    except Exception as e:
        return f"[Error calling Ollama API: {e}]"

