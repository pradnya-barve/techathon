#Importing Library
from PIL import Image
#Open the text file which you have to convert into handwriting
txt=open("../dummy/dummy.txt") # path of your text file
#path of page(background)photo (I have used blank page)
BG=Image.open("../dummy/white.jpg") 
sheet_width=BG.width
gap, ht = 0, 0

for i in txt.read():
    cases = Image.open(“myfont/{}.png”.format(str(ord(i))))
    BG.paste(cases, (gap, ht))
    size = cases.width
    height=cases.height
    #print(size)
    gap+=size
    if sheet_width < gap or len(i)*115 >(sheet_width-gap):
        gap,ht=0,ht+140
print(gap)
print(sheet_width)
BG.show()