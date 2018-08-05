
# coding: utf-8

# In[1]:

import getpass
import os
import imghdr
from PIL import Image


# In[2]:

# get the username
uname=getpass.getuser()


# In[3]:

# get the spotlight folder 
slPathpart="AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
slPath=os.path.join('C:\\Users', uname, slPathpart)
os.chdir(slPath)


# In[4]:

# create the SpotlightImagesRevealed user folder
slPathUser=os.path.join('C:\\Users', uname, 'Pictures\\SpotlightImagesRevealed')
if not os.path.exists(slPathUser):
    os.makedirs(slPathUser)


# In[5]:

# delete all files in SpotLightRevealed folder
for the_file in os.listdir(slPathUser):
    file_path = os.path.join(slPathUser, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)


# In[6]:

# copy all files from SpotLight source folder to SpotlightImagesRevealed one
from distutils.dir_util import copy_tree
fromDirectory = slPath
toDirectory = slPathUser
copy_tree(fromDirectory, toDirectory)


# In[7]:

# delete all files that are not jpeg
for root, _, files in os.walk(slPathUser):
    for f in files:
        fullpath = os.path.join(root, f)
        imageType=imghdr.what(fullpath)
        try:
            if (imageType != 'jpeg'):
                os.remove(fullpath)
        except WindowsError:
            print("Error " + fullpath)


# In[8]:

# add the right extension to files
for root, _, files in os.walk(slPathUser):
    for f in files:
        fullpath = os.path.join(root, f)
        imageType=imghdr.what(fullpath)
        try:
            suffix = imageType
            newName = os.path.join(fullpath + '.' + suffix)
            os.rename(fullpath,newName)
        except WindowsError:
            print("Error " + fullpath)


# In[9]:

# remove the images that have a portrait ratio or a widht lower than 1920px
for root, _, files in os.walk(slPathUser):
    for f in files:
        fullpath = os.path.join(root, f)
        im = Image.open(fullpath)
        width, height = im.size
        ratio = width/height
        im.close()
        if (ratio <= 1.0) or (width < 1920):
            try:
                os.remove(fullpath)
            except WindowsError:
                print("Error " + fullpath)

