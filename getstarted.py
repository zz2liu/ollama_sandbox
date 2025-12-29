%pip install ollama

# %%
# streaming the cloud models
import os
from ollama import Client
os.environ["OLLAMA_API_KEY"] = "1c9543fbd8804594b7178af891c5c505.k1GirRwpJuWfCAP77UnIY-KQ"

client = Client(host="https://ollama.com",
    headers={"Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"})

messages = [
    #{"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Write a poem about the sea."}
]

for part in client.chat(
        model="nemotron-3-nano:30b-cloud",gpt-oss:120b", 
        messages=messages, stream=True):
    #print(part.choices[0].delta.get("content", ""), end="", flush=True)
    print(part['message']['content'], end="", flush=True)


# %%
# simple chat
from ollama import chat, ChatResponse
# response: ChatResponse = chat(model='gemma3:1b', messages=[
response: ChatResponse = chat(model='nemotron-3-nano:30b-cloud', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
#print(response['message']['content'])
# or access fields directly from the response object
print(response.message.content)


# %%
# simple streaming chat
stream = chat(
    model='gemma3:1b',
    messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
    stream=True,
)

for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)


# %% 
# generate, embed and other operations
import ollama
ollama.generate(model='gemma3:1b', prompt='Hello, world!').response

models = ollama.list()
ollama.show('gemma3:1b') 
ollama.ps()

res = ollama.embed(
        #model='embeddinggemma', #gemma3 donot have embed
        model='all-minilm',
        input=['The sky is blue because of rayleigh scattering', 'Grass is green because of chlorophyll'])
res.embeddings