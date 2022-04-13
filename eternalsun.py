import math
import matplotlib.pyplot as plt
debug=1
halo=0

#Param
scale = 1
r=10
spike_space = r/4
spike_length = r*2
spike_width = r/2

#circle
circle_x=[]
circle_y=[]
for theta in range(0,360):
    circle_x.append(math.cos(theta*math.pi/180)*r)
    circle_y.append(math.sin(theta*math.pi/180)*r)

#TopSpike 
Spike_x=[0,spike_width*math.cos(60*math.pi/180),0,-spike_width*math.cos(60*math.pi/180),0]
Spike_y=[r+spike_space,r+spike_space+spike_length/3*math.sin(60*math.pi/180),r+spike_space+spike_length*math.sin(60*math.pi/180),r+spike_space+spike_length/3*math.sin(60*math.pi/180),r+spike_space]
Spike_ny=[item*-1 for item in Spike_y]

#Topright Spike
#rotation
Spike_rx=[]
Spike_ry=[]
for i in range(len(Spike_x)):
    Spike_rx.append(Spike_x[i]*math.cos(45*math.pi/180)+Spike_y[i]*math.sin(45*math.pi/180))
    Spike_ry.append(-Spike_x[i]*math.sin(45*math.pi/180)+Spike_y[i]*math.cos(45*math.pi/180))
Spike_nrx =[item*-1 for item in Spike_rx]
Spike_nry =[item*-1 for item in Spike_ry]

#Halo
if halo:
    halo_x=[]
    halo_y=[]
    for theta in range(0,360):
        halo_x.append(math.cos(theta*math.pi/180)*(r+spike_space+spike_length/3*math.sin(60*math.pi/180)))
        halo_y.append(math.sin(theta*math.pi/180)*(r+spike_space+spike_length/3*math.sin(60*math.pi/180)))

#Scale
circle_x = [item*scale for item in circle_x]
circle_y = [item*scale for item in circle_y]
Spike_x = [item*scale for item in Spike_x]
Spike_y = [item*scale for item in Spike_y]
Spike_ny = [item*scale for item in Spike_ny]
Spike_rx = [item*scale for item in Spike_rx]
Spike_ry = [item*scale for item in Spike_ry]
Spike_nry = [item*scale for item in Spike_nry]
Spike_nrx = [item*scale for item in Spike_nrx]

# plot
if debug:
    plt.plot(circle_x,circle_y,'black',
    Spike_x,Spike_y,'black', #top
    Spike_x,Spike_ny,'black', #bot
    Spike_y,Spike_x,'black',#right
    Spike_ny,Spike_x,'black', #left
    Spike_rx, Spike_ry,'black', #topright
    Spike_nrx,Spike_ry,'black', #topleft
    Spike_nrx,Spike_nry,'black', #botleft
    Spike_rx,Spike_nry, 'black')#botright
    if halo:
        plt.plot(halo_x,halo_y,'black')
    plt.show() 