import openai
# Indica el API Key
openai.api_key = "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"
# Uso de ChapGPT en Python
model_engine = "gpt-3.5-turbo"
prompt = "la suma de 5 mas 5"
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