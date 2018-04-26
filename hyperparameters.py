R =100#radius of flock
r = 50 #too close bird
boundaryThreshold = 100 #reverse the direction
v_min = 15 #minimum speed
v_max = 25 #maximum speed
x_max = 500#x boundary
x_min = -x_max
y_max = x_max #y boundary
y_min = x_min
z_max = x_max #z boundary
z_min = x_min
numberOfBirds = 80
deltaT = 0.1 #small time interval
acc_min = 50
acc_max = 100


F1whentooclose=0.15
F2whentooclose=0.15
F3whentooclose=0.7
mass=0.1

#rendering
window_width=2*y_max
window_height=2*x_max
colorblack = (0,0,0)
colorwhite = (255,255,255)
colorred = (255,198,198)
colorgreen = (209,255,196)

fps=30