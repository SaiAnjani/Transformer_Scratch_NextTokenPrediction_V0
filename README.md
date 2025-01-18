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