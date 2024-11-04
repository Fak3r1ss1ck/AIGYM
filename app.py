from flask import Flask, render_template, redirect, url_for
import subprocess
import os  # Import os to access environment variables

app = Flask(__name__)

# Route for the main menu
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the selected exercise
@app.route('/exercise/<exercise_name>')
def exercise(exercise_name):
    exercises = ['biceps_curls', 'pushups', 'squats', 'jumping_jacks', 'lunges', 'burpees']

    if exercise_name in exercises:
        subprocess.Popen(['python', f'exercises/{exercise_name}.py'])  # Running the exercise in the background
        return render_template('exercise.html', exercise_name=exercise_name)
    else:
        return "Exercise not found!", 404

# Back to menu when 'esc' is pressed
@app.route('/back_to_menu')
def back_to_menu():
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Use the PORT environment variable provided by Render, default to 5000 if not set
    port = int(os.environ.get('PORT', 5000))  
    app.run(host='0.0.0.0', port=port, debug=True)  # Bind to 0.0.0.0 and use the port variable
