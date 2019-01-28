from init import init_app
from flask_cors import CORS

app = init_app()
CORS(app)

@app.route("/")
def welcome():
    # return json.dumps(obj={ "msg" : "welcome to todo app " }), status.HTTP_200_OK
    return 'welcome'


if __name__ == '__main__':
    app.run(debug= True)