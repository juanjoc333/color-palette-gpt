import openai


def get_completion(messages, model="gpt-3.5-turbo", max_tokens=200):
    return openai.ChatCompletion.create(
        model=model, messages=messages, max_tokens=max_tokens
    )
