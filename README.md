# AI Text-To-Image using Stable Diffusion 2.1 from StabilityAI

## Description

This app generates artwork from textual descriptions using the **Stable Diffusion 2.1** model by **StabilityAI**. Users can input a description of an image, and the app will generate a corresponding image based on the text prompt. The user can customize the generated images by selecting different artistic styles and color schemes, as well as generate multiple variations of the same description.

The app is built using **Gradio** to create an interactive web interface, and **Stable Diffusion 2.1** is used to generate the images. The app allows for adjustments to the image's appearance, including the option to apply color scheme filters and randomize the style of the image.

### Key Features:
- **Text-to-Image Generation**: Generate images from text descriptions using the Stable Diffusion model.
- **Customization**: Users can apply different artistic styles and color schemes to the generated image.
- **Multiple Variations**: Users can generate multiple variations of the same prompt.
- **Interactive Interface**: Built using **Gradio**, providing an easy-to-use interface for users to interact with the app.

## Demo

You can try the app by entering a description for the image you want to generate, select an artistic style and color scheme, and choose the number of variations to generate. The app will display the generated images and provide a download link for each.

## Model Used

The app uses the **Stable Diffusion 2.1** model from **StabilityAI**, a powerful deep learning model designed for generating high-quality images from textual descriptions. It leverages a state-of-the-art transformer architecture trained on large datasets.

## Technologies Used

- **Stable Diffusion 2.1**: A text-to-image model from **StabilityAI**.
- **Gradio**: A Python library used to build the user interface and allow easy interaction with the model.
- **Torch**: A deep learning framework used for tensor operations and GPU acceleration.
- **Pillow (PIL)**: A Python library for image processing, used for saving and manipulating generated images.
- **Random**: Python library for randomizing artistic styles and color schemes.
- **Python**: The programming language used to implement the app.

## Installation

### Prerequisites

To run this project locally, you need to have Python installed. You also need to install the required Python packages listed in `requirements.txt`.

1. Clone the repository:
   ```bash
   git clone https://github.com/karanheera/AI-Text-To-Image-using-Stable-Diffusion.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AI-Text-To-Image-using-Stable-Diffusion
   ```

3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

To run the app locally, use the following command:
```bash
python app.py
```
If Gradio app will start running on your local server, usually at [http://127.0.0.1:7860](http://127.0.0.1:7860/).

## File Structure

```plaintext
/AI-Text-To-Image-using-Stable-Diffusion
│
├── app.py              # The main app file
├── CODE_OF_CONDUCT.md  # Code of conduct file
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE             # MIT License file
├── README.md           # This file
├── requirements.txt    # List of required Python libraries
```

## Usage

### Enter a Description
Provide a textual description of the image you want to generate, such as "A futuristic city skyline at night."

### Select Style and Color Scheme
Choose an artistic style (e.g., Impressionist, Surreal) and a color scheme (e.g., Bright, Dark, Muted) for your generated image.

### Generate Variations
Use the slider to choose how many variations of the generated image you want. The app will provide a list of download links to the generated images.

### Download Images
After the images are generated, you can download them directly from the app interface.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- **StabilityAI**: For providing the **Stable Diffusion 2.1** model used in this app for text-to-image generation.
- **Gradio**: For providing an easy-to-use Python library for building interactive demos.
- **Pillow**: Python Imaging Library (PIL) Fork used for image processing.
- **Torch**: Deep learning framework used for efficient computation and GPU acceleration.

### Special Thanks
Special thanks to **StabilityAI** for providing the **Stable Diffusion 2.1** model, which powers the core functionality of this project.

## Contributing

Contributions are welcome! If you find a bug or want to add a feature, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your forked repository.
4. Create a pull request with a clear explanation of your changes.

## Contact

For any questions or inquiries, please contact the project maintainer:

**Karan Heera**  
- LinkedIn: [https://www.linkedin.com/in/karanheera/](https://www.linkedin.com/in/karanheera/)  
- GitHub: [https://github.com/karanheera](https://github.com/karanheera)
