from openai import OpenAI
import re

client=OpenAI()
messages = [
    {"role":"user","content":"프로그래밍 입문자에게 추천할 언어 3가지를 번호를 매겨서 알려줘."}
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    temperature=0.7,
    max_tokens=300
)

gpt_output = response.choices[0].message.content
print("GPT 응답 원본: \n",gpt_output)

def parse_list_response(text):
    lines = text.strip().splitlines()
    items = []
    for line in lines:
        match = re.match(r"[\s]*[\d\w][\.\)\s-]+(.*)", line)
        if match:
            items.append(match.group(1))
        else:
            items.append(line.strip())
    return items


parsed = parse_list_response(gpt_output)
print("\n추천 언어 목록: \n")
for i, item in enumerate(parsed, start=1):
    print(f"{i}. {item}")
