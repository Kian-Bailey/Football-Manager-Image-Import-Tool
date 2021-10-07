# Football Manager Image Import Tool

This tool allows me to import images into the game '**Football Manager**' for my own personal use.

## Why Did I Make This?
In the default game, there is a lack of profile pictures which takes away the overall authentic feel from it. As a result, I downloaded an image pack online which contained the faces of the majority of players. This pack also included a 'config' file which allows the game to understand that the downloaded images need to be added. The file ensures that each image is placed in the correct location by using the player IDs from within the game.
As the pack doesn't contain all player faces, I found a way to add more images myself. However, to have more faces in the game, the config file needs to include the information of the new images. Instead of adding this information manually, I created a program which will write new information into the config file.
## How does the program work?

 - The program deletes the original config file and creates a new one.
 - It uses the folder location of where the images are stored.
 - An array is created which will contain the filepaths of each image file.
 - The program goes through each image in the folder and adds the filepath to the array if it is a .png file.
 - For each file in the array, the program retrieves just the name of the image from the filepath and creates the string in the correct format for the game to understand to map the image to the correct location.
 - The file is saved and closed.
## Screenshots

![The config file produced by the program](https://imgur.com/ant6Asg)

![The folder containing the image files](https://imgur.com/Pl7zBxP)

<blockquote class="imgur-embed-pub" lang="en" data-id="a/ioeg7eH" data-context="false" ><a href="//imgur.com/a/ioeg7eH"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
## Please Note
The program will not work on another device as it was only intended to be used for personal use. The attatched Python file is uploaded solely for the code to be viewed.
