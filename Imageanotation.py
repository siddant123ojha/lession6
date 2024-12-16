import cv2
import matplotlib.pyplot as plt
image_path="3x3 logo.png"
image=cv2.imread(image_path)
imagergb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
height, width, _ =imagergb.shape
rect1_width, rect1_height=150,150
top_left=(20,20)
bottom_right=(top_left[0]+rect1_width,top_left[1]+rect1_height)
cv2.rectangle(imagergb,top_left,bottom_right,(0,255,255),3)


rect2_width, rect2_height=250,150
top_left2=(width-rect2_width-20,height-rect2_height-20)
bottom_right2=(top_left2[0]+rect2_width,top_left2[1]+rect2_height)
cv2.rectangle(imagergb,top_left2,bottom_right2,(0,255,255),3)


center1_x=top_left[0]+rect1_width // 2
center1_y=top_left[0]+rect1_width // 2
center2_x=top_left2[0]+rect1_width // 2
center2_y=top_left2[0]+rect1_width // 2

cv2.circle(imagergb,(center1_x,center1_y),15,(0,255,0),-1)
cv2.circle(imagergb,(center2_x,center2_y),15,(0,255,0),-1)

cv2.line(imagergb,(center1_x,center2_x),(center2_x,center2_y),(0,255,0),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagergb,"Region 1",(top_left[0],top_left[1]-10),font,0.7,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagergb,"Region 2",(top_left2[0],top_left2[1]-10),font,0.7,(0,255,255),2,cv2.LINE_AA)
cv2.putText(imagergb,"Center 1",(center1_x-40,center1_y+40),font,0.6,(0,255,0),2,cv2.LINE_AA)
cv2.putText(imagergb,"Center 2",(center2_x-40,center2_y+40),font,0.6,(0,0,255),2,cv2.LINE_AA)

arrow_start=(width-50,20)
arrow_end=(width-50,height-20)

cv2.arrowedLine(imagergb,arrow_start,arrow_end,(255,255,0),3,tipLength=0.05)
cv2.arrowedLine(imagergb,arrow_end,arrow_start,(255,255,0),3,tipLength=0.05)

height_label_position=(arrow_start[0]-150,(+arrow_start[1]+arrow_end[1]) // 2)

cv2.putText(imagergb,f"Height: {height}px", height_label_position,font,0.8,(255,255,0),2,cv2.LINE_AA)

plt.figure(figsize=(12,8))
plt.imshow(imagergb)
plt.title("Annotated image with regions, centers and Bi-directional height arrow")
plt.axis("off")
plt.show()