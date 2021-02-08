from flask import Flask, render_template

from controllers.bike_controller import bikes_blueprint
from controllers.manufacturer_controller import manufacturers_blueprint

app = Flask(__name__)

app.register_blueprint(bikes_blueprint)
app.register_blueprint(manufacturers_blueprint)


@app.route('/')
def home():
    return render_template('index.html', title="Mikes Bikes - Home")

if __name__ == '__main__':
    app.run(debug=True)