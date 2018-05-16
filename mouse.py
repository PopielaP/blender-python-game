import bge
from bge import render

#render.showMouse(1)
mouse = bge.logic.mouse

def cursor(cont):
    cont = bge.logic.getCurrentController()
    own = cont.owner
    mouse_over = cont.sensors["MouseOverCursor"]
    hit_position = mouse_over.hitPosition
    own.worldPosition.x = hit_position.x
    own.worldPosition.y = hit_position.y
    own.worldPosition = mouse_over.hitPosition

def move_map(cont):
    
    cont = bge.logic.getCurrentController()
    own = cont.owner
    scene = bge.logic.getCurrentScene()
    
    map = scene.objects["Plane"]
    camera = scene.objects["Camera"]
    #arrow = scene.objects["Arrow"]
    
    #mouse_over = cont.sensors["MouseOver"]
    
    #mouse_position = mouse_over.hitPosition
    map["mpx"] = mouse.position[0]
    map["mpy"] = mouse.position[1]
    
    if mouse.position[0]< 0.08:
        camera.position.x -= 0.1
    if mouse.position[0]> 0.9:
        camera.position.x += 0.1
    if mouse.position[1] < 0.08:
        camera.position.y += 0.1
    if mouse.position[1] > 0.9:
        camera.position.y -= 0.1

def move(cont):

    cont = bge.logic.getCurrentController()
    own = cont.owner
    scene = bge.logic.getCurrentScene()
    
    click_object = scene.objects["ClickObject"]
    
    mouse_over = cont.sensors["MouseOver"]
    mouse_click = cont.sensors["MouseClick"]
    
    if mouse_over.positive:
        own.worldPosition = mouse_over.hitPosition
        own.setVisible(1)
        object_position = mouse_over.hitPosition
        if mouse_click.positive:
            click_object.position.x = object_position.x
            click_object.position.y = object_position.y
            click_object.position.z = object_position.z + 1
    else:
        own.setVisible(0)
        
def check(cont):
    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    scene = bge.logic.getCurrentScene()
    skeleton = scene.objects["MeSkeleton"]
    
    collision = cont.sensors["Collision"]
    steering = cont.actuators["Steering"]
    
    if collision.positive:
        cont.deactivate(steering)
        skeleton.playAction('Waiting', 0, 480, layer=0, priority=1,play_mode=bge.logic.KX_ACTION_MODE_LOOP)
        own["hit"] = True
    else:
        cont.activate(steering)
        skeleton.playAction('walk', 41, 63, layer=0, priority=1, blendin=0,layer_weight=0.5, play_mode=bge.logic.KX_ACTION_MODE_LOOP)
        own["hit"] = False
    

