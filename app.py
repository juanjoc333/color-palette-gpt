import openai
import json
from flask import Flask, render_template, request
from dotenv import dotenv_values

from services.openai_service import get_completion
from prompts.color_palette_prompt import get_color_palette_prompt

config = dotenv_values(".env")
openai.api_key = config.get("OPENAI_API_KEY")

app = Flask(
    __name__, template_folder="templates", static_url_path="", static_folder="static"
)


def get_colors(prompt):
    response = get_completion(get_color_palette_prompt(prompt))

    app.logger.info(f"Response: {response.choices[0].message.content}")

    return json.loads(response.choices[0].message.content)


@app.route("/palette", methods=["POST"])
def palette():
    query = request.form.get("query")

    app.logger.info(f"Query: {query}")

    colors = get_colors(query)

    return {"colors": colors}


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
