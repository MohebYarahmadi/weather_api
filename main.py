from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def station_result(station, date):
    temperture = 23
    result = {
        'station': station,
        'date': date,
        'temperture': temperture
    }
    print(result)
    return result

if __name__ == "__main__":
    app.run(debug=True)
