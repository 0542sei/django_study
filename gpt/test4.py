from openai import OpenAI

client = OpenAI()

def gpt_chat(prompt_text):
    messages = [
        {"role": "system", "content": "당신은 유능한 조언자입니다."},
        {"role": "user", "content": prompt_text}
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.7,
        max_tokens=300
    )

    reply = response.choices[0].message.content
    return reply.strip()

# 사용자 입력 받고 결과 보여주기
if __name__ == "__main__":
    user_input = input("질문을 입력하세요: ")
    result = gpt_chat(user_input)
    print("\nGPT의 응답:")
    print(result)
