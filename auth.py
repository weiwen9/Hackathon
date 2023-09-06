from flask import Flask, render_template, request, redirect, url_for
import cryptography as cryptool
import hashlib

app = Flask(__name__)

hash_object = hashlib.sha256() # Hash function


# LOG IN FUNCTION
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



# SIGN UP FUNCTION
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return render_template('signup.html', error='Username already exists')
        
        pass_bytes_data = password.encode('utf-8')
        # Store the user information in the database (in-memory for this example)

        # Update the hash object with your data
        #   # Convert your data to bytes if it's not already
        hash_object.update(pass_bytes_data)
        
        # Get the hexadecimal representation of the hash
        encrypted_password = hash_object.hexdigest()

        users[username] = encrypted_password

        return render_template('login.html')

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)


