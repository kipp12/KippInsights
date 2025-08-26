from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)



@app.route('/', methods=["POST", "GET"])
def index():
    
    action_type = None
    x_start_coordinate = "0.00"
    y_start_coordinate = "0.00"
    x_end_coordinate = "0.0"
    y_end_coordinate = "0.00"

    if request.method == "POST":
        # Get selected action type from the form
        action_type = request.form.get("action_type")
        x_start_coordinate = request.form.get("x_start")
        y_start_coordinate = request.form.get("y_start")
        x_end_coordinate = request.form.get("x_end")
        y_end_coordinate = request.form.get("y_end")
        print("Action:", action_type, "X:", x_start_coordinate, "Y:", y_start_coordinate)
        print("Action:", action_type, "X:", x_end_coordinate, "Y:", y_end_coordinate)
    
    

    #temporary variables 
    #player = "Bukayo Saka"
    successful = True
    shot_x_coordinate = "0.85"
    shot_y_coordinate = "0.25"

    return render_template('index.html', type=action_type,
                            #player=player,
                            x_start_coordinate=x_start_coordinate,
                            y_start_coordinate=y_start_coordinate,
                            x_end_coordinate=x_end_coordinate,
                            y_end_coordinate=y_end_coordinate,
                            successful=successful,
                            shot_x_coordinate=shot_x_coordinate,
                            shot_y_coordinate=shot_y_coordinate)

if __name__ == '__main__':
    app.run(debug=True)