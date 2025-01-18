# GPT Text Generator

A lightweight GPT implementation trained on custom text data with a Gradio web interface for text generation.

## Project Overview

This project implements a small GPT (Generative Pre-trained Transformer) model that can generate text continuations. The model is quantized to 8-bit precision for efficient deployment and includes a user-friendly web interface built with Gradio.

## Model Architecture

- Base GPT architecture with the following configuration:
  - 12 layers
  - 12 attention heads
  - 768 embedding dimensions
  - 1024 block size (max sequence length)
  - 50,257 vocabulary size (GPT-2 tokenizer)

## Features

- 8-bit quantized weights for reduced model size
- Efficient text generation
- Interactive web interface
- Example prompts for easy testing
- Support for both CPU and GPU inference

## Files Structure 

    project/
    ├── app.py # Gradio interface for the model
    ├── model.py # Model architecture definition
    ├── requirements.txt # Project dependencies
    └── README.md # Project documentation

## Installation

1. Clone the repository
2. Install dependencies:
    pip install -r requirements.txt

## Model Details

- **Tokenizer**: GPT-2 tokenizer (50,257 tokens)
- **Context Window**: 1024 tokens
- **Generation Method**: Top-k sampling with temperature
- **Quantization**: 8-bit integer quantization for efficient storage

## Dependencies

- torch
- gradio
- tiktoken
- numpy
- huggingface-hub

## Deployment

The model is deployed on Hugging Face Spaces with a Gradio interface. Visit [Space URL] to try it out.

## Training

The model was trained on a custom dataset with the following specifications:
    - Batch size: 4
    - Sequence length: 32
    - Learning rate: 3e-4
    - Optimizer: AdamW
    - Steps: 5000

## Limitations

    - Maximum input length: 1024 tokens
    - Generation length: 10 tokens per request
    - Model size optimized for deployment, trading off 


