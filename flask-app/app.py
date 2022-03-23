import os
import random
from flask import Flask, render_template

app = Flask(__name__)

# list of images
images = [
    "https://sipecam-open-data.s3.amazonaws.com/23378b5f-bfd0-4035-bb19-b6905bb97277.jpg",
    "https://sipecam-open-data.s3.amazonaws.com/8f8c9659-c3e7-42bb-a212-fa3bfbe8875e.jpg",
    "https://sipecam-open-data.s3.amazonaws.com/a0c57f20-1e29-4610-95cd-0f8bfbc47040.jpg"
    ]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
