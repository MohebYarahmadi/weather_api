from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def station_result(station, date):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperture = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    result = {
        'station': station,
        'date': date,
        'temperture': temperture
    }
    return result

if __name__ == "__main__":
    app.run(debug=True)
