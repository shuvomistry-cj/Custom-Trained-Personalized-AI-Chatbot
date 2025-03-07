import google.generativeai as genai

# Replace with your actual API key
genai.configure(api_key="YOUR_GOOGLE_API_KEY")

# List available models
models = genai.list_models()
for model in models:
    print(model.name, "-", model.description)
