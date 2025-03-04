import os  # For interacting with the filesystem (e.g., saving images)
import random  # For randomizing style and color schemes
import torch  # For GPU processing and handling tensors
from diffusers import StableDiffusionPipeline  # To use the pre-trained Stable Diffusion model
from PIL import Image  # For image processing and saving
from torch import autocast  # For automatic precision adjustment to speed up processing
import gradio as gr  # For creating a user-friendly interface


# Set up the device for faster processing (use GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"  # Use GPU if available, otherwise CPU

# Create a directory to store generated images
output_dir = "generated_images"  # Folder name to save generated images
os.makedirs(output_dir, exist_ok=True)  # Create the folder if it doesn't exist

# Load the Stable Diffusion 2.1 model with error handling
try:
    model = StableDiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1",  # Model name
    ).to(device)  # Transfer the model to GPU or CPU based on the device variable
except Exception as e:
    print(f"Error loading the model: {e}")
    model = None  # Set model to None in case of failure


def generate_image(prompt):
    """
    Generate an image from a given text prompt using the Stable Diffusion model.
    
    Args:
        prompt (str): The textual description for generating the image.
        
    Returns:
        PIL.Image or None: The generated image, or None if generation fails.
    """
    if model is None:
        return None

    try:
        # Use autocast to enable mixed precision (automatically choose between 16-bit or 32-bit precision)
        with autocast("cuda" if device == "cuda" else "cpu"):
            result = model(prompt)  # Generate the image from the text prompt
            return result.images[0]  # Return the generated image
    except Exception as e:
        print(f"Error generating image: {e}")
        return None


def customize_image(image, color_scheme="bright"):
    """
    Customize the appearance of the generated image based on the selected color scheme.
    
    Args:
        image (PIL.Image): The image to be customized.
        color_scheme (str): The color scheme to apply ("bright", "dark", "muted").
        
    Returns:
        PIL.Image: The customized image.
    """
    if color_scheme == "dark":
        image = image.convert("L")  # Convert the image to grayscale (dark theme)
    elif color_scheme == "muted":
        image = image.point(lambda p: p * 0.8)  # Darken the image slightly
    return image


def randomize_style():
    """
    Randomly select an artistic style from a predefined list.
    
    Returns:
        str: A randomly chosen artistic style.
    """
    styles = ["Impressionist", "Picasso", "Surreal", "Modern", "Abstract", "Pop Art", "Cubism"]
    return random.choice(styles)  # Randomly choose one style


def randomize_colors():
    """
    Randomly select a color scheme from a predefined list.
    
    Returns:
        str: A randomly chosen color scheme.
    """
    return random.choice(["Bright", "Dark", "Muted", "Pastel", "Vibrant"])  # Randomly choose one color scheme


def generate_art(user_input, style, color_scheme, variations):
    """
    Generate artwork based on user input, style, color scheme, and number of variations.
    
    Args:
        user_input (str): The description of the image.
        style (str): The selected artistic style.
        color_scheme (str): The selected color scheme.
        variations (int): The number of image variations to generate.
        
    Returns:
        tuple: A tuple containing a list of download links for the generated images and a string describing the random style and color scheme.
    """
    if not user_input.strip():
        return None, "Error: Prompt is empty. Please provide a valid description."

    images = []  # List to store generated images
    download_links = []  # List to store file paths for downloading images
    for i in range(variations):
        generated_image = generate_image(user_input)
        if generated_image is None:
            return None, "Error: Failed to generate image. Please try again later."

        customized_image = customize_image(generated_image, color_scheme)

        image_path = os.path.join(output_dir, f"generated_image_{i+1}.png")
        customized_image.save(image_path, format="PNG")  # Save the image as PNG
        download_links.append(image_path)  # Add the image file path to the download list

    random_style = randomize_style()  # Randomly choose a style
    random_color = randomize_colors()  # Randomly choose a color scheme

    return download_links, f"Random Style: {random_style}, Random Color Scheme: {random_color}"


# Gradio interface function to allow the user to interact with the model
iface = gr.Interface(
    fn=generate_art,  # The function to call when the user interacts with the interface
    inputs=[  # Define the inputs for the user interface
        gr.Textbox(label="Enter a description for the image:", placeholder="e.g., A futuristic city skyline at night"),
        gr.Dropdown(["Impressionist", "Picasso", "Surreal", "Modern", "Abstract", "Pop Art", "Cubism"], label="Select an artistic style:"),
        gr.Dropdown(["Bright", "Dark", "Muted", "Pastel", "Vibrant"], label="Choose a color scheme:"),
        gr.Slider(1, 5, value=1, step=1, label="Number of variations")  # Slider to choose the number of variations (1 to 5)
    ],
    outputs=[  # Define the outputs to show after processing
        gr.Gallery(label="Generated Art Variations", elem_id="gallery"),  # Gallery to display generated images
        gr.Textbox(label="Random Style and Color Scheme")  # Display random style and color scheme
    ],
    title="AI Text to Image using Stable Diffusion",  # Title of the app
    description="Generate art based on a description using Stable Diffusion 2.1. Customize style, color scheme, and variations.",  # Description of the app
    flagging_mode="never"  # Disable flagging feature
)

# Launch the interface
iface.launch(share=False)  # Launch the Gradio interface without sharing publicly
