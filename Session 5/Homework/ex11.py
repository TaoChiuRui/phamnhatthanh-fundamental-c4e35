
def is_inside(x,y,x1,y1,x2,y2):
    if x>x1 and x<(x1+x2) and y>y1 and y<(y1+y2):
        return True
    else:
        return False
print(is_inside(200,120,140,60,100,200))