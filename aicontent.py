import os
import openai
import config

openai.apy_key = config.openai.api_key

def open_ai_query(query):
    response = openai.Completion.create(
  model="davinci-instruct-beta",
  prompt=query,
  temperature=0.7,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0)
    
    if 'choices' in response:
        if len(response['choices']) > 0:
            answer = response['choices'][0]['text']
        else:
            answer = 'Opps sorry, you beat the AI this time'
    else:
        answer = 'Opps sorry, you beat the AI this time'
    return answer