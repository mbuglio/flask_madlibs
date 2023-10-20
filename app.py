from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)



@app.route('/')
def ask_adlibs():
    prompts = story.prompts
    return render_template("prompts.html", prompts=prompts)

@app.route('/story')
def view_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)



