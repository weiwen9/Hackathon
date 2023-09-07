from flask import Flask, render_template, request, redirect, url_for
import cryptography as cryptool
import hashlib

app = Flask(__name__)

hash_object = hashlib.sha256() # Hash function

# LOG IN FUNCTION
users = {
    'john': ['Password', 'John@email.com'],
    'jane': ['Password', 'John@email.com'],
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
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']

        if username in users:
            return render_template('signup.html', error='Username already exists')
        
        pass_bytes_data = password.encode('utf-8') # Convert to bytes
        hash_object.update(pass_bytes_data)
        encrypted_password = hash_object.hexdigest() # Get the hexadecimal representation of the hash
    
        pass_bytes_data2 = password2.encode('utf-8') # Convert to bytes
        hash_object.update(pass_bytes_data2)
        encrypted_password2 = hash_object.hexdigest()

        if encrypted_password != encrypted_password2:
            return render_template('signup.html', error='Passwords do not match')

        users[username] = [encrypted_password, email]
        print(username,": Encrypted[",encrypted_password,']') # FOR DEBUGGING TO BE REMOVED LATER
        return render_template('login.html', success='Your account has been created')

    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)


