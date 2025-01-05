**Name:** KISHOR K S

**Company:** CODETECH IT SOLUTIONS

**Intern ID:** CT4MTDS40

**Domain:** MACHINE LEARNING

**Duration:** SEPTEMBER 30th, 2024 to JANUARY 30th, 2025.

**Mentor:** MUZAMMIL AHMED

# Ovewview of the Project

## Project: Text to Image Generation Application

<p align="center">
  <img src="https://github.com/user-attachments/assets/082109f2-477c-4132-8a88-1a6f66959187" width="45%" />
  <img src="https://github.com/user-attachments/assets/fff09c75-f220-48ad-aa30-e5c21fa37232" width="45%" />
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/8067cb1e-1858-44ae-8a03-73b9c0c7043c" width="45%" />
  <img src="https://github.com/user-attachments/assets/bc04e840-2efb-4867-94ea-45c6f42d0998" width="45%" />
</p>

### Single Image

<p align="center">
  <img src="https://github.com/user-attachments/assets/95fa8e4a-fce6-40e7-97e2-c8c163c4857c" width="90%" />
</p>


This project is a Text-to-Image Generation Application that allows users to create unique images based on textual prompts using multiple Stable Diffusion models. The application features an interactive web UI, enabling users to choose from a variety of models, enter prompts, and generate AI-driven visuals.


### Features
1. **Model Selection:** Users can select from a range of models, including:
      - CompVis/stable-diffusion-v1-4
      - stabilityai/stable-diffusion-2-1
      - dreamlike-art/dreamlike-diffusion-1.0
      - stabilityai/stable-diffusion-xl-base-1.0
      - dreamlike-art/dreamlike-anime-1.0
      
2. **Customizable Prompts:** Users can input any descriptive prompt to guide image generation, providing a wide array of creative possibilities.

3. **Interactive UI:** Built with HTML, CSS, and JavaScript, the user interface allows:
      - *Real-time Model Selection:* Intuitive buttons allow users to select their desired model.
      - *Prompt Entry:* Users enter their prompts in an enlarged input box with "Enter the prompt" placeholder text.
      - *Backend Processing:* The Flask server manages model loading, image generation, and memory management. It dynamically loads and unloads models as needed to manage GPU memory usage efficiently.

4. **Downloadable Images:** Once generated, images are displayed on the UI with an option to download the high-resolution result.


### Technical Details
 1. **Frameworks and Tools:**
       - **Backend:** Flask and PyTorch are used to handle model loading, prompt processing, and image generation.
       - **Frontend:** HTML, CSS, and JavaScript create a seamless and responsive UI.
       - **Models:** Diffusion models from Hugging Face's Diffusers library power the generation capabilities.
  
  2. **CUDA Memory Management:** Each model unloads automatically after image generation, clearing GPU memory for the next selection.


### Usage
  - Clone the repository.
  - Ensure diffusers, torch, flask, and required CUDA dependencies are installed.
  - Run server.py to start the Flask backend server.
  - Open the index.html file in a browser to interact with the app.

This application provides a straightforward and efficient approach to text-to-image generation with multiple model support, making it an ideal tool for experimentation and creative projects.


