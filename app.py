from flask import Flask, render_template, request, redirect
from database import db, User, Document
from hashing import generate_hash
from qrcode_generator import generate_qr
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
APP_VERSION = "1.0"

app.config["SECRET_KEY"] = "blockchain123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["UPLOAD_FOLDER"] = "uploads"

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "Email already registered. Please login."

        user = User(
            fullname=fullname,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:
            return redirect("/dashboard")

        return "Invalid Email or Password"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        file = request.files["document"]

        if file:

            filename = secure_filename(file.filename)

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )

            file.save(filepath)

            document_hash = generate_hash(filepath)
            document = Document(
                filename=filename,
                filehash=document_hash
            )

            db.session.add(document)
            db.session.commit()
            qr_path = generate_qr(filename, document_hash)
          

            return render_template(
                "upload_success.html",
                filename=filename,
                document_hash=document_hash,
                qr_image="/static/qr/" + filename + ".png"
)

    return render_template("upload.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():

    if request.method == "POST":

        file = request.files["document"]

        if file:

            filename = secure_filename(file.filename)

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )

            file.save(filepath)

            new_hash = generate_hash(filepath)

            document = Document.query.filter_by(
                filename=filename
            ).first()

            if document:

                if document.filehash == new_hash:

                    return render_template(
                        "verified.html",
                        filename=document.filename,
                        document_hash=document.filehash
                    )

                else:

                    return render_template("tampered.html")

            else:

                return """
                <h2>No Record Found.</h2>

                <a href='/dashboard'>Back</a>
                """

    return render_template("verify.html")
@app.route("/admin")
def admin():

    documents = Document.query.all()

    return render_template(
        "admin.html",
        documents=documents
    )
if __name__ == "__main__":
    app.run(debug=True)