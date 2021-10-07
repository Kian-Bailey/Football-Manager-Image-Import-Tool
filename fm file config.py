import os #allows python to operate with the operating system

os.remove("config.xml") #deletes the existing config file
fConfig = open("config.xml", "w") #creates and opens a new config file

fConfig.write("<record>"+"\n")
fConfig.write('	<boolean id="preload" value="false"/>'+'\n') 
fConfig.write('	<boolean id="amap" value="false"/>'+'\n') 


fConfig.write('	\n')
fConfig.write('	<list id="maps">'+'\n') 

path = r"C:\Users\kianb\Documents\Sports Interactive\Football Manager 2021\graphics\Faces" #path containing the image files to be mapped

files = [] #creates array to store filepaths
# r=root, d=directories, f = files
for r, d, f in os.walk(path): #retrieves the files from the path
    for file in f: #for each file in the path folder
        if '.png' in file: #if the file is a .png file:
            files.append(os.path.join(r, file)) #add filepath to files array

for f in files: #for each file in array
    filename=f[81:-4] #creates string made from characters between the 81st and 4th to last character
    imageMap = '		<record from="'+filename+'" to="graphics/pictures/person/'+filename+'/portrait"/>'
    #creates the correct format to map the image file
    fConfig.write(imageMap+'\n') #adds the remap string to the file

fConfig.write('	</list>'+'\n')
fConfig.write('</record>'+'\n')
fConfig.close() #closes the file
