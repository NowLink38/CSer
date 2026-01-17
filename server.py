from flask import Flask, send_from_directory

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

@app.route("/radio1")
def r1():
    return """
    <audio controls autoplay>
      <source src="/capb/seg2.mp3" type="audio/mpeg">
    </audio>
    """

@app.route("/radio2")
def r2():
    return """
    <audio controls autoplay>
      <source src="/hrtw/seg2.mp3" type="audio/mpeg">
    </audio>
    """

@app.route("/radio3")
def r3():
    return """
    <audio controls autoplay>
      <source src="/htsw/seg2.mp3" type="audio/mpeg">
    </audio>
    """

@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory(".", path)
