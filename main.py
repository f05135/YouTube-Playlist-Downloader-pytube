'''
MIT License

Copyright (c) 2023 f05135

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
from pytube import Playlist

# Constants for Folder Names
MAIN_FOLDER = "Youtube Playlist Videos"

def sanitize_string(input_string):
    """Remove forbidden characters from the string."""
    return ''.join(char if char.isalnum() or char in ['.', '_'] else ' ' for char in input_string)

def create_videos_folder(playlist_url):
    """
    Create the folder structure for storing downloaded videos.
    
    Args:
        playlist_url (str): The URL of the YouTube playlist.
    """
    # Extract channel and playlist names from the URL
    channel_name = Playlist(playlist_url).videos[0].author
    playlist_name = Playlist(playlist_url).title

    # Sanitize folder names
    channel_name_sanitized = sanitize_string(channel_name)
    playlist_name_sanitized = sanitize_string(playlist_name)

    playlist_folder = os.path.join(MAIN_FOLDER, f"{channel_name_sanitized}_{playlist_name_sanitized}")

    # Create main and playlist folders if they don't exist
    os.makedirs(MAIN_FOLDER, exist_ok=True)
    os.makedirs(playlist_folder, exist_ok=True)

def download_videos_from_playlist(playlist_url):
    """
    Download videos from the specified YouTube playlist.
    
    Args:
        playlist_url (str): The URL of the YouTube playlist.
    """
    playlist = Playlist(playlist_url)
    
    for index, video in enumerate(playlist.videos, start=1):
        download_video(video, index, playlist_url)

def download_video(video, index, playlist_url):
    """
    Download an individual video and save it with an index in the filename.
    
    Args:
        video: A Pytube Video object.
        index (int): The index of the video in the playlist.
        playlist_url (str): The URL of the YouTube playlist.
    """
    try:
        stream = video.streams.get_highest_resolution()
        video_title = video.title

        # Replace spaces with underscores and remove other forbidden characters
        video_title_sanitized = sanitize_string(video_title)
        video_title_sanitized = '_'.join(video_title_sanitized.split())

        # Extract channel and playlist names from the URL
        channel_name = Playlist(playlist_url).videos[0].author
        playlist_name = Playlist(playlist_url).title

        # Sanitize folder names
        channel_name_sanitized = sanitize_string(channel_name)
        playlist_name_sanitized = sanitize_string(playlist_name)

        playlist_folder = os.path.join(MAIN_FOLDER, f"{channel_name_sanitized}_{playlist_name_sanitized}")
        file_path_temp = os.path.join(playlist_folder, f"{index}_{video_title_sanitized}")
        file_path_mp4 = file_path_temp + ".mp4"

        # Check if the file already exists, and avoid downloading it again
        if not os.path.exists(file_path_mp4):
            print(f"\nDownloading video {index}/{len(playlist)}: {video_title}")
            
            # Specify the filename with the index when downloading
            stream.download(output_path=playlist_folder, filename=f"{index}_{video_title_sanitized}")
            
            # Rename the downloaded file to include the correct extension
            os.rename(file_path_temp, file_path_mp4)

            print(f"Video {index}/{len(playlist)} downloaded successfully: {file_path_mp4}")
        else:
            print(f"Video {index}/{len(playlist)} already exists. Skipping: {file_path_mp4}")

    except FileNotFoundError:
        print(f"Error: FileNotFoundError - Video {index}/{len(playlist)} not found on YouTube.")
    except Exception as e:
        print(f"Error downloading video {index}/{len(playlist)}: {e}")

if __name__ == "__main__":
    try:
        playlist_url = r"https://www.youtube.com/playlist?list=PLEfwqyY2ox84iIVoCHP8JjObsXQtVjh2k" # Insert here the playlist URL link
        playlist = Playlist(playlist_url)
        
        create_videos_folder(playlist_url)
        download_videos_from_playlist(playlist_url)

        print("Download completed successfully!")

    except Exception as e:
        print(f"Error: {e}")