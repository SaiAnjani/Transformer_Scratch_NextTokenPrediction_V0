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

## Training Logs
        Training for 18 full epochs plus 2480 steps
      Steps per epoch: 2640


      Epoch 1/19
      Loss: 4.8999: 100%|█████████████████████████████████████████████| 2640/2640 [03:33<00:00, 12.36it/s]

      Epoch 1 completed. Average Loss: 5.4756
      Total steps completed: 2640/50000

      Epoch 2/19
      Loss: 4.5167: 100%|█████████████████████████████████████████████| 2640/2640 [03:31<00:00, 12.48it/s]

      Epoch 2 completed. Average Loss: 4.7085
      Total steps completed: 5280/50000

      Epoch 3/19
      Loss: 4.3296: 100%|█████████████████████████████████████████████| 2640/2640 [03:31<00:00, 12.48it/s]

      Epoch 3 completed. Average Loss: 4.4431
      Total steps completed: 7920/50000

      Epoch 4/19
      Loss: 4.2910: 100%|█████████████████████████████████████████████| 2640/2640 [03:30<00:00, 12.52it/s]

      Epoch 4 completed. Average Loss: 4.2576
      Total steps completed: 10560/50000

      Epoch 5/19
      Loss: 4.0824: 100%|█████████████████████████████████████████████| 2640/2640 [03:30<00:00, 12.51it/s]

      Epoch 5 completed. Average Loss: 4.1186
      Total steps completed: 13200/50000

      Epoch 6/19
      Loss: 4.0714: 100%|█████████████████████████████████████████████| 2640/2640 [03:30<00:00, 12.55it/s]

      Epoch 6 completed. Average Loss: 4.0095
      Total steps completed: 15840/50000

      Epoch 7/19
      Loss: 3.9644: 100%|█████████████████████████████████████████████| 2640/2640 [03:30<00:00, 12.55it/s]

      Epoch 7 completed. Average Loss: 3.9413
      Total steps completed: 18480/50000

      Epoch 8/19
      Loss: 3.9114: 100%|█████████████████████████████████████████████| 2640/2640 [03:30<00:00, 12.54it/s]

      Epoch 8 completed. Average Loss: 3.8785
      Total steps completed: 21120/50000

      Epoch 9/19
      Loss: 3.8918: 100%|█████████████████████████████████████████████| 2640/2640 [03:30<00:00, 12.57it/s]

      Epoch 9 completed. Average Loss: 3.8209
      Total steps completed: 23760/50000

      Epoch 10/19
      Loss: 4.0032: 100%|█████████████████████████████████████████████| 2640/2640 [03:34<00:00, 12.30it/s]

      Epoch 10 completed. Average Loss: 3.8591
      Total steps completed: 26400/50000

      Epoch 11/19
      Loss: 3.9065: 100%|█████████████████████████████████████████████| 2640/2640 [03:32<00:00, 12.41it/s]

      Epoch 11 completed. Average Loss: 3.8333
      Total steps completed: 29040/50000

      Epoch 12/19
      Loss: 3.9104: 100%|█████████████████████████████████████████████| 2640/2640 [03:32<00:00, 12.43it/s]

      Epoch 12 completed. Average Loss: 3.7966
      Total steps completed: 31680/50000

      Epoch 13/19
      Loss: 3.7988: 100%|█████████████████████████████████████████████| 2640/2640 [03:30<00:00, 12.55it/s]

      Epoch 13 completed. Average Loss: 3.7541
      Total steps completed: 34320/50000

      Epoch 14/19
      Loss: 3.9110: 100%|█████████████████████████████████████████████| 2640/2640 [03:30<00:00, 12.57it/s]

      Epoch 14 completed. Average Loss: 3.7761
      Total steps completed: 36960/50000

      Epoch 15/19
      Loss: 3.8775: 100%|█████████████████████████████████████████████| 2640/2640 [03:31<00:00, 12.47it/s]

      Epoch 15 completed. Average Loss: 3.7545
      Total steps completed: 39600/50000

      Epoch 16/19
      Loss: 3.8950: 100%|█████████████████████████████████████████████| 2640/2640 [03:33<00:00, 12.39it/s]

      Epoch 16 completed. Average Loss: 3.7358
      Total steps completed: 42240/50000

      Epoch 17/19
      Loss: 3.8693: 100%|█████████████████████████████████████████████| 2640/2640 [03:36<00:00, 12.20it/s]

      Epoch 17 completed. Average Loss: 3.7656
      Total steps completed: 44880/50000

      Epoch 18/19
      Loss: 3.8908: 100%|█████████████████████████████████████████████| 2640/2640 [03:36<00:00, 12.19it/s]

      Epoch 18 completed. Average Loss: 3.7240
      Total steps completed: 47520/50000

      Epoch 19/19
      Loss: 3.2449: 100%|█████████████████████████████████████████████| 2480/2480 [03:23<00:00, 12.17it/s]

      Epoch 19 completed. Average Loss: 3.6901
      Total steps completed: 50000/50000

## Limitations

    - Maximum input length: 1024 tokens
    - Generation length: 10 tokens per request
    - Model size optimized for deployment, trading off 


