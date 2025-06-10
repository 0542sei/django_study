from openai import OpenAI

# OpenAI 클라이언트 초기화 (환경변수 또는 직접 키 입력)
client = OpenAI()

# 스트리밍 요청
stream = client.chat.completions.create(
    model="gpt-4o",  # 또는 "gpt-3.5-turbo"
    messages=[
        {"role": "user", "content": "이 답변을 스트리밍으로 출력해줘"}
    ],
    stream=True
)

# 스트리밍 응답 출력
for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end='', flush=True)
