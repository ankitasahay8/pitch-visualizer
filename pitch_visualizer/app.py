from flask import Flask, render_template, request
from nltk.tokenize import sent_tokenize

from prompt_engine import generate_prompt
from image_generator import generate_image

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    images = []
    scenes = []

    if request.method == "POST":

        text = request.form["story"]

        scenes = sent_tokenize(text)

        for i, scene in enumerate(scenes):

            prompt = generate_prompt(scene)

            image_path = generate_image(prompt, i)

            if image_path:
                images.append("/" + image_path)

    return render_template(
        "index.html",
        images=images,
        scenes=scenes
    )

if __name__ == "__main__":
    app.run(debug=True)