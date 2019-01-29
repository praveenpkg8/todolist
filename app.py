from init import init_app
from flask_cors import CORS




app = init_app()
CORS(app)


@app.route("/")
def welcome():
    return 'welcome todo app'


if __name__ == '__main__':
    app.run(debug=True)
