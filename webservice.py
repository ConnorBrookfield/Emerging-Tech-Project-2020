# Flask web microservice import.
import flask as fl

# Create a new web app.
app = fl.Flask(__name__)

# Add route to the root ('/') location, that calls the "hello_world()" function.
@app.route('/')
def hello_world():
    return "Hello world!"