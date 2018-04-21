R = 200 #radius of flock
r = 100 #too close bird
boundaryThreshold = 50 #reverse the direction
v_min = 10 #minimum speed
v_max = 20 #maximum speed
x_max = 800 #x boundary
y_max = x_max #y boundary
z_max = x_max #z boundary
numberOfBirds = 50
deltaT = 0.1 #small time interval
alpha = 10

F1whentooclose=0.1
F2whentooclose=0.1
F3whentooclose=0.8
mass=0.1

#rendering
window_width=800
window_height=800
colorblack = (0,0,0)
colorwhite = (255,255,255)
colorred = (255,198,198)
colorgreen = (209,255,196)

fps=30