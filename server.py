"""Greeting Flask app."""

# from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULT = [
    'mean', 'rude', 'sassy', 'bossy', 'awful', 'awkward', 'cruel', 'malicious',
    'idiotic', 'inconsiderate', 'ignorant', 'vicious', 'toxic']


@app.route("/")
def start_here():
    """Home page."""

    return """<!doctype html><html>
    <head>Hi! This is the home page.</head>
    <a href="/hello">hello</a>
    </html>"""


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""
    # rad_start = """<input type="radio" name="adj" value='"""
    # rad_end = "<br>"
    # radio_string = ""
    rad = ""
    for adj in AWESOMENESS:
        # radio_string += rad_start + adj + "'>" + adj.upper() + rad_end
        rad += """<input type="radio" 
        name="adj" value="{}">{}<br>""".format(adj, adj.upper())

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br><br>
          Which word describes you? <br>
          {}
          <a href="/diss">click here if you transcend human limits</a><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(rad)

@app.route("/diss")
def say_diss():

    rad = ""
    for adj in INSULT:
        rad += """<input type="radio" 
        name="adj" value="{}">{}<br>""".format(adj, adj.upper())

    return """
    <!doctype html>
    <html>
      <head>
        <title>You have been judged!</title>
      </head>
      <body>
        <h1>Your hubris defines you!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br><br>
          Which word describes you? <br>
          {}
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(rad)


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("adj")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
