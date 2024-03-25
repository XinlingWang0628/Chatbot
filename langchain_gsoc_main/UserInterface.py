import gradio as gr
import sys
sys.path.append('/Users/xinling/Desktop/chatbot/langchain_gsoc_main/demo.py')
from demo import getAnswer

def predict(question):
    # This is a wrapper function for Gradio
    ans = getAnswer(question)
    # Assuming 'ans' is a string or can be converted to string
    return str(ans)

# Define Gradio Interface
iface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Ask me anything!"),
    outputs=gr.Textbox(label="Answer"),
    title="AI Chatbot",
    description="This is an AI chatbot. Ask it any question."
)

# Launch the interface
iface.launch()
