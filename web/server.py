from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('sendCookies')
def handle_message(cookies):  # รับข้อมูลเป็น string จาก JavaScript
    print('Received cookies:', cookies)
    cookies_dict = parse_cookie_string(cookies)
    if cookies_dict is not None:
        print('Parsed cookies:', cookies_dict)
        # ทำงานกับ cookies_dict ต่อไป
    else:
        print('Failed to parse cookies.')

def parse_cookie_string(cookie_str):
    cookies = {}
    parts = cookie_str.split(';')
    for part in parts:
        key_value = part.split('=')
        if len(key_value) == 2:
            key = key_value[0].strip()
            value = key_value[1].strip()
            cookies[key] = value
        else:
            return None  # ถ้าไม่สามารถแยกได้ให้คืนค่า None
    return cookies

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
