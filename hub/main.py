from fastapi import FastAPI
import radio


app = FastAPI(title='SmartHome Hub API')

@app.get('/toggle/relay')
def toggle_relay():
    radio.toggle(radio.Device.relay)
    return 'ok'

@app.get('/toggle/led')
def toggle_led():
    radio.toggle(radio.Device.led)
    return 'ok'

@app.get('/led/red')
def led_red():
    radio.led_red()
    return 'ok'

@app.get('/led/green')
def led_green():
    radio.led_green()
    return 'ok'

@app.get('/led/blue')
def led_blue():
    radio.led_blue()
    return 'ok'