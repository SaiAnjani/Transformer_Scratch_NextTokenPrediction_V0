import gradio as gr
import torch
import tiktoken
import numpy as np
from model import GPT, GPTConfig  # Changed from train to model

def load_quantized_model():
    model = GPT(GPTConfig())
    quantized_dict = torch.load("gpt_model_quantized.pt")
    
    # Dequantize model
    state_dict = {}
    for key, value in quantized_dict.items():
        if isinstance(value, dict):
            state_dict[key] = torch.tensor(
                value['data'].astype(np.float32) * value['scale']
            )
        else:
            state_dict[key] = value
    
    model.load_state_dict(state_dict)
    model.eval()
    return model

def generate_text(input_text):
    try:
        # Set device
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        
        # Load model
        model = load_quantized_model()
        model = model.to(device)
        
        # Tokenize input
        tokenizer = tiktoken.get_encoding('gpt2')
        input_tokens = torch.tensor([tokenizer.encode(input_text)]).to(device)
        
        # Generate
        with torch.no_grad():
            output_tokens = model.generate(input_tokens, max_new_tokens=10)[0].tolist()
        
        # Decode and return
        generated_text = tokenizer.decode(output_tokens)
        return generated_text
    except Exception as e:
        return f"Error generating text: {e}"

# Create Gradio interface
iface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=5, label="Input Text"),
    outputs=gr.Textbox(lines=10, label="Generated Text"),
    title="Text Generator",
    description="Enter some text and the model will generate a Shakespeare-style continuation.",
    examples=[
        ["To be, or not to be,"],
        ["All the world's a stage, and all the men"],
        ["But soft, what light through yonder"],
        ["Friends, Romans, countrymen,"],
        ["Now is the winter of our discontent"]
    ]
)

# Launch the interface
iface.launch() 