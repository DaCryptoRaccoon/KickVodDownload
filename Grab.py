## Kick VOD Downloader & Converter
## Da Crypto Raccoon - Kick.com
import requests
import ffmpeg

# Define your kick master.m3u8 file here (ADD YOUR KICK m3u8 HERE)
url = "https://kick.com/Your/m3u8/File/Here/master.m3u8"

# Send an HTTP GET request to the HLS stream URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the master playlist to get the highest quality variant URL
    lines = response.text.split('\n')
    variant_url = None

    for line in lines:
        if line.endswith('.m3u8'):
            variant_url = line

    if variant_url:
        # Create a new HLS stream URL for the variant playlist
        variant_url = '/'.join(url.split('/')[:-1]) + '/' + variant_url

        # Use ffmpeg-python to download the video
        ffmpeg.input(variant_url).output('output.mp4').run(overwrite_output=True)

        print("Video downloaded successfully as 'output.mp4'.")
    else:
        print("No variant playlist found in the master playlist.")
else:
    print("Failed to fetch the HLS stream. Status code:", response.status_code)
