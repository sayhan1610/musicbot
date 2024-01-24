# bot.py

from flask import Flask, render_template
import subprocess
from threading import Thread


# Flask setup
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# Function to start JMusicBot
def start_jmusicbot():
    # Run JMusicBot
    subprocess.run(['java', '-Dnogui=true', '-jar', 'JMusicBot-X.Y.Z.jar'])



# Run Flask and Discord bot
if __name__ == "__main__":
    # Start JMusicBot in a separate thread
    Thread(target=start_jmusicbot).start()

    # Start Flask in the main thread
    app.run(host='0.0.0.0', port=8080)

