import time
# import raspi cpu params
from gpiozero import CPUTemperature
# Flask for web-dev
from flask import Flask, render_template

# define app
app = Flask('Testing')

@app.route('/')
def index():   
    cpu = CPUTemperature()
    temp = round(cpu.temperature, 2)
    return render_template('temperatuur.html', variable=temp)

if __name__ == '__main__':
    app.run()