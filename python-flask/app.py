from flask import Flask, request, render_template

import model
import poker as p
from controller.api_v1 import api_v1

app = Flask(__name__, static_url_path="/resource", static_folder="resource")
app.register_blueprint(api_v1, url_prefix="/api")

@app.route("/")
def hello():
    return "<h1>Hello Flask!</h1>123123123"


# @app.route("/hello/<username>")
# def hello_someone(username):
#     return f"Hello {username}!"

# aaa = "test {bbb}"
# print(aaa.format(bbb="124"))

@app.route("/hello/<username>")
def hello_someone(username):
    return render_template(
        "hello.html",
        username=username,
    )


# @app.route("/two_sum/<x>/<y>")
# def two_sum(x, y):
#     return str(int(x) + int(y))


@app.route("/two_sum/<int:x>/<int:y>")
def two_sum(x: int, y: int) -> str:
    return str(x + y)


# [GET] /api/get_employee_detail/<string:employee_id>
@app.route("/api/get_employee_detail/<employee_id>")
def get_employee_detail(employee_id: str) -> dict:
    def query(sql: int) -> dict:
        return {}
    sql = f"""
        select
            employee_name
            , employee_id
            , employee_dep
            , age
            , gender
        from employee
        where employee_id = '{employee_id}'
    """
    return query(sql)


# /hello_get?username=Allen&age=22
# @app.route("/hello_get")
# def hello_get():
#     username = request.args.get("username")
#     age = request.args.get("age")

#     if username is None:
#         return "What is your name?"
#     if age is None:
#         return f"Hello {username}."

#     return f"Hello {username}, you are {age} years old."


@app.route("/hello_get")
def hello_get():
    return render_template(
        "hello_get.html",
        username=request.args.get("username"),
        age=request.args.get("age"),
    )


# /hello_post
@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    result_html = """
        <form method="POST">
            <label>What is your name?</label>
            <input name="username">
            <button>SUBMIT</button>
        </form>
    """

    username = request.form.get("username")
    request_method = request.method

    if request_method == "POST":
        result_html += f"""
            <h1>Hello {username}!</h1>
        """

    return result_html


# @app.route("/poker/<int:player>")
# def poker(player: int) -> dict:
#     return p.poker(player=player)


@app.route("/poker", methods=["GET", "POST"])
def poker():
    request_method = request.method
    players = 0
    cards = dict()
    if request_method == "POST":
        players = int(request.form.get("players"))
        cards = p.poker(players)
    return render_template(
        "poker.html",
        request_method=request_method,
        cards=cards,
    )


@app.route("/show_staff")
def hello_google():
    staff_data = model.getStaff()
    column = ["ID", "Name", "DeptId", "Age", "Gender", "Salary"]
    return render_template(
        "show_staff.html",
        staff_data=staff_data,
        column=column,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
