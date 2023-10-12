from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('07-index.html')

# This page will be the page after the form
@app.route('/report')
def report():
    user = request.args.get('user')

    is_correct = False
    errors = []

    has_one_lower = any(c.islower() for c in user)
    has_one_upper = any(c.isupper() for c in user)
    has_one_number = any(c.isdigit() for c in user)
    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.

    if has_one_lower & has_one_upper & has_one_number:
        is_correct = True

    if not has_one_lower:
        errors.append("Lower is missing")
    if not has_one_upper:
        errors.append("Upper is missing")
    if not has_one_number:
        errors.append("Number is missing")

    return render_template('07-report.html', user=user, is_correct=is_correct, errors=errors)


if __name__ == '__main__':
    app.run(debug=True)
