from pytube import YouTube  # Install the required module using pip
# pip install pytube

link = input('Enter your Youtube URL : ')
yt = YouTube(link)
videos = yt.streams.all()
# This will stream all the format available for the video
video = list(enumerate(videos))
# This will be index all the format in list starting with zero
for i in video:
  print(i)
  # print all the available format of video with proper index
print("Enter the desired option to download the format")
dn_option = int(input("Enter the option : "))
# Ask user that which format he wanted to download
dn_video = videos[dn_option]
dn_video.download() # For downloading the video

print("Download Successfully")
