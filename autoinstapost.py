import os
import shutil
from PIL import Image
from instabot import Bot
# sdfsdf

def clean_up(i):
    dir = "config"
    remove_me = "imgs\\resized_{}.REMOVE_ME".format(i)

    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("imgs\\resized_{}".format(i))
        os.remove(src)


def resize(img, img_title):
    newsize = (1080, 1080)
    img_resized = img.resize(newsize)
    img_resized.save("C:\\Users\\User\\PycharmProjects\\automateinsta\\imgs\\resized_{}".format(img_title))


def uploadphoto(imgTitle):
    bot = Bot()
    bot.login(username="3sc4p1sm", password="85d4c62624ef8796f0cd59096e42a3f1d3ef6988740e72bf55ab07b73fe279ef")
    bot.upload_photo(imgTitle, "@3sc4p1sm")


def getfilename():
    list = os.listdir("imgs\\")
    filename = list[0]
    return filename


def movepostedimages(filename):
    shutil.move("imgs\\{}".format(filename), "posted\\{}".format(filename))

print("Getting the file...")
filename = getfilename()
img = Image.open("imgs\\{}".format(filename))

print("Cleaning up...")
clean_up(filename)
print("Cleaned up.")

print("Resizing... ")
resize(img, filename)
print("Done resizing.")

print("Uploading the file..")
uploadphoto("imgs\\resized_{}".format(filename))
print("Photo Uploaded.")

print("Moving the posted image...")
movepostedimages(filename)
print("Image moved into another folder.")
