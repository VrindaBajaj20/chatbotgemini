import google.generativeai as genai
import gradio as gr

# Configure Gemini API
genai.configure(api_key="__")  
model = genai.GenerativeModel("gemini-1.5-pro-latest")  

# Function to interact with Gemini
def chat_with_gemini(user_input):
    response = model.generate_content(user_input)
    return response.text

# Gradio Interface
iface = gr.Interface(
    fn=chat_with_gemini, 
    inputs="text", 
    outputs="text",
    title="Gemini Chatbot",
    description="Chat with Google's Gemini AI",
)

# Launch Gradio app
iface.launch()
