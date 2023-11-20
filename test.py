import requests

response = requests.post(
                    url=f"https://cooltang.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2023-06-01-preview",
                    headers={"api-key": "5166ee6959bc4733944925bc3c3f2143"},
                    json={
                        "model": "gpt-35-turbo",
                        "messages": [{'role': 'system', 'content': 'You are an AI assistant that helps people find information.'}, {'role': 'user', 'content': '炖骨头汤海带什么时候放'}],
                        "temperature": 0.7,
                        "top_p": 1.0,
                        "presence_penalty": 0,
                        "frequency_penalty": 0,
                        "n": 1,
                        "user": "user",
                        "max_tokens": 500,
                    }
                )

print(response.text)