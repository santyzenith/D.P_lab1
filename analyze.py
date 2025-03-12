import yaml
from openai import OpenAI

def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)

def get_llm_response(url="https://www.hola.com/horizon/landscape/d1eaad20c4c6-adobestock47432136.jpg",
                     prompt="What is in this image? Anwer in spanish."
                    ):

    config = load_config()
    
    client = OpenAI(
        base_url=config["openai"]["base_url"],
        api_key=config["openai"]["api_key"],
    )
    
    completion = client.chat.completions.create(
      model=config["openai"]["model"],
      messages=[
        {
          "role": "user",
          "content": [
            {
              "type": "text",
              "text": prompt
            },
            {
              "type": "image_url",
              "image_url": {
                "url": url
              }
            }
          ]
        }
      ]
    )
    return completion.choices[0].message.content
    