import os
from openai import OpenAI

def interact_with_data(crimesData, moneyImages, userInput):

    XAI_API_KEY = "xai-8Tcgc4AfUTIde5o7W4Ennjiko3dpA4ECNeNZqFQYQef2py6iIYac65SxtD2dSJKaqviOlfyR1hPujnGt"

    client = OpenAI(
        api_key=XAI_API_KEY,
        base_url="https://api.x.ai/v1",
    )
    messages = [
        {"role": "system", "content": "You are a chatbot designed to cross-reference public security spending data with crime rates."},
        {"role": "user", "content":  crimesData},
    ]

    base64_prefix = "data:image/png;base64," 

    for base64_image in moneyImages:
        messages.append({
            "role": "user",
            "content": [{"type": "image_url", "image_url": {"url": f"{base64_prefix}{base64_image}"}}]
        })

    messages.append({
        "role": "user",
        "content": userInput
    })

    completion = client.chat.completions.create(
        model="grok-2-vision-1212",
        messages=messages,
    )

    return completion.choices[0].message