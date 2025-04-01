#images and pdf 
import google.generativeai as genai
import gradio as gr
import PIL.Image

# Configure Gemini API
genai.configure(api_key="AIzaSyBG-4wDu6xj90eMsoGHlrRp_yIG2xN5Rek")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Vision model for images/docs

# Function to process input
def chat_with_gemini(user_input, image):
    if image:
        response = model.generate_content([user_input, image])
    else:
        response = model.generate_content(user_input)
    
    return response.text

# Gradio Interface
iface = gr.Interface(
    fn=chat_with_gemini, 
    inputs=[
        gr.Textbox(label="Ask something"), 
        gr.Image(type="pil", label="Upload an Image (Optional)")
    ],
    outputs="text",
    title="Gemini Chatbot with Vision",
    description="Chat with Google's Gemini AI using text or images.",
)

# Launch Gradio app
iface.launch()
