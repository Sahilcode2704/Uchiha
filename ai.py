from google import genai

client = genai.Client(api_key="AIzaSyCqQIbb7XP-aJ-E-sThLLdKB4SJlW1tCB0")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="who are you"
)
print(response)
print(response.text)

def send(content): 
  response = client.models.generate_content(
    model="gemini-2.5-flash", contents=content)
    print(response)
    print(response.text)

send("What is your name")



