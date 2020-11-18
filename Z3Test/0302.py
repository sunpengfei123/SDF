from z3 import *

v1,v2,v3 = Ints('v1 v2 v3')
x1,x2,x3 = Ints('x1 x2 x3')
e1,e2,e3 = Ints('e1 e2 e3')
w = Int('w')

#solver = Solver()#创建一个求解器对象
solver = Optimize()
solver.add(If(And(x1==x2,x1==0),Or(v1>=v2+5,v2>=v1+3),v1>=0))
solver.add(If(And(x1==x2,x1==1),Or(v1>=v2+3,v2>=v1+2),v1>=0))

solver.add(If(And(x3==x2,x3==0),Or(v3>=v2+5,v2>=v3+6),v1>=0))
solver.add(If(And(x3==x2,x3==1),Or(v3>=v2+3,v2>=v3+3),v1>=0))

solver.add(If(And(x1==x3,x1==0),Or(v1>=v3+6,v3>=v1+3),v1>=0))
solver.add(If(And(x1==x3,x1==1),Or(v1>=v3+3,v3>=v1+2),v1>=0))

solver.add(If(And(x1!=x2,x2!=x3),Or(e1>=e2+1,e2>=e1+1),v1>=0))
solver.add(If(And(x1!=x2,x1!=x3),Or(e1>=e3+1,e3>=e1+1),v1>=0))
solver.add(If(And(x1!=x3,x2!=x3),Or(e3>=e2+1,e2>=e3+1),v1>=0))

solver.add(If(x1!=x2,v2>=e1+1,v2>=e1))
solver.add(e1>=v1+3*(1-x1)+2*x1)
solver.add(e2>=v2+5*(1-x2)+3*x2)
solver.add(e3>=v3+6*(1-x3)+3*x3)

solver.add(v1>=0)
solver.add(v2>=0)
solver.add(v3>=0)

solver.add(x1>=0)
solver.add(x2>=0)
solver.add(x3>=0)

solver.add(x1<=1)
solver.add(x2<=1)
solver.add(x3<=1)

solver.add(e1>=0)
solver.add(e2>=0)
solver.add(e3>=0)

solver.add(If(x1==x2,w>=e1,w>=e1+1))
solver.add(If(x3==x2,w>=e2,w>=e2+1))
solver.add(If(x1==x3,w>=e3,w>=e3+1))

solver.minimize(w)

print ("asserted constraints...")
for c in solver.assertions():
    print (c)


if solver.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = solver.model() #model()方法得到解
    print(ans)
else:
    print("no ans!")
