from litellm import completion
import os

os.environ['GEMINI_API_KEY'] = "AIzaSyDhXD9SX9hjzvZai0rh_7QgXm0BDP0al9o"

def call_gemini():
    response = completion(
        model="gemini/gemini-1.5-flash", 
        messages=[{"role": "user", "content": "who is the founder of microsoft"}]
    )
    print(response['choices'][0]['message']['content'])