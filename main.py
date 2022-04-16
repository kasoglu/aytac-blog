from flask import Flask, render_template, request
import requests
import smtplib

JSON_API = "https://api.npoint.io/c326edc97f9ae13aa2c1"

posts = requests.get(JSON_API).json()

app = Flask(__name__)


@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_mail(name, email, phone, message):
    my_email = YOUR EMAIL ADDRESS
    password = YOUR PASSWORD

    title = "You have a message! from Aytac's Blog"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email",
            msg=f"Subject:{title}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
        )


if __name__ == "__main__":
    app.run(debug=True)
