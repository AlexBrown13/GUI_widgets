import sys
import requests 
from logger import logger

# Ollama local server
OLLAMA_URL  = "http://localhost:11434"        
# Model to use
MODEL = "llama3" 


# Make sure Ollama is runing
def check_ollama():
    try:
        res = requests.get(f"{OLLAMA_URL}/api/tags", timeout=5)
        if res.status_code == 200:
            models = [m['name'] for m in res.json().get("models", [])]
            logger.info(f"Ollama is running. Available models {models}")
            if not any(MODEL in m for m in models):
                logger.warning(f"Model not found")
                sys.exit(2) 
        else:
            logger.error("Connection to Ollama failed")
            raise ConnectionError()
    except Exception:
        logger.error(f"Ollma is not running or not reachable at {OLLAMA_URL}")
        sys.exit(2)


def ask_ollama(question, history=None):
    PROMPT = f'''
    You are an AI assistant.
    
    User histroy conversation: {history}
    User question: {question}
    '''
    
    try:
        payload = {
            "model": 'llama3.1',
            "prompt": PROMPT,
            "stream": False
        }

        response = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json=payload
        )

        # If Ollama returns 400 or 500 error, this trigger an exception
        response.raise_for_status()
        return response.json().get('response', "").strip()

    except Exception as e:
        print(f"Error {e}")
        logger.error(f"Error communication with Ollama {e}")


def chat_service(question=None):
    try:
        check_ollama()
        answer_ai = ask_ollama(question)

        return answer_ai
    
    except Exception:
        print("Error in connection chat service")


if __name__ == "__main__":
    chat_service()