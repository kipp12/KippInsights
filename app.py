from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd

events = []
count = 0

app = Flask(__name__)

def create_empty_dataframe():
    df = pd.DataFrame(columns=["action_id", "sequence_id", "action_type","successful", "x_start_coord", "y_start_coord","x_end_coord", "y_end_coord"])
    return df


    

@app.route('/', methods=["POST", "GET"])
def index():
    
    successful = False
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

        if request.form.get("successful") == "on":
            successful = True
        else:
            successful = False

        #testing that values are returned from the form correctly
        print("Action:", action_type, "X:", x_start_coordinate, "Y:", y_start_coordinate)
        print("Action:", action_type, "X:", x_end_coordinate, "Y:", y_end_coordinate)
        print(successful)

        # Each time a new event happens:
        new_event = {
            #"action_id": len(events)+1,
            "sequence_id": 1,
            "action_type": action_type,
            "successful": successful,
            "x_start_coord": x_start_coordinate,
            "y_start_coord": y_start_coordinate,
            "x_end_coord": x_end_coordinate,
            "y_end_coord": y_end_coordinate
        }
        events.append(new_event)

        #Redirect to GET page
        return redirect(url_for("index"))

    
    
    #print()
    #print("all events:")
    #print(events)

    return render_template('index.html', type=action_type,
                            x_start_coordinate=x_start_coordinate,
                            y_start_coordinate=y_start_coordinate,
                            x_end_coordinate=x_end_coordinate,
                            y_end_coordinate=y_end_coordinate,
                            successful=successful,
                            action_id=len(events)+1,
                            )

@app.route('/save', methods=["POST", "GET"])
def save():
    global events
    
    print("save test")
    print(events)
    print()
    df = pd.DataFrame(events)
    df.index += 1
    print(df)
    events = []
    


    return redirect(url_for("index"))



if __name__ == '__main__':
    app.run(debug=True)