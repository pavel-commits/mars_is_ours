# flask
from flask import Flask
from flask import render_template

# data
from data.db_session import global_init
from data.db_session import create_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department

app = Flask(__name__)


@app.route("/")
def index():
    db_sess = create_session()
    actions = db_sess.query(Jobs).all()

    return render_template("index.html", title="Рабочий журнал", actions=actions)


if __name__ == '__main__':
    global_init("mars_explorer.db")
    app.run()