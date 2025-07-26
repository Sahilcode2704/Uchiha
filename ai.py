from google import genai

client = genai.Client(api_key="AIzaSyCqQIbb7XP-aJ-E-sThLLdKB4SJlW1tCB0")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)