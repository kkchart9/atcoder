import openai

openai.api_key = ""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "atcoder D問題相当の問題を出してください。"},
    ]
)

print(response["choices"][0]["message"]["content"])