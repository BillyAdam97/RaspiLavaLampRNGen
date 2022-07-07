import cv2
import random
import hashlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cap = cv2.VideoCapture(0)
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
dic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

def animate(i):
    ret, frame = cap.read()
    for i in frame:
        b = bytearray(i)
        r2 = []
        for k in range(len(b)):
            if k%3==0:
                r2.append(b[k])
        c = bytearray(r2)
        hashed = hashlib.sha256(c).hexdigest()
        random.seed(hashed)
        dic[random.randint(1,10)]+=1
    
    x = list(dic.keys())
    y = list(dic.values())
    ax1.clear()
    ax1.bar(range(len(dic)),y, tick_label=x)
    

ani = animation.FuncAnimation(fig, animate,interval=100)
plt.show()
cap.release()
cv2.destroyAllWindows() 
