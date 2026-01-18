from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    print("new web request")
    return f"hello from disco!!! heyyyyyyyyyy! we're live! the datetime is {datetime.now()}"


@app.route("/big")
def big_html():
    # Generate ~1MB of HTML
    chunk = "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>\n"
    # chunk is ~130 bytes, need ~7700 repetitions for 1MB
    body = chunk * 7700
    return f"<html><head><title>Big Page</title></head><body><h1>1MB HTML Test</h1>{body}</body></html>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
