from flask import Flask, render_template, session
from datetime import datetime

app = Flask(__name__)

app.secret_key = "0112"


@app.context_processor
def inject_globals():
    return dict(current_date=datetime.now().strftime("%d/%m/%Y"))


@app.route("/")
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1

    count = session["count"]
    fib_num = fibonacci(count)
    return render_template("index.html", count=count, fib_num=fib_num)


# implement memoization
def fibonacci(count):
    if count <= 0:
        return 0
    elif count == 1:
        return 1

    fib_num_1 = 0
    fib_num_2 = 1

    for _ in range(2, count + 1):
        fib_num_1, fib_num_2 = fib_num_2, fib_num_1 + fib_num_2

    return fib_num_2


if "__main__" == (__name__):
    app.run(debug=True)
