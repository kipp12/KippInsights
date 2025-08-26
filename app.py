from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)



@app.route('/', methods=["POST", "GET"])
def index():
    
    action_type = None
    x_start_coordinate = None
    y_start_coordinate = None
    x_end_coordinate = None
    y_end_coordinate = None

    if request.method == "POST":
        #Get selected action type from the form
        action_type = request.form.get("action_type")
        x_start_coordinate = request.form.get("x_start")
        y_start_coordinate = request.form.get("y_start")
        x_end_coordinate = request.form.get("x_end")
        y_end_coordinate = request.form.get("y_end")
        successful = "successful" in request.form

        #testing that values are returned from the form correctly
        print("Action:", action_type, "X:", x_start_coordinate, "Y:", y_start_coordinate)
        print("Action:", action_type, "X:", x_end_coordinate, "Y:", y_end_coordinate)
        print(successful)


    #temporary variables 
    successful = True
    shot_x_coordinate = "0.85"
    shot_y_coordinate = "0.25"

    return render_template('index.html', type=action_type,
                            x_start_coordinate=x_start_coordinate,
                            y_start_coordinate=y_start_coordinate,
                            x_end_coordinate=x_end_coordinate,
                            y_end_coordinate=y_end_coordinate,
                            successful=successful,
                            )

if __name__ == '__main__':
    app.run(debug=True)