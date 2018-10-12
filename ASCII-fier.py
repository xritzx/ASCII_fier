RES = 128
import numpy as np
import easygui
import cv2 as cv
import matplotlib.pyplot as plt
def ax(res):
    scale = RES/res
    return round(scale,3)
def write_to_file(pic):
    f = open('ASCII_image.html','w')
    f.write("<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>ASCII-Fied</title></head><body><pre style=\"text-align: center;\">")
    for i in range(len(pic)):
        for j in range(len(pic[0])):
            k = pic[i][j]
            if(k > 220):
                c = '.'
            elif(220>=k>200):
                c = '-'
            elif(200>=k>150):
                c = '*'
            elif(150>=k>100):
                c = '#'
            elif(100>=k>50):
                c = '$'
            else:
                c = "%"
            f.write(c)
        f.write('\n')
    f.write("</pre>")
    f.write("<style>pre:active{background: black;color:white;}</style>")
    f.write("</body></html>")
def main():
    file = easygui.fileopenbox(msg="Select your Image", title="Select an Image File",default="*.jpg",filetypes=["*.png","*.jpeg"])
    pic = cv.imread(file, 0)
    f_x, f_y = map(ax, pic.shape)
    pic = cv.resize(pic,None,fx=f_x+0.02, fy=f_y-0.02,interpolation=cv.INTER_CUBIC)
    maxIntensity = 255
    phi, theta = 1, 1
    pic = (maxIntensity/phi)*(pic/(maxIntensity/theta))**0.5
    pic = np.array(pic, dtype=np.uint8)
    write_to_file(pic)
if __name__ == '__main__':
    main()