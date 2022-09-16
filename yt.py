from pytube import YouTube

link = input("Enter link of youtube video to be downloaded: ")
you_tube = YouTube(link)

print(f"Title: {you_tube.title}")
print(f"Author: {you_tube.author}")
print(f"Views: {you_tube.views}")
print("Length: " + "{:.2f}".format(you_tube.length / 60) + " minutes")

# Getting the highest resolution possible
youtube_stream = you_tube.streams.get_highest_resolution()

print("Downloading...")
youtube_stream.download('C:\Downloads')
print("Download completed!")