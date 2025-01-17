"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

INSULTS = [
    'lame', 'dorky', 'a doofus', 'slow']

@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html><a href='/hello'>Hello</a><br>Hi! This is the home page.</html>"

# The <a> tag, also known as the anchor tag, is used to define a hyperlink that links one page to another.
# href=  specifies that clicking the link will take the user to the web address

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
<!doctype html>
<html>
  <head>
    <title>Hi There!</title>
  </head>
  <body>
    <h1>Hi There!</h1>
    <form action="/greet">
      What's your name? <input type="text" name="person">
      <input type="submit" value="Submit">
      <br>
	 <label for="compliment-select">Select a compliment:</label>
    <select name="compliment" id="compliment-select">
     <option value="smart">smart</option>
     <option value="cool">cool</option>
     <option value="funny">funny</option>
     </select>
	</form>
  </body>
</html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person") # get the 'person' parameter from URL query string
    compliment = request.args.get("compliment") # get selected compliment from the droptown

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>


    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0", port=6060)
