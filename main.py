import cv2
import sys
import os

WIDTH = 4
HEIGHT = 5


def get_color(imgfile, rowlocn, collocn):
    R = int(0)
    G = int(0)
    B = int(0)
    for i in range(WIDTH):
        for j in range(HEIGHT):
            R += int(imgfile[WIDTH*rowlocn + i,HEIGHT*collocn + j][0])
            G += int(imgfile[WIDTH*rowlocn + i,HEIGHT*collocn + j][1])
            B += int(imgfile[WIDTH*rowlocn + i,HEIGHT*collocn + j][2])

    R /= WIDTH * HEIGHT
    G /= WIDTH * HEIGHT
    B /= WIDTH * HEIGHT
    return R,G,B


def MakeCSSFile(ImgFile):
    outputfile = open("Image.css", "w")
    outputfile.write("#Image {\n position: absolute;\n box-shadow: \n")
    img_initial = cv2.imread(ImgFile)
    img_initial = cv2.cvtColor(img_initial, cv2.COLOR_BGR2RGB)
    rows, cols, color = img_initial.shape
    rows = int(rows / WIDTH)
    cols = int(cols / HEIGHT)

    for i in range(rows):
        for j in range(cols):
            colorValue = get_color(img_initial, i, j)
            outputfile.write( str(HEIGHT * j) + "px "  + str(WIDTH * i) + "px " + str(
                HEIGHT) + "px " + str(WIDTH) + "px " + "rgb(" + str(int(colorValue[0]) )+ " " + str(int(colorValue[1]) ) + " " + str(int(colorValue[2]) ) + ")")

            if i == rows-1 and j == cols-1:
                outputfile.write(";\n}")
            else:
                outputfile.write(",\n")


    outputfile.close()






if __name__ == "__main__":


    img = sys.argv[1]
    print("Converting")
    MakeCSSFile(img)
    print("Done!!")

    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # os.chdir(os.path.join(BASE_DIR+ "\\CSS my image"))
    #
    # inputPath = os.path.join(BASE_DIR + "\\CSS my image\\Input")
    # outputPath = os.path.join(BASE_DIR + " \\CSS my image\\Output")
    # print(inputPath)
    #
    # i = 0
    # for file in os.listdir(inputPath):
    #     MakeCSSFile(inputPath + "\\" + file, outputPath, i)
    #     i += 1