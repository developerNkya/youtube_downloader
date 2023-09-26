
# ############################# console based youtube downloader #################################
import os
import yt_dlp

def download_playlist(playlist_url, format_type, location, directory):
    # Specify the location for save:
    output_folder = os.path.join(os.path.expanduser("~"), location, directory)
    
    # Map format_type A and B to their respective format strings
    format_mapping = {
        'A': 'bestaudio/best',
        'B': 'bestvideo+bestaudio/best',
    }
    
    # Determine the format based on user input or set to 'unknown' if invalid
    selected_format = format_mapping.get(format_type, 'unknown')
    
    if selected_format == 'unknown':
        print("Invalid format type. Please choose 'A' for audio or 'B' for video.")
        return
    
    ydl_opts = {
        'format': selected_format,
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'ignoreerrors': True,
        'playlistreverse': False,
        'playlistend': None,
        'playliststart': 1,
        'yesplaylist': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

# Prompt the user for input
playlist_url = input("Enter the YouTube URL: ")
while True:
    format_type = input("Choose format (A: audio, B: video): ").upper()
    if format_type in ['A', 'B']:
        break
    else:
        print("Invalid format type. Please choose 'A' for audio or 'B' for video:")

location = input("Enter Location (e.g., Desktop): ")
directory = input("Enter Directory (e.g., sampleDirectory): ")

# Call the download_playlist function with user input values
download_playlist(playlist_url, format_type, location, directory)


# Written by @developer_nkya

