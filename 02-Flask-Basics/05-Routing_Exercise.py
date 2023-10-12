# Set up your imports here!
# import ...
from flask import Flask
app = Flask(__name__)


@app.route('/') # Fill this in!
def index():
     return '<h1>Welcome</h1>'

@app.route('/puppylatin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!
    last_character = name[-1]

    out_name = name[0:-1] + 'iful' if last_character == 'y' else name + 'y'

    return f"<h1>Your puppy latin name is {out_name}"

if __name__ == '__main__':
    app.run()
