import os
from flask import render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from cifar10_simple_flask_app import app

# Load the model
MODEL_PATH = "weights/model.h5"
model = load_model(MODEL_PATH)

# CIFAR-10 class names
CLASS_NAMES = [
    "Airplane",
    "Automobile",
    "Bird",
    "Cat",
    "Deer",
    "Dog",
    "Frog",
    "Horse",
    "Ship",
    "Truck",
]


@app.route("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            # Ensure the directory exists
            image_directory = os.path.join(app.static_folder, "images")
            if not os.path.exists(image_directory):
                os.makedirs(image_directory)

            image_location = os.path.join(image_directory, image_file.filename)
            image_file.save(image_location)

            img = image.load_img(image_location, target_size=(32, 32))
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0) / 255.0

            prediction = model.predict(img)
            predicted_class = np.argmax(prediction, axis=1)
            predicted_class_name = CLASS_NAMES[predicted_class[0]]

            return render_template(
                "index.html",
                prediction=predicted_class_name,
                image_loc=image_file.filename,
            )
    return render_template("index.html", prediction="None", image_loc=None)
