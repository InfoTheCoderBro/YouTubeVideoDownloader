from pytube import YouTube

# Replace "Youtube video link here" with the URL of the YouTube video you want to download.
link = "Youtube video link here"
youtube_1 = YouTube(link)

# Uncomment the following lines if you want to print the video title and thumbnail URL.
# print(youtube_1.title)
# print(youtube_1.thumbnail_url)

# Get all available video streams for the YouTube video.
videos = youtube_1.streams.all()  # All Format
# If you want to download only the audio, you can use the following line instead.
# videos = youtube_1.streams.filter(only_audio=True)  # Only Audio

# Enumerate and print the available video streams along with their indices.
vid = list(enumerate(videos))
for i in vid:
    print(i)

print()

# Prompt the user to select a stream for downloading.
strm = int(input("Enter the index of the stream you want to download: "))
videos[strm].download()
print('Successfully downloaded!')

# # ***** Playlist ****

# Uncomment the following lines if you want to download videos from a playlist.
# from pytube import Playlist
#
# # Replace 'Videos Playlist link here' with the URL of the YouTube playlist you want to download.
# py = Playlist('Videos Playlist link here')
#
# print(f'Downloading: {py.title}')
#
# # Download the first available stream for each video in the playlist.
# for video in py.videos:
#     video.streams.first().download()
