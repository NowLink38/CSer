from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h2>Radio Recordings</h2>
    <ul>
      <li><a href="/capb">capb</a></li>
      <li><a href="/hrtw">hrtw</a></li>
      <li><a href="/htsb">htsb</a></li>
    </ul>
    """

@app.route("/capb")
def r1():
    return """
    <audio controls autoplay>
      <source src="/capb/seg2.mp3" type="audio/mpeg">
    </audio>
    """

@app.route("/hrtw")
def r2():
    return """
    <audio controls autoplay>
      <source src="/hrtw/seg2.mp3" type="audio/mpeg">
    </audio>
    """

@app.route("/htsb")
def r3():
    return """
    <audio controls autoplay>
      <source src="/htsb/seg2.mp3" type="audio/mpeg">
    </audio>
    """

@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

