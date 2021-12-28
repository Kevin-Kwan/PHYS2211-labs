GlowScript 3.2 VPython
## PHYS 2211
## Lab 5: Choose Your Own Adventure: The Human Rocket
## Kevin Kwan
## Most of the code is based of the falling object lab that we did in the past.

## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

# Object and trail and earth
ball = sphere(color=color.blue, radius = 500)
trail = curve(color=color.green, radius = 200)
#earth = sphere(color=color.white, texture="https://upload.wikimedia.org/wikipedia/commons/d/d9/Ocean-wind-atmosphere-ice-arctic-terrain-1123814-pxhere.jpg", radius = 6.3781e6)
earth = sphere(color = color.black, radius = 300)
# Graph
plot = graph(title="Position vs Time", xtitle="Time (s)", ytitle="Position (m)")
poscurve = gcurve(color=color.green, width=4)
plot = graph(title="Velocity vs Time", xtitle="Time (s)", ytitle="Velocity (m/s)")
velcurve = gcurve(color=color.green, width=4)

## =======================================
## SYSTEM PROPERTIES & INITIAL CONDITIONS 
## =======================================

# Earth's mass
earth.m = 5.97219e24
# Earth's radius
earth.r = 6.3781e6
# Universal Gravitational constant
G = 6.67408e-11
# yhat unit vector in the negative y direction (since he's going down)
yhat = vector(0,-1,0)


# Initial conditions
initpos = vector(0,38969.4,0) # initial position (m)
ball.pos = vector(0,38969.4,0) # initial position (m)
ball.vel = vector(0,0,0) # starts at rest

# System mass
# he is 73kg, his suit was 27kg
ball.m = 73 + 27

# Time start and deltat
t=0
deltat = 0.01

b = 710

Fnet = 0
Fgrav = 0

scene.waitfor("textures")

## ======================================
## CALCULATION LOOP
## (motion prediction and visualization)
## ======================================
# He pulled his chute at 259 seconds
while t < 259:
    rate(10000)
    # Calculate Net Force
    Fdrag = -norm(ball.vel)*b*(1/(ball.pos.y))*(mag(ball.vel)**2)#(initpos.y-ball.pos.y)
    Fgrav = yhat*((G*ball.m*earth.m)/((ball.pos.y+earth.r)**2))
    Fnet = Fgrav+Fdrag
    
    # Apply the Momentum Principle
    # Update object velocity
    ball.vel = ball.vel + (Fnet/ball.m) * deltat
    # Update object position
    ball.pos = ball.pos + ball.vel * deltat
    # Advance the clock
    t = t + deltat
    # Update the object's track
    trail.append(pos=ball.pos)
    
    # Plot position and veloity as a function of time
    poscurve.plot(t,ball.pos.y)
    velcurve.plot(t,ball.vel.y)
    if(t%2<0.01):
        print(t, ball.vel.y)

    
print("Fnet: ", Fnet)
print("Y Pos Above Earth: ", ball.pos)
    

