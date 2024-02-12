import os
from flask import render_template, request, url_for, redirect
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from cifar10_simple_flask_app import app

# Load the model
MODEL_PATH = "weights/model.h5"
model = load_model(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"]
        if image_file:
            image_location = os.path.join("static/images", image_file.filename)
            image_file.save(image_location)

            img = image.load_img(image_location, target_size=(32, 32))
            img = image.img_to_array(img)
            img = np.expand_dims(img, axis=0) / 255.0

            prediction = model.predict(img)
            predicted_class = np.argmax(prediction, axis=1)

            return render_template(
                "index.html",
                prediction=predicted_class[0],
                image_loc=image_file.filename,
            )
    return render_template("index.html", prediction=0, image_loc=None)


@app.route("/about")
def about():
    return "A simple CIFAR-10 image classifier"
