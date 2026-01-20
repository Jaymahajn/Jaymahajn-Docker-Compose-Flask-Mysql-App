from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

# Connect to MySQL (DB must already exist)
db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "mysql"),
    user=os.getenv("MYSQL_USER", "root"),
    password=os.getenv("MYSQL_PASSWORD", "root"),
    database=os.getenv("MYSQL_DATABASE", "testdb")
)

cursor = db.cursor()

# Flask creates TABLE (not database)
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT
)
""")
db.commit()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        cursor.execute(
            "INSERT INTO messages (text) VALUES (%s)",
            (text,)
        )
        db.commit()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
