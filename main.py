from flask import Flask, render_template, request, make_response
import datetime

app = Flask(__name__)

# Jinja enables us to send variables from a handler to an HTML template

@app.route("/")
def index():
    some_text = "Message from the handler."
    current_year = datetime.datetime.now().year
    cities = ["Boston", "Vienna", "Paris", "Berlin"]

    response = make_response(render_template("index.html", some_text=some_text, current_year=current_year, cities=cities))
    # como apagar o cookie criado
    response.set_cookie("user_name", expires=0)
    return response

# se não for especificado nenhum método, o default será o GET
# @app.route("/about-me", methods=["GET"])
# def about():
#     return render_template("about.html")

@app.route("/contact", methods=["POST"])
def contact():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template("success.html")

# comentado os dois handlers acima e substituido pelo about me com POST e GET

@app.route("/about-me", methods=["GET", "POST"])
def about():
    if request.method == "GET":
        #return render_template("about.html")
        user_name = request.cookies.get("user_name")
        return render_template("about.html", name=user_name)

    elif request.method == "POST":
        contact_name = request.form.get("contact-name")
        contact_email = request.form.get("contact-email")
        contact_message = request.form.get("contact-message")

        print(contact_name)
        print(contact_email)
        print(contact_message)

        # em vez do retorno do success.html, vamos retornar o cookie
        # return render_template("success.html")
        response = make_response(render_template("success.html"))
        response.set_cookie("user_name", contact_name)

        return response




if __name__ == '__main__':
    app.run(use_reloader=True)





