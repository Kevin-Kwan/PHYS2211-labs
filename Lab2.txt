GlowScript 3.0 VPython
## PHYS 2211 Online
## Lab 2: Motion of a Falling Object
## 2211-lab2start.py
## Last updated: 2021-01-11 EAM


## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

# Uncomment this next line if you prefer a white background
#scene.background = color.white

# Visualization (object, trail, origin)
ball = sphere(color=color.blue, radius=0.22)
trail = curve(color=color.green, radius=0.02)
origin = sphere(pos=vector(0,0,0), color=color.yellow, radius=0.04)

# Arrows to represent vector quantities in the visualization window
gravArrow = arrow(pos=ball.pos, axis=vector(0,0,0), color=color.orange)
dragArrow = arrow(pos=ball.pos, axis=vector(0,0,0), color=color.cyan)

# Graphing (if needed, you can add more plot and curve lines)
plot = graph(title="Position vs Time", xtitle="Time (s)", ytitle="Position (m)")
poscurve = gcurve(color=color.green, width=4)
plot = graph(title="Velocity vs Time", xtitle="Time (s)", ytitle="Velocity (m/s)")
velcurve = gcurve(color=color.green, width=4)


## =======================================
## SYSTEM PROPERTIES & INITIAL CONDITIONS 
## =======================================

# System Mass -- EDIT THIS NEXT LINE
ball.m = 1

# Initial Conditions -- EDIT THESE TWO LINES (as necessary)
ball.pos = vector(0,0,0)
ball.vel = vector(0,-1,0)

# Time -- EDIT THESE TWO LINES (as necessary)
t = 0            # where the clock starts
deltat = 0.001   # size of each timestep


# Interactions
# Magnitude of the acceleration due to gravity near Earth's surface
g = 9.8

# Unit vector for the positive y axis (pointing up)
jhat = vector(0,1,0)

# Proportionality constant for the magnitude of the drag force -- EDIT AS NECESSARY
# When b=0, the model is gravity only, no air resistance
b = 0



## ======================================
## CALCULATION LOOP
## (motion prediction and visualization)
## ======================================

while t < 1.0:
    # Control how fast the program runs (larger number runs faster)
    rate(100)
    
    # Calculate Net Force -- EDIT THIS NEXT LINE, ADDING MORE LINES AS NECESSARY
    Fnet = vector(10,0,0)

    # Apply the Momentum Principle (Newton's 2nd Law)
    # Update the object's velocity -- EDIT THIS NEXT LINE
    ball.vel = ball.vel + vector(0,0,0)
    # Update the object's position -- EDIT THIS NEXT LINE
    ball.pos = ball.pos + vector(0,-0.001,0)
    
    # Advance the clock
    t = t + deltat
    # Update the object's track
    trail.append(pos=ball.pos)

    # Plot position and veloity as a function of time
    # EDIT THIS NEXT LINE, or add more lines as necessary
    poscurve.plot(t,ball.pos.y)
    velcurve.plot(t,ball.vel.y)

    # Draw arrows to represent forces
    # EDIT THE NEXT FIVE LINES
    arrowscale = 1 # determines how long to draw the arrows that represent vectors
    gravArrow.pos = vector(0,0,0)
    gravArrow.axis = vector(0,0,0)
    dragArrow.pos = vector(0,0,0)
    dragArrow.axis = vector(0,0,0)

    # Uncomment this next line to print time and position in text field
    # (which you can then copy and paste into a spreadsheet)
    #print(t,ball.pos.y)
    
print("All done!")
