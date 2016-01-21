class Position:
    '''
    Define the position components for a particle.
    '''
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

class Velocity:
    '''
    Define the velocity components for a particle.
    '''
    def __init__(self, vx=0.0, vy=0.0, vz=0.0):
        self.vx = vx
        self.vy = vy
        self.vz = vz

class Particle:
    '''
    Define the mass, position, and velocity for a particle 
    and compute the force between them.
    '''
    def __init__(self, mass=1.0, pos=Position(), vel=Velocity()):
        self.mass = mass
        self.pos = pos
        self.vel = vel
    
    @staticmethod
    def force(p1,p2):
        G = 6.67e-11
        F = G * p1.mass * p2.mass / ((p1.pos.x - p2.pos.x)**2 + (p1.pos.y-p2.pos.y)**2 + (p1.pos.z-p2.pos.z)**2)
        return F
