from ursina import*
import random

app = Ursina()
camera.orthographic = True
camera.fo = 40

car  = Entity(
    model = 'quad',
    texture = 'assets/car2.png',
    collidar = 'box',
    scale= (5,10),
    #rotation_z = -90
    )

road1  = Entity(
    model = 'quad',
    texture = 'assets/road2.jpg',
   
    scale= 45,
    #z=1
    rotation_z = -90
    )
road2 = duplicate(road1, y=15)
pair = [road1, road2]

enemies = []
def newEnemy():
     val  =random.uniform(-2,2)
     new = duplicate(
          car,
          texture = 'assets/car3.png',
          x = 2*val,
          y=25,
          color = color.random_color()
        )


def update():
    car.x -= held_keys['a']*5*time.dt
    car.x += held_keys['d']*5*time.dt
    for road in pair:
        road.y -= 6*time.dt
        if road.y < -15:
               road.y += 30
app.run()
