
# coding: utf-8

# In[104]:

import getpass
import os
import imghdr
from PIL import Image
import shutil
from distutils.dir_util import copy_tree


# In[105]:

# get the username
uname=getpass.getuser()


# In[106]:

# get the spotlight folder 
slPathpart="AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
slPath=os.path.join('C:\\Users', uname, slPathpart)
os.chdir(slPath)


# In[107]:

# create the SpotlightImagesRevealed user folder and the temp subfolder
slPathUser=os.path.join('C:\\Users', uname, 'Pictures\\SpotlightImagesRevealed')
if not os.path.exists(slPathUser):
    os.makedirs(slPathUser)
tempFolder=os.path.join(slPathUser,'temp')
if not os.path.exists(tempFolder):
    os.makedirs(tempFolder)


# In[108]:

# delete all files in SpotLightRevealed temp folder
for the_file in os.listdir(tempFolder):
    file_path = os.path.join(tempFolder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)


# In[109]:

# the list of source files
slrlistS = []
for root, dirs, files in os.walk(slPath):
    for file in files:
        slrlistS.append(file)


# In[110]:

# the list of destination files
slrlistD = []
for root, dirs, files in os.walk(slPathUser):
    for file in files:
        slrlistD.append(file)
slrlistD = [ext.replace('.jpeg', '') for ext in slrlistD]


# In[111]:

# the files to copy from source folder, only those that are not already in destination
filesToCopy=list(set(slrlistS) - set(slrlistD))


# In[112]:

# copy the files from source to destination
for i in filesToCopy:
    shutil.copy2(os.path.join('C:\\Users', uname, slPathpart,i), tempFolder)


# In[113]:

# delete all files that are not jpeg
for root, _, files in os.walk(tempFolder):
    for f in files:
        fullpath = os.path.join(root, f)
        imageType=imghdr.what(fullpath)
        try:
            if (imageType != 'jpeg'):
                os.remove(fullpath)
        except WindowsError:
            print("Error " + fullpath)


# In[114]:

# add the right extension to files
for root, _, files in os.walk(tempFolder):
    for f in files:
        fullpath = os.path.join(root, f)
        imageType=imghdr.what(fullpath)
        try:
            suffix = imageType
            newName = os.path.join(fullpath + '.' + suffix)
            os.rename(fullpath,newName)
        except WindowsError:
            print("Error " + fullpath)


# In[115]:

# remove the images that have a portrait ratio or a widht lower than 1920px
for root, _, files in os.walk(tempFolder):
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


# In[116]:

# copy all files from SpotLight temp user folder to SpotlightImagesRevealed one
fromDirectory = tempFolder
toDirectory = slPathUser
copy_tree(fromDirectory, toDirectory)


# In[117]:

# remove the temp SpotlightImagesRevealed folder
try:
    shutil.rmtree(tempFolder)
except OSError as e:
    print ("Error: %s - %s." % (e.filename, e.strerror))

