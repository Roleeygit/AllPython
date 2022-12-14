import imp
from turtle import position
from ursina import *
from ursina.prefabs.\
    first_person_controller\
        import FirstPersonController

app = Ursina()
Sky(texture='sky_sunset')
player = FirstPersonController()

boxes=[]
for n in range(12):
    for k in range(12):
        box = Button(
            color=color.white,
            model='cube',
            position=(k,0,n),
            texture='assets\grass',
            parent=scene,
            origin_y=0.5
        )
        boxes.append(box)






app.run()