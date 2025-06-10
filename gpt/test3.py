from openai import OpenAI

client = OpenAI()

# 대화 메시지 정의
messages = [
    {"role": "system", "content": "당신은 유능한 조언자입니다."},
    {"role": "user", "content": "파이썬으로 JSON 파싱하는 간단한 예제를 알려줘"}
]

# 1. API 요청: GPT-4o 모델 호출
response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0.7,
    max_tokens=50
)

# 2. 응답 JSON 구조 확인
response_json = response.to_dict()

# 3. 응답 내용 추출
gpt_reply = response_json['choices'][0]['message']['content']

# 4. 사용자에게 가공된 결과 표시
print("GPT 응답 결과:")
print(gpt_reply)
