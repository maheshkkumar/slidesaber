# slidesaber 🔦

A simple tool to visually compare image pairs using a slider. This tool is built on top of the [image-slider](https://www.w3schools.com/howto/howto_js_image_comparison.asp) codebase and further developed to load images from two folders for comparison.

# Installation
To set up the environment required to run the app, follow these steps:

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server**:
   ```bash
   python3 app.py
   ```

5. **Open your web browser** and navigate to `http://127.0.0.1:5000` to access the image comparison tool.
   
Make sure you have Python 3 and pip installed on your system before starting the setup.

## Usage
Once the server is running, you can use the tool as follows:

1. **Upload Images**: Enter the paths to the two folders containing the images you want to compare. You can also specify keywords to filter the images.

2. **Compare Images**: After submitting the form, the images will be loaded side by side. You can click and drag the blue slider to compare the two images visually.

3. **Navigate Through Images**: Use the "Previous" and "Next" buttons to navigate through the images in the specified folders.

4. **Refresh the Page**: If you want to compare a different set of images, simply refresh the page and enter new folder paths and keywords.

<!-- ## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. Any contributions, bug fixes, or feature requests are welcome! -->

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.