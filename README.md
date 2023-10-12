# Kick.com Video Downloader
Easy Simple Way To Download Your Kick.com Vod's 

![GitHub](https://img.shields.io/github/license/DaCryptoRaccoon/KickVodDownload/blob/main/LICENSE)

## Introduction

Kick.com VOD Downloader is a Python script designed for downloading videos from an HLS stream and saving them in MP4 format. This script fetches the highest quality variant playlist from the provided HLS stream URL and uses FFmpeg for video download.

## Prerequisites

Before using this script, ensure you have the following components installed on your system:

- [Python](https://www.python.org/downloads/)  Python 3.10+
- [FFmpeg](https://ffmpeg.org/download.html)
- Python libraries: `requests` and `ffmpeg-python`. You can install them using pip:

pip3 install requests ffmpeg-python

## Usage

1. Clone this repository to your local machine:

git clone https://github.com/

2. Navigate to the project directory:

cd KickVodDownload

3. Edit the Python script to set your HLS stream URL. You can change the URL in the `url` variable in the script.

4. Run the script:

python3 grab.py

The video will be downloaded as 'output.mp4' in the same directory.

## Acknowledgments

- This script utilizes [FFmpeg](https://ffmpeg.org/) for downloading HLS video streams.
- It makes use of the [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) Python library for working with FFmpeg in Python.
- Stream on Kick.com

## Author

- DaCryptoRaccoon (GDAX)
