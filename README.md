# Spotlight Images Revealed

"Windows 10 is keeping your lock screen sexy with its curated, personalized slideshow of images in Windows Spotlight" ([here an old how-to](https://www.windowscentral.com/how-enable-windows-spotlight)). But where are these images and how to use them?

**Spotlight Images Revealed** is a Windows 10 utility that collects these images and insert them in the folder `SpotlightImagesRevealed`, inside the user "Pictures" folder.

Written in python and built with [pyinstaller](http://www.pyinstaller.org/) (`pyinstaller --onefile -w slr.py`).

**NOTE**: I have no idea about the images license. I think that all the rights are reserverd to Microsoft.

## How to use it

Download the latest [**exe file**](https://github.com/aborruso/SpotlightImagesRevealed/releases), run it and wait until the process stops (usually no more than some seconds). It's a background process, you will not see any window.
Than you will have the images in `C:\Users\[username]\Pictures\SpotlightImagesRevealed` folder.

![SpotlightImagesRevealed](./resources/SpotlightImagesRevealed.png)
