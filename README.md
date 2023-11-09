# YouTube Playlist Downloader

## Introduction
This Python script allows you to download videos from a YouTube playlist using the `pytube` library. It organizes the downloaded videos into a structured folder hierarchy based on the channel and playlist names.

## Prerequisites
- **Python 3.x**: The script relies on Python, and having version 3.x installed is essential. If you haven't installed Python, download it from python.org.
- **Required Libraries**: You only need to install the `pytube` library. Use the following command to install it: `pip install pytube`
- **Operating System**: The script is designed and tested for Windows 10 and 11. While it may work on other platforms, _it has not been tested on Linux OS_.

## How to Run

You can run the script either from the command line or from an integrated development environment (IDE). Follow the steps below:

### Running from an IDE
1. Ensure Python and Pytube are installed.
2. Open the `main.py` file in your preferred integrated development environment (IDE).
3. Locate the `playlist_url` variable at Line 94.
4. Change the value of `playlist_url` to the desired YouTube playlist URL.
5. Run the script from the IDE.

### Running from the Command Line
1. Ensure Python and Pytube are installed.
2. Open a terminal.
3. Navigate to the script's directory.
4. Run the script: `python main.py`

## How the Script Works

### Folder Structure Creation
The script organizes downloaded videos into a structured folder hierarchy based on the channel and playlist names. Here's how the folder creation process works:

1. **Main Folder:** 
   - The script defines a constant named `MAIN_FOLDER` representing the main directory where all videos will be stored. By default, it is set to "Youtube Playlist Videos."

2. **Sanitizing Strings:**
   - The function `sanitize_string(input_string)` is used to remove forbidden characters from strings, ensuring folder and file names are valid.

3. **Channel and Playlist Extraction:**
   - When preparing to download a playlist, the script extracts the channel and playlist names from the provided YouTube playlist URL.

4. **Creating Folder Names:**
   - The channel and playlist names are then sanitized using `sanitize_string` to remove any invalid characters.
   - The script combines the sanitized names to create a unique folder name for the playlist.

5. **Folder Creation:**
   - The script creates the main folder (`MAIN_FOLDER`) and the playlist-specific folder if they don't already exist, using `os.makedirs`.

### Downloading Videos
The script utilizes the Pytube library to download videos from the specified YouTube playlist. Here's an overview of the video download process:

1. **High-Resolution Stream:**
   - For each video in the playlist, the script selects the highest resolution stream using `video.streams.get_highest_resolution()`.

2. **File Naming:**
   - The video title is sanitized and combined with the video index. Spaces are replaced with underscores, and forbidden characters are removed.

3. **File Path Determination:**
   - The script determines the file path for the video, including the main folder, playlist folder, and the video filename with the index.

4. **Download Check:**
   - Before downloading, the script checks if the file already exists to avoid redundant downloads.

5. **Downloading and Renaming:**
   - If the file is not present, the script downloads the video, specifying the filename with the index.
   - After download completion, the script renames the file to include the correct extension.

### Error Handling
The script includes error handling to address scenarios where a video is not found or encounters other download-related issues.
