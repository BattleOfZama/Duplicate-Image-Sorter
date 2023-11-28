# Duplicate-Image-Sorter

**What does it do?**
Searches through a user defined folder system for a massive list of image types and then copies them to a new user defined single folder without loosing photos with the same name.

**Why would you want that?**
I had loads of photos in folders in folders in folders on Google drive that were not part of Google Photos. I wanted them moved to Google photos. Unfortunately, Google photos does not allow you to point to folders to upload. Instead it requires you to point to the specific photos. Due to the sheer number of folders and photos i had, this was not an option. This script copies all the images it can find from in all the folders (no matter how many folders deep) in the user defined source folder, and pulls them into a single, user defiend, folder. Then you can point google uplaoid to this folder.

**Duplicate names**
i had something like 50,000 photos, and many had the same name, despite ebing diff photos. This script handles those by simply adding a suffix to the name of addiational images with the same name, and copies them over/ They are not lost.

**What image types / file extensions doe sit support?**
'.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG', '.mp4', '.MP4', '.avi', '.AVI', '.gif', '.GIF', '.thm', '.THM', '.ppt', '.PPT', '.pptx', '.PPTX', '.bmp', '.BMP', '.eps', '.EPS', '.pdf', '.PDF', '.tif', '.TIF', '.tiff', '.TIFF', '.eps', '.EPS', '.raw', '.RAW', '.3gp', '.3GP', '.mov', '.MOV', '.psd', '.PSD', '.mpg', '.MPG', '.emf','.EMF', '.amr', '.AMR', '.wmf', '.WMF'
Note - i have written these extensions as both small and large case to cover both types of spelling.

**Source and Target folders**
User will need to add the source and target folder directories to the code. For example:
source_directory = 'C:/Users/Horatio/Desktop/source' # Change this to your source directory

Thanks
