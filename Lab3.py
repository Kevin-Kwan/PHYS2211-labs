GlowScript 3.1 VPython
## PHYS 2211 Online
## Lab 3: Black Hole
## 2211-lab3start.py
## Last updated: 2021-01-11 EAM


## =============================================================== 
## EDIT THIS ONE LINE: TYPE YOUR GT EMAIL ADDRESS HERE, IN QUOTES 
## ===============================================================
seed="kkwan9@gatech.edu"




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

# Mass of the star 
star.m = 2.0e30  # given in the lab instructions

# Time interval between imported data points
deltat = 86400 # number of seconds in a day

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
    rate(100) 

    # Use velocity components define initial and final velocities
    v_init = vector(Xvel[idx-1],Yvel[idx-1],0)
    v_final = vector(Xvel[idx],Yvel[idx],0)

    # Compute initial and final momentum vectors 
    p_init = star.m*v_init # pi=mvi
    p_final = star.m*v_final # pf=mvf
    
    # Calculate star's change in velocity and change in momentum 
    deltav = v_final-v_init # change in v = vf-vi
    deltap = p_final-p_init # change in p = pf-pi

    # Calculate dp/dt (call it dpdt)
    dpdt = deltap/deltat 

    # Use Newton's 2nd Law to calculate Fnet 
    Fnet = dpdt 

    # Calculate dp/dt parallel (to phat) -- EDIT THESE THREE LINES
    phat = p_init/mag(p_init) # unit vector of p
    dmagpdt = (mag(p_final)-mag(p_init))/deltat
    dpdt_par = dmagpdt*phat

    # Use Newton's 2nd Law to calculate Fnet_par -- EDIT THIS LINE
    Fnet_par = dpdt_par

    # Calculate dp/dt perpendicular (to phat) -- EDIT THIS LINE
    dpdt_perp = dpdt-dpdt_par

    # Use Newton's 2nd Law to calculate Fnet_perp -- EDIT THIS LINE
    Fnet_perp = dpdt_perp

    # Calculate the mass of the black hole 
    mBH = ((mag(Fnet)*mag(star.pos)*mag(star.pos))/(G*star.m))
    print(mBH)
    

    # Update current position and velocity and show the object's current track
    star.pos = vector(X[idx],Y[idx],0)
    trail.append(pos=star.pos)

    # Draw arrows to represent forces (Fnet, Fnet_par, Fnet_perp)
    # EDIT THE NEXT SEVEN LINES
    arrowscale = 2e-17     # determines how long to draw the arrows that represent vectors
    arrowFnet.pos = star.pos
    arrowFnet.axis = Fnet*arrowscale
    arrowFnet_par.pos = star.pos
    arrowFnet_par.axis = Fnet_par*arrowscale
    arrowFnet_perp.pos = star.pos
    arrowFnet_perp.axis = Fnet_perp*arrowscale
    
    # Advance the clock
    t = t + deltat
    # Advance the index to step through all data points
    idx = idx + 1

# Printing the forces
print("|Fnet|=",mag(Fnet))
print("|Fnet_par|=",mag(Fnet_par))
print("|Fnet_perp|=",mag(Fnet_perp))

print("All done!")


