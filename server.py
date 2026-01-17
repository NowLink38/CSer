import glob
import os
from flask import Flask, send_from_directory, Response

app = Flask(__name__)

# Utility: get latest segment of a radio
def latest_segment(radio_name):
    files = sorted(glob.glob(f"{radio_name}/seg*.mp3"))
    if files:
        return os.path.basename(files[-1])
    return None

# Route: index page with links
@app.route("/")
def index():
    return """
<html><head></head><body style="background-color:black;">
<p style="font-size: 10vw;"><a href="/capb">capb</a></p>
<br>
<p style="font-size: 10vw;"><a href="/hrtw">hrtw</a></p>
<br>
<p style="font-size: 10vw;"><a href="/htsb">htsb</a></p>
</body></html>
    """

# Route: play a radio seamlessly
def radio_player_html(radio_name):
    return f"""
<html><head><style>
  audio {
    width: 100%;
    max-width: 100%;
  }

  body {
    margin: 0;
    padding: 20px;
    display: flex;
    justify-content: center;
  }
</style></head><body style="background-color:black;">
    <h3>{radio_name.title()}</h3>
    <audio id="player" controls autoplay></audio>
    <script>
    const player = document.getElementById('player');
    let lastSegment = null;

    async function checkSegment() {{
        try {{
            const res = await fetch('/{radio_name}/latest');
            const seg = await res.text();
            if (!seg) return;  // no audio yet
            if (seg !== lastSegment) {{
                player.src = '/{radio_name}/' + seg;
                player.play();
                lastSegment = seg;
            }}
        }} catch (e) {{
            console.log('Error fetching latest segment:', e);
        }}
    }}

    // Check every 2 seconds for new segments
    setInterval(checkSegment, 2000);

    // Initial load
    checkSegment();
    </script>
    </body></html>
    """

@app.route("/capb")
def r1():
    return radio_player_html("capb")

@app.route("/hrtw")
def r2():
    return radio_player_html("hrtw")

@app.route("/htsb")
def r3():
    return radio_player_html("htsb")

# Route: return latest segment filename
@app.route("/<radio_name>/latest")
def latest_file(radio_name):
    seg = latest_segment(radio_name)
    if seg:
        return seg
    return ""

# Route: serve mp3 files
@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory(".", path)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
