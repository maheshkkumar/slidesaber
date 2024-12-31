from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Serve images from the /images/ directory
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Prepend '/images' to the folder paths
        folder1 = os.path.join('images', request.form['folder1'])
        folder2 = os.path.join('images', request.form['folder2'])
        keyword1 = request.form['keyword1']
        keyword2 = request.form['keyword2']
        current_index = int(request.form.get('current_index', 0))  # Get current index from form, default to 0

        print(f"Folder 1: {folder1}, Folder 2: {folder2}, Keyword 1: {keyword1}, Keyword 2: {keyword2}")

        # Check if folders exist and list their contents
        if os.path.exists(folder1):
            images1 = [f for f in os.listdir(folder1) if keyword1 in f and f != '.DS_Store']
            print(f"Contents of Folder 1: {images1}")
        else:
            images1 = []
            print(f"Folder 1 does not exist: {folder1}")

        if os.path.exists(folder2):
            images2 = [f for f in os.listdir(folder2) if keyword2 in f and f != '.DS_Store']
            print(f"Contents of Folder 2: {images2}")
        else:
            images2 = []
            print(f"Folder 2 does not exist: {folder2}")

        # Select the current image from each folder for comparison
        img1 = images1[current_index] if current_index < len(images1) else None
        img2 = images2[current_index] if current_index < len(images2) else None

        print(f"Selected images: img1={img1}, img2={img2}")  # Debugging output

        # Pass the full path to the template
        return render_template('index.html', img1=os.path.join(request.form['folder1'], img1) if img1 else None,
                               img2=os.path.join(request.form['folder2'], img2) if img2 else None,
                               current_index=current_index, total_images=len(images1))

    return render_template('index.html', img1=None, img2=None, current_index=0, total_images=0)

if __name__ == '__main__':
    app.run(debug=True)