# EmergingTech-Tasks-Project-2020
This is a repository for the Emerging Technology module's project, for Fourth Year.
This repository displays knowledge of Tensorflow, Python, Flask (Web framework for Python), and Docker. 
## Repository contents
This repository contains several files. Listed below are the files and their functions;
1. ```templates``` - Contains a static html webpage for the Flask web application.
2. ```wind_turbine_model``` - Contains a trained Keras/Tensorflow model of a Wind turbine's power and wind speed data. 
3. ```.dockerignore``` - This file ignores the files when a docker image is created.
4. ```.gitignore``` - This file contains files and folders that don't get uploaded when pushing to this Github repository.
5. ```Dockerfile``` - File contains compilation instructions for a Docker image.
6. ```README.md``` - Contains useful information about this repository, and operating the applications/files present.
7. ```powerproduction.csv``` - The csv file/dataset that was used to create the keras/tensorflow model for the wind_turbine_model.
8. ```requirements.txt``` - Contains the dependancies required for to create a Docker image.
9. ```webservice.py``` - Flask application that uses the wind_turbine_model to make predictions on a wind turbines power output, simply by entering a wind speed as an input.
10. ```wind_turbine_training_models.ipynb``` - A Juptyer notebook that inports the powerproduction.csv file to create and export a keras/tensorflow model called "wind_turbine_model".

## How to run a Jupyter Notebook file (.ipynb) locally.
To run a Jupyter notebook file, in this case, "EmergingTech-Tasks.ipynb", you must:
1. Either download and install Anaconda (https://www.anaconda.com/products/individual#Downloads) or if you have Python already installed on your machine; Open a command prompt window, and type ```pip install notebook```.
2. Navigate to the the folder containing the "EmergingTech-Tasks.ipynb" file, open a command prompt window in that folder and type: ```jupyter notebook```
3. Jupyter Notebook should open automatically within your default browser, then click the "wind_turbine_training_models.ipynb" to open that specific notebook.

## How to Run a Flask application locally.
Presuming that the latest version of Python, Flask and Tensorflow are installed on your machine, open a command prompt window or a terminal window and type in the following depending on your operating system: 
### Linux
1. ```export FLASK_APP=webservice.py```
2. ```python3 -m flask run```

### Windows
1. ```set FLASK_APP=webservice.py```
2. ```python -m flask run```

## How to Build, Run, Kill and Remove a Docker Image.
1. Build the Docker image: ```docker build -t web-service .```
2. Run the Docker image: ```docker run -d -p 5000:5000 web-service```
3. Check running Docker images: ```docker container ls```
4. Kill a runner instance of a Docker image: ```docker kill CONTAINER_ID```
5. Remove a Docker image: ```docker rm CONTAINER_ID```
