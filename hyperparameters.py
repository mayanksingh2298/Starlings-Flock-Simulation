"""
This file contains all the hyperparameters used in running the simulation:
R : birds within this distance are considered in my flock
r : birds within this distance are too close
boundaryThreshold : threshold from the window boundary
v_min : min speed
v_max : max speed
x_max : maximum x
x_min : maximum x
y_max : maximum y
y_min : minimum y
z_max : maximum z
z_min : minimum z
numberOfBirds : total number of birds to simuate
deltaT : small time interval
acc_min : minimum acceleration
acc_max : maximum acceleration
F1whentooclose : F1 value when too close to any bird
F2whentooclose : F2 value when too close to any bird
F3whentooclose : F3 value when too close to any bird
mass : mass of bird
window_width : width of screen
window_height : height of screen 
fps : fps of screen
"""

R =100#radius of flock
r = 50 #too close bird
boundaryThreshold = 0 #reverse the direction
v_min = 15 #minimum speed
v_max = 25 #maximum speed
x_max = 500#x boundary
x_min = -x_max
y_max = x_max #y boundary
y_min = x_min
z_max = x_max #z boundary
z_min = x_min
# z_max = 0 #z boundary
# z_min = 0
numberOfBirds = 100
deltaT = 0.15#small time interval
acc_min = 5
acc_max = 10


F1whentooclose=0.25
F2whentooclose=0.25
F3whentooclose=0.5
mass=0.1

#rendering
window_width=2*y_max
window_height=2*x_max
fps=30
