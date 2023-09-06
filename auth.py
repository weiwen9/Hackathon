from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple user database (in-memory for this example)
users = {
    'john': 'password123',
    'jane': 'securepass',
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            # Redirect to a success page or perform other actions
            return 'Login successful!'
        else:
            # Redirect back to the login page with an error message
            return render_template('login.html', error='Invalid credentials')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
