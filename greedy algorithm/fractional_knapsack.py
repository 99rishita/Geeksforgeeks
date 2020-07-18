def fractional(capacity, wt, val):
    
    density = []
    for i in range(0, len(val)):
        density[i] =  val[i] // wt[i]
        density.sort(reversed=True)
