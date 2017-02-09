from PIL import Image #imports pillow from python

def medianOdd(mylist): #sorts the data and returns the median
    listLength = len(imgList)
    sortedValues = sorted(imgList)
    middleIndex = (((listLength +1)/2)-1)
    return sortedValues[middleIndex]

imgList =[] #list to store the pictures
imgList.append(Image.open("1.png"))#loads the pictures into imglist
imgList.append(Image.open("2.png"))
imgList.append(Image.open("3.png"))
imgList.append(Image.open("4.png"))
imgList.append(Image.open("5.png"))
imgList.append(Image.open("6.png"))
imgList.append(Image.open("7.png"))
imgList.append(Image.open("8.png"))
imgList.append(Image.open("9.png"))

#hold RGB values into the list
redList =[]
greenList = []
blueList = []

canvas = Image.new("RGB",(495,557), "white") #creates new image with the RGB colors the pixels and the white background color

for x in range(0,495): #width
    for y in range(0,557): #length
        for myImage in imgList:
            myRed, myGreen, myBlue = myImage.getpixel((x,y)) #gets the current pixel value from position
                
                redList.append(myRed) #places the RGB values into its place
                greenList.append(myGreen)
                blueList.append(myBlue)
    
        red = sorted(redList) #sorts the list from highest values to its lowest value
        green = sorted(greenList)
        blue = sorted(blueList)
        
        redHold = red[5] #temp for the median
        greenHold = green[5]
        blueHold = blue[5]
        
        canvas.putpixel((x,y),(redHold,greenHold,blueHold)) #colors in the picture
        redList = []
        greenList = []
        blueList = []

canvas.save("newpic.png") #Saves the final product


