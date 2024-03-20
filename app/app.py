from flask import Flask
from pywizlight import wizlight

app = Flask(__name__)

@app.route('/sendUDP/<localIP>/<action>', methods=['GET', 'POST'])
async def sendUDP(localIP, action):

    light = wizlight(localIP)

    if ('on'.__eq__(action)):
        await light.turn_on()
        return f"Bulb ip {localIP} on"
    else:
        await light.turn_off()
        return f"Bulb ip {localIP} off"


@app.route('/')
def hello():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)