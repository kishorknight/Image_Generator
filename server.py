from flask import Flask, request, send_file
from flask_cors import CORS  # Add CORS
import torch
from diffusers import DiffusionPipeline, StableDiffusionPipeline
from io import BytesIO
from PIL import Image

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dictionary of available models
MODEL_PATHS = {
    "stable-diffusion-v1-4": "CompVis/stable-diffusion-v1-4",
    "stable-diffusion-2-1": "stabilityai/stable-diffusion-2-1",
    "dreamlike-diffusion-1.0": "dreamlike-art/dreamlike-diffusion-1.0",
    "stable-diffusion-xl-base-1.0": "stabilityai/stable-diffusion-xl-base-1.0",
    "dreamlike-anime-1.0": "dreamlike-art/dreamlike-anime-1.0"
}

def load_pipeline(model_name):
    model_path = MODEL_PATHS[model_name]
    
    if model_path == "stabilityai/stable-diffusion-xl-base-1.0":
        pipeline = DiffusionPipeline.from_pretrained(
            model_path, torch_dtype=torch.float16, use_safetensors=True, variant="fp16"
        ).to("cuda")
    else:
        pipeline = StableDiffusionPipeline.from_pretrained(model_path, torch_dtype=torch.float16).to("cuda")
        
    return pipeline

@app.route("/generate", methods=["POST"])
def generate_image():
    data = request.json
    model_name = data.get("model")
    prompt = data.get("prompt")
    
    # Load the selected model pipeline
    pipeline = load_pipeline(model_name)

    # Generate the image
    with torch.no_grad():
        image = pipeline(prompt).images[0]
    
    # Clear memory and delete pipeline to enable model switching
    del pipeline
    torch.cuda.empty_cache()
    
    # Save image to a BytesIO object to send as a response
    img_io = BytesIO()
    image.save(img_io, "PNG")
    img_io.seek(0)
    
    return send_file(img_io, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)

