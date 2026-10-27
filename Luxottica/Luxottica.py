
from pyomo.environ import *

model = AbstractModel()

# Sets
model.P = Set()
model.V = Set()
model.R = Set()
model.W = Set(within=model.V)

# Parameters
model.p = Param(model.P, model.V)
model.d = Param(model.P)
model.t = Param(model.R, model.P, model.V)
model.v = Param(model.P)
model.c = Param(model.R)
model.A = Param(model.R)

# Decision variables
model.x = Var(model.P, model.V, domain=NonNegativeReals)

# Objective function
def obj(model):
    return sum(model.p[i,j] * model.x[i,j]
               for i in model.P for j in model.V) - sum(
        model.c[r] * model.t[r,i,j] * model.x[i,j]
        for r in model.R for i in model.P for j in model.V
    )
model.objfn = Objective(rule=obj, sense=maximize)

# Demand constraint
def demcons(model, i):
    return sum(model.x[i,j] for j in model.V) <= model.d[i]
model.demconstr = Constraint(model.P, rule=demcons)

# Resource availability constraint
def resourcecons(model, r):
    return sum(model.t[r,i,j] * model.x[i,j]
               for i in model.P for j in model.V) <= model.A[r]
model.resourceconstr = Constraint(model.R, rule=resourcecons)

# Blending constraint
def blendcons(model, i):
    return sum(model.x[i,j] for j in model.W) <= model.v[i] * sum(
        model.x[i,j] for j in model.V
    )
model.blendconstr = Constraint(model.P, rule=blendcons)
