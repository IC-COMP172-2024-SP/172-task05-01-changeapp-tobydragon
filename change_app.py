from flask import Flask, request
import change_library

app = Flask(__name__)


@app.route('/')
def home():
 return """
     <html><body>
         <h2>Welcome to the Change Machine</h2>
         <a href="/countchange">Count Change</a>
         <br>
         <a href="/makechange">Make Change</a>   
     </body></html>
 """


@app.route('/countchange')
def count_change():
    """
    Fetches any URL parameters for pennies, nickels, dimes, and/ or quarters and reports the total dollars
    Any missing or mis-formatted URL params are replaced with 0
    """
    return """Under construction<br><br><a href="/">Home</a>"""


@app.route('/makechange')
def make_change():
    """
    Fetches a URL parameters for "money" (a float) and reports the appropriate change for that money
    (the least amount of dollars and each coin)
    missing or mis-formatted URL param is replaced with 0
    """
    return """Under construction<br><br><a href="/">Home</a>"""


if __name__ == "__main__":
    app.run(host="localhost", debug=True)

