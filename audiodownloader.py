import pafy

url = input("Enter the complete URL of the audio ") 

# create an object using pafy.new()
audio = pafy.new(url)

print(audio.title) #to get the title of the audio
print(audio.author) #to get the author of the audio 
print(audio.viewcount) #to get the number of views
print(audio.length) #to get the length of audio

streams = audio.m4astreams  #this will return A list of audio streams (streams containing both audio and audio)

for i in streams:
    print (i) #print all the streams available for that audio link

best = audio.getbestaudio(preftype="m4a") #this method returns the best resolution

print("downloading " + str(best))
best.download(filepath="./media/songs/")

print(" m4a downloaded successfully")