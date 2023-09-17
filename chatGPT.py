import openai
# Indica el API Key
openai.api_key = "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"
# Uso de ChapGPT en Python
model_engine = "gpt-3.5-turbo"
prompt = "quien ha ganado más copas del mundo"
completion = openai.Completion.create(engine=model_engine,
                                    prompt=prompt,
                                    max_tokens=1024,
                                    n=1,
                                    stop=None,
                                    temperature=0.7)
respuesta=""
for choice in completion.choices:
    respuesta=respuesta+choice.text
    print(f"Response: %s" % choice.text)