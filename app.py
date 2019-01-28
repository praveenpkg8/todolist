from init import init_app

app = init_app()

@app.route("/")
def welcome():
    # return json.dumps(obj={ "msg" : "welcome to todo app " }), status.HTTP_200_OK
    return 'welcome'


if __name__ == '__main__':
    app.run(debug= True)