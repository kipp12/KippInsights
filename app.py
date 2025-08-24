from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():

    #temporary variables 
    type = "pass"
    passer = "Bukayo Saka"
    x_start_coordinate = "0.34"
    y_start_coordinate = "0.76"
    x_end_coordinate = "0.24"
    y_end_coordinate = "0.64"
    

    return render_template('index.html', type=type, passer=passer, x_start_coordinate=x_start_coordinate, y_start_coordinate=y_start_coordinate,x_end_coordinate=x_end_coordinate,y_end_coordinate=y_end_coordinate)

if __name__ == '__main__':
    app.run(debug=True)