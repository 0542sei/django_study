from openai import OpenAI

# 환경변수 사용 시 아래 코드로 충분
# client = OpenAI()

# 명시적 API 키 전달 (보안에 유의)
client = OpenAI(api_key=)

# 대화 메시지 정의
messages = [
    {"role": "system", "content": "당신은 유능한 조언자입니다."},
    {"role": "user", "content": "신경망이 어떻게 작동하는지 간단한 용어로 설명하세요."}
]

# GPT-4o 모델 호출
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0.7,
    max_tokens=300
)

# 출력
print(response.choices[0].message.content)
