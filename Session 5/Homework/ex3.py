import turtle
def draws_a_square(t,l,c):
    for i in range(4):
       t.color(c)
       t.forward(l)
       t.left(90)      
tess=turtle.Turtle()
draws_a_square(tess,100,'green')
wn=turtle.Screen()
wn.mainloop()
