from flask import Flask, request, render_template, redirect, url_for

from forms import PersonalExpenses
from models import expenses

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/expenses/", methods=["GET", "POST"])
def expenses_list():
    form = PersonalExpenses()
    error = ""
    total = expenses.total()
    if request.method == "POST":
        if form.validate_on_submit():
            expenses.create(form.data)
            expenses.save_all()
        return redirect(url_for("expenses_list"))
    return render_template("expenses.html", form=form, expenses=expenses.all(), error=error, total=total)


@app.route("/expenses/<int:expense_id>/", methods=["GET", "POST", "DELETE"])
def expense_details(expense_id):
    expense = expenses.get(expense_id - 1)
    form = PersonalExpenses(data=expense)

    if request.method == "POST":
        if form.validate_on_submit():
            expenses.update(expense_id - 1, form.data)
        return redirect(url_for("expenses_list"))
    elif request.method == "DELETE":
        if form.validate_on_submit():
            expenses.delete(expense_id - 1)
        return redirect(url_for("expenses_list"))
    return render_template("expense.html", form=form, expense_id=expense_id)

if __name__ == "__main__":
    app.run(debug=True)