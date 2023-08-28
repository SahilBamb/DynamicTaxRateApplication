from flask import Flask, request,render_template
from taxes import getStates, getAllInfo, getStateInfo

app = Flask(__name__)


@app.route("/", methods=["GET"])
def form():
    state = request.args.get("state")
    allCols = getStateInfo(state)
    rVals = ['','','','','']
    for i in range(5):
        if "column"+str(i)+"_header" in allCols:
            rVals[i] = allCols["column"+str(i)+"_header"]
    return render_template("form.html", state=state, col0=rVals[0], col1=rVals[1], col2=rVals[2], col3=rVals[3], col4=rVals[4])

@app.route("/")
def home():
    states = getStates()
    return render_template("form.html")

@app.route("/about")
def about():
    return "This is the about page."

if __name__ == "__main__":
    app.run(debug=True)