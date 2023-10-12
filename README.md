# Kick.com Video Downloader
Easy Simple Way To Download Your Kick.com Vod's 

<p align="center">
  <img src="https://img.shields.io/github/license/DaCryptoRaccoon/KickVodDownload">
  <img src="https://img.shields.io/github/languages/top/DaCryptoRaccoon/KickVodDownload">
</p>

## Introduction

Kick.com VOD Downloader is a Python script designed for downloading videos from an HLS stream and saving them in MP4 format. This script fetches the highest quality variant playlist from the provided HLS stream URL and uses FFmpeg for video download.
![image](https://github.com/DaCryptoRaccoon/KickVodDownload/assets/129953346/02ef1a4a-c2e0-4c98-8ea6-a07c8ed55bbd)
## Prerequisites

Before using this script, ensure you have the following components installed on your system:

- [Python](https://www.python.org/downloads/)  Python 3.10+
- [FFmpeg](https://ffmpeg.org/download.html)
- Python libraries: `requests` and `ffmpeg-python`. You can install them using pip:

pip3 install requests ffmpeg-python

## How to get your Kick URL

Open your browser and press F12

Click the "Network" tab

Load the replay in your browser

In the network tab, search for m3u8

![image](https://github.com/DaCryptoRaccoon/KickVodDownload/assets/129953346/7e4a8c0f-fad6-49f8-a39d-08328015e4a9)

![image](https://github.com/DaCryptoRaccoon/KickVodDownload/assets/129953346/3b311c59-cf47-4b14-b224-1ce4899b004f)

Right Click the file master.m3u8 and select Copy Link Address

![image](https://github.com/DaCryptoRaccoon/KickVodDownload/assets/129953346/3262d68e-0338-411a-8d1d-e9ec791b6e30)

Paste the URL into he script and save it then use the guide below to start the process. 

## Usage

1. Clone this repository to your local machine:

git clone https://github.com/DaCryptoRaccoon/KickVodDownload.git

2. Navigate to the project directory:

cd KickVodDownload

3. Edit the Python script to set your HLS stream URL. You can change the URL in the `url` variable in the script.

4. Run the script:

python3 grab.py

The video will be downloaded as 'output.mp4' in the same directory.

## Acknowledgments

- This script utilizes [FFmpeg](https://ffmpeg.org/) for downloading HLS video streams.
- Stream on Kick.com

## Author

- DaCryptoRaccoon (GDAX)
- https://kick.com/dacryptoraccoon ( SUBSCRIBE FOR MORE )
