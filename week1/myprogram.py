#!/usr/bin/python

# Import relevant classes
from particles import Particle, Position, Velocity

# Create two particles
p1 = Particle(1.0, Position(1,2,3), Velocity(1,2,3))
p2 = Particle(2.0, Position(3,2,1), Velocity(3,2,1))

# Calculate the force between the particles
print Particle.force(p1,p2), 'N'
