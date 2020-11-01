from flask import Flask, request, render_template, redirect, url_for

from forms import PersonalExpenses
from models import expenses

app = Flask(__name__)
app.config["SECRET_KEY"] = "1234"

@app.route("/expenses/", methods=["GET", "POST"])
def expenses_list():
    form = PersonalExpenses()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            expenses.create(form.data)
            expenses.save_all()
        return redirect(url_for("expenses_list"))

    return render_template("expenses.html", form=form, expenses=expenses.all(), error=error)

@app.route("/expenses/<int:exp_id>/", methods=["GET", "POST"])
def expenses_update(exp_id):
    expense = expenses.get(exp_id - 1)
    form = PersonalExpenses(data=expense)

    if request.method == "POST":
        if form.validate_on_submit():
            expenses.update(exp_id - 1, form.data)
        return redirect(url_for("expenses_list"))
    return render_template("expense.html", form=form, exp_id=exp_id)

if __name__ == "__main__":
    app.run(debug=True)