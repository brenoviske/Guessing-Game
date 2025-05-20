from flask import Flask, render_template, request # importing tools
import random 
app = Flask(__name__)
# Creating flask application

@app.route ('/', methods = ['GET','POST']) # creating the route and it's type
def homepage():
    if request.method == 'POST':
        machine = random.randint(1,10) # creating the machine number
        guess =  int(request.form.get('guess')) 
        if guess == machine:
            message = f'CONGRATS, you guessed the right number'
            return render_template('index.html',message = message) # Winning message, if you get the number right
        else:
            message = f'Nah, the number {guess} that you guessed is not the right number'
            return render_template('index.html',message=message) # Error mesage, it should pop up every time that the user gets the wrong number
    return render_template('index.html')

if __name__ == '__main__': # putting the file in conditional terms to assure that this code will display only if this file is runned
    app.run(debug=True)