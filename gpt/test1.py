import os
import requests
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

# 환경변수 읽기
secret_key = os.getenv("OPENAI_API_KEY")
api_url = os.getenv("OPENAI_API_URL")

print("Secret Key:", secret_key)
print("API URL:", api_url)


headers = {
    "Authorization": f"Bearer {secret_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o",
    "messages": [
        {"role": "system", "content": "당신은 유능한 조언자입니다."},
        {"role": "user", "content": "신경망이 어떻게 작동하는지 간단한 용어로 설명하세요."}
    ],
    "temperature": 0.7
}

response = requests.post(api_url, headers=headers, json=data)
if response.status_code != 200:
    print("Error:", response.status_code, response.text)
else:
    print(response.json())
