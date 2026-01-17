import glob
import os
from flask import Flask, send_from_directory

app = Flask(__name__)

def latest_segment(radio_name):
    files = sorted(glob.glob(f"{radio_name}/seg*.mp3"))
    if files:
        return os.path.basename(files[-1])
    return None

def audio_html(radio_name):
    seg = latest_segment(radio_name)
    if seg:
        return f"""
        <audio controls autoplay>
            <source src="/{radio_name}/{seg}" type="audio/mpeg">
        </audio>
        <p>Auto-refresh every 10 seconds to play newest segment</p>
        <script>
        setTimeout(()=>{{ location.reload() }}, 10000);
        </script>
        """
    return "<p>No audio yet</p>"

@app.route("/")
def index():
    return """
    <ul>
        <p>Running</p>
    </ul>
    """

@app.route("/capb")
def r1():
    return audio_html("capb")

@app.route("/hrtw")
def r2():
    return audio_html("hrtw")

@app.route("/htsb")
def r3():
    return audio_html("htsb")

@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
