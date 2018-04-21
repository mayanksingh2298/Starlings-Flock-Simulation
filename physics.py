def force(mass,v1,v2,dt):
	return [mass*(v2[0]-v1[0])/dt,mass*(v2[1]-v1[1])/dt,mass*(v2[2]-v1[2])/dt]

def angularMomentum(mass,r,v):
	return [mass*(r[1]*v[2]-r[2]*v[1]),mass*(r[0]*v[2]-r[2]*v[0]),mass*(r[0]*v[1]-r[1]*v[0])]

def power(f,v):
	return (f[0]*v[0]+f[1]*v[1]+f[2]*v[2])