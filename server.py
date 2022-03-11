from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def checker8():
    return render_template("index.html")


@app.route('/<int:num1>')
def checker4(num1):
    return render_template("index.html", num1=num1)


@app.route('/<int:num1>/<int:num2>')
def checker_x_by_y(num1, num2):
    return render_template("index.html", num1=num1, num2=num2)


@app.route('/<int:num1>/<int:num2>/<color1>/<color2>')
def checker_x_by_y_color_by_color(num1, num2, color1, color2):
    return render_template("index.html", num1=num1, num2=num2, color1=color1, color2=color2)


#! MUST BE AT THE BOTTOM ---------------
if __name__ == "__main__":
    app.run(debug=True)
