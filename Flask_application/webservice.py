# Flask web microservice import.
from flask import Flask, request, render_template
import tensorflow as tf

# Create a new web app.
app = Flask(__name__)

# Setting a constant for the index page
INDEX = "index.html"

# Add route to the root ('/') location, that calls the "hello_world()" function.
@app.route('/', methods=["GET", "POST"])
def root():
    if request.method == "POST":
        # Setting a wind speed that we want to predict the power output for
        wind_speed = request.form["speed_input"]
        # Casting wind_speed to a float from a string
        wind_speed = [float(wind_speed)]
        # Grabbing the saved wind turbine tensorflow model
        wind_turbine_model = tf.keras.models.load_model('wind_turbine_model')
        # Testing the accuracy of the predictions (using the "wind_speed" guess)
        model_prediction = wind_turbine_model.predict(wind_speed)
        return render_template(INDEX, prediction=model_prediction[0])
    return render_template(INDEX)