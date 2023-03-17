import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "atcoder D問題相当の問題を出してください。"},
    ]
)

print(response["choices"][0]["message"]["content"])