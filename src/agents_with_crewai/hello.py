from litellm import completion
import os


def call_gemini():
    response = completion(
        model="gemini/gemini-1.5-flash", 
        messages=[{"role": "user", "content": "who is the founder of crewai framework?"}]
    )
    print(response['choices'][0]['message']['content'])