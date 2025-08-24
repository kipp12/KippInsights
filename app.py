from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)



@app.route('/', methods=["POST", "GET"])
def index():

    action_type = None

    if request.method == "POST":
        # Get selected action type from the form
        action_type = request.form.get("action_type")

    print(action_type)

    #temporary variables 
    player = "Bukayo Saka"
    x_start_coordinate = "0.34"
    y_start_coordinate = "0.76"
    x_end_coordinate = "0.24"
    y_end_coordinate = "0.64"
    successful = True
    shot_x_coordinate = "0.85"
    shot_y_coordinate = "0.25"

    return render_template('index.html', type=action_type, player=player, x_start_coordinate=x_start_coordinate, y_start_coordinate=y_start_coordinate,x_end_coordinate=x_end_coordinate,y_end_coordinate=y_end_coordinate, successful=successful,shot_x_coordinate=shot_x_coordinate,shot_y_coordinate=shot_y_coordinate)

if __name__ == '__main__':
    app.run(debug=True)