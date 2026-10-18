import os
from openai import OpenAI

if os.getenv("ENVIRONMENT", "dev") == "dev":
    from dotenv import load_dotenv

    load_dotenv()  # 读取项目根目录 .env

client = OpenAI(
    api_key= os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)

print(response.choices[0].message.content)

print(response.model_dump_json())