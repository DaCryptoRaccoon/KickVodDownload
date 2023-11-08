import requests
import ffmpeg

# Define the HLS stream URL
url = "https://stream.kick.com/ivs/v1/your_vod_link_here/master.m3u8"

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

        # Adjust the FFmpeg encoding settings for higher quality and resolution
        input_stream = ffmpeg.input(variant_url)
        output_stream = ffmpeg.output(input_stream, 'output.mp4', s='1920x1080', b='5000k', **{'c:v': 'libx264', 'crf': 18, 'preset': 'slow', 'movflags': 'faststart'})
        ffmpeg.run(output_stream, overwrite_output=True)

        print("Video downloaded successfully as 'output.mp4' with improved encoding settings.")
    else:
        print("No variant playlist found in the master playlist.")
else:
    print("Failed to fetch the HLS stream. Status code:", response.status_code)
