
import pandas as pd

f = open("Luxottica.dat", "w")

# Read the Excel sheets
t = pd.read_excel("15.Luxottica_prodmix.xlsx", "time")
p = pd.read_excel("15.Luxottica_prodmix.xlsx", "Price")
d = pd.read_excel("15.Luxottica_prodmix.xlsx", "Demand")
v = pd.read_excel("15.Luxottica_prodmix.xlsx", "MaxPercVar")
c = pd.read_excel("15.Luxottica_prodmix.xlsx", "UnitCost")
A = pd.read_excel("15.Luxottica_prodmix.xlsx", "Availability")

# Sets
f.write("set P:= \n")
d.Product.to_csv(f, sep=" ", header=False, index=False)
f.write("; \n")

f.write("set V:= \n")
variations = p.Variation.drop_duplicates()
variations.to_csv(f, sep=" ", header=False, index=False)
f.write("; \n")

f.write("set R:= \n")
c.Resource.to_csv(f, sep=" ", header=False, index=False)
f.write("; \n")

f.write("set W:= \n")
f.write("RB3603 FlashLenses Collection Mirror PolarizedLenses\n")
f.write("; \n")

# Parameters

# Price
f.write("param p:= \n")
p.to_csv(f, sep=" ", columns=["Product", "Variation", "Price"],
         header=False, index=False)
f.write("; \n")

# Demand
f.write("param d:= \n")
d.to_csv(f, sep=" ", columns=["Product", "Demand"],
         header=False, index=False)
f.write("; \n")

# Time required
f.write("param t:= \n")
t.to_csv(f, sep=" ", columns=["Resource", "Product", "Variation", "Time"],
         header=False, index=False)
f.write("; \n")

# Maximum percentage variation
f.write("param v:= \n")
v.to_csv(f, sep=" ", columns=["Product", "MaxPercVar"],
         header=False, index=False)
f.write("; \n")

# Cost per minute
f.write("param c:= \n")
c.to_csv(f, sep=" ", columns=["Resource", "UnitCost"],
         header=False, index=False)
f.write("; \n")

# Resource availability
f.write("param A:= \n")
A.to_csv(f, sep=" ", columns=["Resource", "Availability"],
         header=False, index=False)
f.write("; \n")

f.close()
