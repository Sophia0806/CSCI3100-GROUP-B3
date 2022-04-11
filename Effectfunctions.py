#condition: pause, slow, accelerated, powerful
def canteen_a(item,target):
    if target.team == 'a':
        target.heal(None,15)

def canteen_b(item,target):
    if target.team == 'b':
        target.heal(None,15)
        
def heart(item,target):
    if target.team == item.team:
        target.heal(item.user,15)

def food(item,target):
    if target.team == item.team:
        target.heal(item.user,100)
    
def dessert(item,target):
    if target.team == item.team:
        target.heal(item.user,50)
        condition = {'name':'powerful','duration':600}
        target.addcondition(condition)
    
def generate_heart(item,target):
    if target.team == item.team:
        heart = item('heart',item.user,item.pos,0)

def generate_dessert(item,target):
    if target.team == item.team:
        heart = item('dessert',item.user,item.pos,0)

def pause(item,target):
    if target.team != item.team:
        condition = {'name':'pause','duration':30}
        target.addcondition(condition)
        
def slow(item,target):
    if target.team != item.team:
        condition = {'name':'slow','duration':900}
        target.addcondition(condition)
        
def wsbeat(item,target):
    pass
    