R = 125 #radius of flock
r = 30 #too close bird
boundaryThreshold = 50 #reverse the direction
v_min = 15 #minimum speed
v_max = 20 #maximum speed
x_max = 1200 #x boundary
y_max = x_max #y boundary
z_max = x_max #z boundary
numberOfBirds = 90
deltaT = 0.1 #small time interval
acc_min = 0
acc_max = 40


F1whentooclose=0.1
F2whentooclose=0.1
F3whentooclose=0.8
mass=0.1

#rendering
window_width=y_max
window_height=x_max
colorblack = (0,0,0)
colorwhite = (255,255,255)
colorred = (255,198,198)
colorgreen = (209,255,196)

fps=30