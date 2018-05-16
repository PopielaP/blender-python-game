import bge

path = bge.logic.expandPath("//")

cont = bge.logic.getCurrentController()
own = cont.owner

current_scene = bge.logic.getCurrentScene()
print(current_scene)

#bge.logic.addScene("Home",0)

#---move menu objects from camera------------------------------------------------------

def move_menu():
    scenes = bge.logic.getSceneList()
    for scene in scenes :
        if scene.name == "Menu":
            start = scene.objects["Start"]
            save = scene.objects["Save"]
            load = scene.objects["Load"]
            quit = scene.objects["Quit"]
            text = scene.objects["Text"]
            text1 = scene.objects["Text.001"]
            text2 = scene.objects["Text.002"]
            text3 = scene.objects["Text.003"]
            start.worldPosition.x = 100
            save.worldPosition.x = 100
            load.worldPosition.x = 100
            quit.worldPosition.x = 100
            text.worldPosition.x = 100
            text1.worldPosition.x = 100
            text2.worldPosition.x = 100
            text3.worldPosition.x = 100
            quit["x"] = quit.worldPosition.x 
            bge.logic.globalDict["Menu"] = False
        elif scene.name == "Home" or scene.name == "Home1":
            scene.resume()
            

def move_back_menu():
    scenes = bge.logic.getSceneList()
    for scene in scenes :
        if scene.name == "Menu":
            start = scene.objects["Start"]
            save = scene.objects["Save"]
            load = scene.objects["Load"]
            quit = scene.objects["Quit"]
            text = scene.objects["Text"]
            text1 = scene.objects["Text.001"]
            text2 = scene.objects["Text.002"]
            text3 = scene.objects["Text.003"]
            start.worldPosition.x = 3.5
            save.worldPosition.x = 3.5
            load.worldPosition.x = 3.5
            quit.worldPosition.x = 3.5
            text.worldPosition.x = -1.7
            text1.worldPosition.x = -1.7
            text2.worldPosition.x = -1.7
            text3.worldPosition.x = -1.7
            quit["x"] = quit.worldPosition.x 
            bge.logic.globalDict["Menu"] = True 
        elif scene.name == "Home" or scene.name == "Home1":
            scene.suspend()


#---loading default scene and variables------------------------------------------------

def start(cont):
    
    scenes = bge.logic.getSceneList()
    #print(scenes)
    scene = bge.logic.getCurrentScene()
    home_scene = scenes[0]    
    
    #scene_suspended = player["current_scene"]
    #scene_suspended.suspende()
    
    mouse = cont.sensors["MouseOver"]
    mouse_left = cont.sensors["MouseLeft"]
    
    if mouse.positive and mouse_left.positive:
        #scene.end()
        move_menu()
        
        player = home_scene.objects["Player"]
        print(player["current_scene"])
        
        for scene in scenes :
            if scene.name == "Home1" or scene.name == "Home2":
                scene.replace("Home")
                print("Nowa scena: ")
                print(scene)
            elif scene.name == "Home":
                scene.restart()
        
        print("start")
        bge.logic.globalDict["player_position"] = [2.0213, 0.45624, 0.28715]
        #player.worldPosition = [2.0213, 0.45624, 0.28715]
               

#----save current scene into player["current_scene"] variable---------------------------------

def save_scene(cont):
    scene = bge.logic.getCurrentScene()
    #print("scene:"+str(scene))
    
    scenes = bge.logic.getSceneList()
    #print(scenes)
    #scene = bge.logic.getCurrentScene()
    home_scene = scenes[0]
    player = home_scene.objects["Player"]
    
    player["current_scene"] = str(scene)  
    
################## test for replacing scenes #########################################
    l = cont.sensors["L"]
    if l.positive:
        scene.replace("Home1")
######################################################################################


#---save scene name and other variables to file "save.txt"---------------------------------------

def save_game(cont):
    
    scenes = bge.logic.getSceneList()
    #print(scenes)
    scene = bge.logic.getCurrentScene()
    home_scene = scenes[0]
    player = home_scene.objects["Player"]
    click_object = home_scene.objects["ClickObject"]
    
    mouse = cont.sensors["MouseOver"]
    mouse_left = cont.sensors["MouseLeft"]

    p_position_0 = player.worldPosition[0]
    p_position_1 = player.worldPosition[1]
    p_position_2 = player.worldPosition[2]
    p_scene = player["current_scene"]
    co_position_0 = click_object.worldPosition[0]
    co_position_1 = click_object.worldPosition[1]
    co_position_2 = click_object.worldPosition[2]

    if mouse.positive and mouse_left.positive and player["current_scene"] != "":
        with open(path + "save.txt" , 'w' ) as f:
            f.write("{0},{1},{2},{3},{4},{5},{6}".format(str(p_position_0) , 
            str(p_position_1), str(p_position_2), p_scene, 
            str(co_position_0), str(co_position_1), str(co_position_2)) )
            
            #scene.end()
            move_menu()


#---load data from file/replace scene/save data to globalDict---------------------------------------

def load_game(cont):
    
    scenes = bge.logic.getSceneList()
    #print(scenes)
    scene = bge.logic.getCurrentScene()
    home_scene = scenes[0]
    player = home_scene.objects["Player"]
    click_object = home_scene.objects["ClickObject"]
    
    mouse = cont.sensors["MouseOver"]
    mouse_left = cont.sensors["MouseLeft"]
  
    if mouse.positive and mouse_left.positive:
        with open(path + "save.txt" , 'r' ) as f:
            line = f.read()
            vars = line.split(',')
            
            home_scene.replace(str(vars[3]))
            bge.logic.globalDict["player_position"] = [float(vars[0]), float(vars[1]), float(vars[2])] 
            bge.logic.globalDict["click_obj_position"]  = [float(vars[4]), float(vars[5]), float(vars[6])]
            
            #scene.end()
            move_menu()


#---load variables from globalDict - connected to player (MUST)---------------------------------------

def load_variables(cont):
    scenes = bge.logic.getSceneList()
    #print("loading")
    #print(scenes)
    
    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    print(bge.logic.globalDict["player_position"])
    own.worldPosition = bge.logic.globalDict["player_position"]