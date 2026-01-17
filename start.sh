#!/usr/bin/env bash
set -e

mkdir -p capb hrtw htsb

record_radio() {
  NAME=$1
  URL=$2

  while true; do
    echo "Starting $NAME..."
    ffmpeg -loglevel error \
      -reconnect 1 \
      -reconnect_streamed 1 \
      -reconnect_delay_max 5 \
      -i "$URL" \
      -map 0:a \
      -c:a libmp3lame \
      -b:a 64k \
      -f segment \
      -segment_time 6900 \
      -segment_wrap 3 \
      -reset_timestamps 1 \
      "$NAME/seg%d.mp3"
    echo "$NAME crashed, restarting in 5s..."
    sleep 5
  done
}

# Start radio recordings in background
record_radio capb "http://media-ice.musicradio.com/CapitalBirmingham" &
record_radio hrtw "http://media-ssl.musicradio.com/HeartWestMids" &
record_radio htsb "http://stream-al.hellorayo.co.uk/freebirmingham.aac?aw_0_1st.skey=1602676850" &

# Start Flask web server last (Render requires binding to $PORT)
export PORT=${PORT:-10000}
echo "Starting web server on port $PORT..."
python server.py

