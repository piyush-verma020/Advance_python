"""Q7> Explore the 'Flask' module and create a web server using Flask and Python."""

# This was mine

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
app.run()

# OUTPUT:-
#  * Serving Flask app '007_Solution'
#  * Debug mode: off
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000                   # # In order to run this code press left crtl and click on the http link
# Press CTRL+C to quit
# 127.0.0.1 - - [27/Apr/2025 13:53:54] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [27/Apr/2025 14:00:46] "GET /favicon.ico HTTP/1.1" 404 -


# This one is made by chatgpt since i was not interested in building a website

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
    <html>
        <head>
            <title>Welcome Page</title>
            <style>
                body {
                    background-color: #f0f8ff;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #555;
                }
            </style>
        </head>
        <body>
            <h1>🌟 Hello, World! 🌟</h1>
            <p>Welcome to your beautiful Flask app!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)


# OUTPUT:-

#  * Serving Flask app '007_Solution'
#  * Debug mode: on
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
#  * Running on http://127.0.0.1:5000
# Press CTRL+C to quit
#  * Restarting with stat
#  * Debugger is active!
#  * Debugger PIN: 152-619-422
# 127.0.0.1 - - [27/Apr/2025 14:01:49] "GET / HTTP/1.1" 200 -
# 127.0.0.1 - - [27/Apr/2025 14:01:50] "GET /favicon.ico HTTP/1.1" 404 -
#  * Detected change in 'd:\\python\\advance_python02.py\\007_Solution.py', reloading
#  * Restarting with stat
#   File "d:\python\advance_python02.py\007_Solution.py", line 61
#     🌟 Hello, World! 🌟
#     ^
# SyntaxError: invalid character '🌟' (U+1F31F)


# 🌟 Hello, World! 🌟
# Welcome to your beautiful Flask app!