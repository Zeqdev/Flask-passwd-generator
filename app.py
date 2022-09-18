from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/password', methods=['GET'])
def password():
    Numbers = list('0123456789')
    Chars = list('abcdefghijklmnopqrstuvwxyz')
    UppercaseChars = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    SpecialChars = list('!@#$%^&*(+-)')

    length_of_password = int(request.args.get('length'))
    type_of_password = request.args.get('type')

    password = ''

    if type_of_password == 'letters':
        for x in range(length_of_password):
            password += random.choice(Chars + UppercaseChars)
    if type_of_password == 'letters_and_numbers':
        for x in range(length_of_password):
            password += random.choice(Chars + UppercaseChars + Numbers)
    if type_of_password == 'all_characters':
        for x in range(length_of_password):
            password += random.choice(Numbers + Chars + UppercaseChars + SpecialChars)

    return render_template('password.html', password=password)

if __name__ == '__main__':
    app.run(debug = True)