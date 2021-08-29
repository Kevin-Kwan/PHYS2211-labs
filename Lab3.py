GlowScript 2.9 VPython
## PHYS 2211 Online
## Lab 3: Black Hole
## 2211-lab3start.py
## Last updated: 2021-01-11 EAM


## =============================================================== 
## EDIT THIS ONE LINE: TYPE YOUR GT EMAIL ADDRESS HERE, IN QUOTES 
## ===============================================================
seed="gpburdell@gatech.edu"




# =================================================== #
# v v v v DO NOT ALTER THE FOLLOWING SECTIONS v v v v #
# =================================================== #

# Generate ellipse path with de la Hire paramaterization
def generateEllipse(a,b,focusOrigin=False,deltat=0.01):
    tlist = []
    t = 0
    while t < 2*pi:
        tlist.append(t)
        t+=deltat
    x = [a*cos(t) for t in tlist]
    y = [b*sin(t) for t in tlist]
    c = sqrt(a**2-b**2)
    if focusOrigin:
        # shift the ellipse in the +x direction
        x = [xx + c for xx in x]
    return(x,y)

def triangleArea(A,B,C=vector(0,0,0)):
    # A,B,C vectors of vertices, S is area
    AB = B-A
    AC = C-A
    S = 0.5*mag(cross(AB,AC))
    return(S)

def randomizer(seedval):
    emailchars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                    "p","q","r","s","t","u","v","w","x","y","z","1","2","3","4",
                    "5","6","7","8","9","0","!","#","$","%","&","'","*","+","-",
                    "/","=","?","^","_","`","{","|","}","~","."]
    if seedval[0] in emailchars:
        index = emailchars.index(seedval[0].lower())*1.0
    else:
        index = 19 # default if we get a weird character
    randval = index/len(emailchars)
    return(randval)

# Populate this trajectory 
def generateTrajectoryKepler(seed):
    x = []
    y = []
    b = 50*(1+randomizer(seed[1]))
    a = b+5*(1+randomizer(seed[0]))
    
    deltat = 0.00001
    ex,ey = generateEllipse(a*5e10,b*5e10,focusOrigin=True,deltat=deltat)
    N = len(ex)
    initStart = round(0.5*randomizer(seed[2])*N)
    initEnd = initStart + 1000 + round(randomizer(seed[3])*30)
    # start at a random point, then go another few points
    x.append(ex[initStart],ex[initEnd])
    y.append(ey[initStart],ey[initEnd])
    A0 = triangleArea(vector(x[0],y[0],0),vector(x[1],y[1],0))

    ii = 0
    area = 0
    while ii < N:
        index = (initEnd+ii)%N
        A = vector(ex[index],ey[index],0)
        index = (index+1)%N
        B = vector(ex[index], ey[index],0)
        area = area + triangleArea(A,B)
        if area >= A0:
            x.append(ex[index])
            y.append(ey[index])
            area = 0
        ii += 1
    return([x,y])

# Generate trajectory customized to seed value
[X,Y] = generateTrajectoryKepler(seed)

# =============================================== #
# ^ ^ ^ ^ DO NOT ALTER THE ABOVE SECTIONS ^ ^ ^ ^ #
# =============================================== #




## =====================================
## VISUALIZATION & GRAPH INITIALIZATION
## =====================================

# White background so the black hole is visible
scene.background = color.white

# Visualization (object, trail, origin)
star = sphere(color=color.yellow, radius=3e11)
trail = curve(color=color.green)
origin = sphere(pos=vector(0,0,0), color=color.black, radius=3e11)

# Arrows to represent vector quantities in the visualization window
arrowFnet = arrow(pos=star.pos, axis=vector(0,0,0), color=color.orange)
arrowFnet_par = arrow(pos=star.pos, axis=vector(0,0,0), color=color.magenta)
arrowFnet_perp = arrow(pos=star.pos, axis=vector(0,0,0), color=color.cyan)


## =======================================
## SYSTEM PROPERTIES & INITIAL CONDITIONS 
## =======================================

# Gravitational constant
G = 6.7e-11

# Mass of the star -- EDIT THIS LINE
star.m = 1 

# Time interval between imported data points -- EDIT THIS LINE
deltat = 1

# Time for first observation data point (default t=0)
t = 0

# Calculate velocity from data
Xvel = [0 for i in range(len(X)-1)]  # list that will hold calculated x components of velocity
Yvel = [0 for i in range(len(X)-1)]  # list that will hold calculated y components of velocity

idx = 0
while idx < (len(X)-1):
    # compute x component of velocity
    deltaX = X[idx+1] - X[idx]
    Xvel[idx] = deltaX/deltat
    # compute y component of velocity 
    deltaY = Y[idx+1] - Y[idx]
    Yvel[idx] = deltaY/deltat
    idx = idx + 1

t = t + deltat 



## =======================================
## CALCULATION LOOP
## (calculate net force from motion data)
## =======================================

idx=1

while idx <(len(X)-1):  #iterate over data values
    # Control how fast the simulation runs (larger number runs faster)
    rate(50) 

    # Use velocity components define initial and final velocities
    v_init = vector(Xvel[idx-1],Yvel[idx-1],0)
    v_final = vector(Xvel[idx],Yvel[idx],0)

    # Compute initial and final momentum vectors -- EDIT THESE TWO LINES
    p_init = vector(0,0,0)
    p_final = vector(0,0,0)
    
    # Calculate star's change in velocity and change in momentum -- EDIT THESE TWO LINES
    deltav = vector(0,0,0)
    deltap = vector(0,0,0)

    # Calculate dp/dt (call it dpdt) -- EDIT THIS LINE
    dpdt = vector(0,0,0)

    # Use Newton's 2nd Law to calculate Fnet -- EDIT THIS LINE
    Fnet = vector(0,0,0)

    # Calculate dp/dt parallel (to phat) -- EDIT THESE THREE LINES
    phat = vector(0,0,0)
    dmagpdt = vector(0,0,0)
    dpdt_par = vector(0,0,0)

    # Use Newton's 2nd Law to calculate Fnet_par -- EDIT THIS LINE
    Fnet_par = vector(0,0,0)

    # Calculate dp/dt perpendicular (to phat) -- EDIT THIS LINE
    dpdt_perp = vector(0,0,0)

    # Use Newton's 2nd Law to calculate Fnet_perp -- EDIT THIS LINE
    Fnet_perp = vector(0,0,0)

    # Calculate the mass of the black hole 
    # EDIT AND ADD LINES AS NEEDED
    mBH = 1
    print(mBH)

    # Update current position and velocity and show the object's current track
    star.pos = vector(X[idx],Y[idx],0)
    trail.append(pos=star.pos)

    # Draw arrows to represent forces (Fnet, Fnet_par, Fnet_perp)
    # EDIT THE NEXT SEVEN LINES
    arrowscale = 1      # determines how long to draw the arrows that represent vectors
    arrowFnet.pos = vector(0,0,0)
    arrowFnet.axis = vector(0,0,0)
    arrowFnet_par.pos = vector(0,0,0)
    arrowFnet_par.axis = vector(0,0,0)
    arrowFnet_perp.pos = vector(0,0,0)
    arrowFnet_perp.axis = vector(0,0,0)
    
    # Advance the clock
    t = t + deltat
    # Advance the index to step through all data points
    idx = idx + 1

# Printing the forces
print("|Fnet|=",mag(Fnet))
print("|Fnet_par|=",mag(Fnet_par))
print("|Fnet_perp|=",mag(Fnet_perp))

print("All done!")


