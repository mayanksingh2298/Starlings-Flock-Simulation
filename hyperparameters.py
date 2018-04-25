R =500#radius of flock
r = 20 #too close bird
boundaryThreshold = 20 #reverse the direction
v_min = 20 #minimum speed
v_max = 30 #maximum speed
x_max = 500#x boundary
x_min = -500
y_max = x_max #y boundary
y_min = x_min
z_max = x_max #z boundary
z_min = x_min
numberOfBirds = 50
deltaT = 0.1 #small time interval
acc_min = 0
acc_max = 60


F1whentooclose=0.1
F2whentooclose=0.1
F3whentooclose=0.8
mass=0.1

#rendering
window_width=2*y_max
window_height=2*x_max
colorblack = (0,0,0)
colorwhite = (255,255,255)
colorred = (255,198,198)
colorgreen = (209,255,196)

fps=30