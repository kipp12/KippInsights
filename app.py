from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd

events = []
count = 0
sequence_id = 1
action_id = 1
app = Flask(__name__)
    

@app.route('/', methods=["POST", "GET"])
def index():
    print("on index")
    print(events)
    return render_template('index.html', events = events, sequence_id=sequence_id,action_id=action_id)


@app.route('/add_event', methods=["POST"])
def add_event():
    global action_id, sequence_id, events

    successful = request.form.get("successful") == "on"
    action_type = request.form.get("action_type")
    x_start_coordinate = request.form.get("x_start")
    y_start_coordinate = request.form.get("y_start")
    x_end_coordinate = request.form.get("x_end")
    y_end_coordinate = request.form.get("y_end")

    new_event = {
        "sequence_id": sequence_id,
        "action_id": action_id,
        "action_type": action_type,
        "successful": successful,
        "x_start_coord": x_start_coordinate,
        "y_start_coord": y_start_coordinate,
        "x_end_coord": x_end_coordinate,
        "y_end_coord": y_end_coordinate
    }
    events.append(new_event)

    # increment action_id so the next event in this sequence gets a new one
    action_id += 1  
    print(events)

    return redirect(url_for("index"))


@app.route('/save', methods=["POST", "GET"])
def save():
    global events
    global sequence_id
    global action_id
    
    print("save test")
    
    #df = pd.DataFrame(events)
    #df.index += 1
    #print(df)
    
    sequence_id+=1
    action_id = 1

    return redirect(url_for("index"))

@app.route('/save_to_file', methods=["POST", "GET"])
def save_to_file():
    global events
    global sequence_id
    global action_id
    filepath = '~/documents/CODE/KippInsights/data/'
    
    filename = request.form.get('filename')
    if not filename.endswith(".csv"):
        filename += ".csv"

    filename = filepath + filename

    print("save to file test")
    
    df = pd.DataFrame(events)
    df.index += 1
    print(df)
    
    df.to_csv(filename, index=False)

    events = []

    sequence_id=1
    action_id=1

    return redirect(url_for("index"))



if __name__ == '__main__':
    app.run(debug=True)