from litellm import completion
import os

os.environ['GEMINI_API_KEY'] = "AIzaSyDhXD9SX9hjzvZai0rh_7QgXm0BDP0al9o"

def call_gemini():
    response = completion(
        model="gemini/gemini-pro", 
        messages=[{"role": "user", "content": "write code for saying hi from LiteLLM"}]
    )
    print(response['choices'][0]['message']['content'])