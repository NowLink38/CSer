#!/usr/bin/env bash
set -e

mkdir -p capb hrtw htsb

echo "Starting radio recorders..."

ffmpeg -loglevel error \
  -i "http://media-ice.musicradio.com/CapitalBirmingham" \
  -map 0:a \
  -c:a libmp3lame \
  -b:a 64k \
  -f segment \
  -segment_time 6900 \
  -segment_wrap 3 \
  -reset_timestamps 1 \
  capb/seg%d.mp3 &

ffmpeg -loglevel error \
  -i "http://media-ssl.musicradio.com/HeartWestMids" \
  -map 0:a \
  -c:a libmp3lame \
  -b:a 64k \
  -f segment \
  -segment_time 6900 \
  -segment_wrap 3 \
  -reset_timestamps 1 \
  hrtw/seg%d.mp3 &

ffmpeg -loglevel error \
  -i "http://stream-al.hellorayo.co.uk/freebirmingham.aac?aw_0_1st.skey=1602676850" \
  -map 0:a \
  -c:a libmp3lame \
  -b:a 64k \
  -f segment \
  -segment_time 6900 \
  -segment_wrap 3 \
  -reset_timestamps 1 \
  htsb/seg%d.mp3 &

wait
