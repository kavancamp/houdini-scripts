# Houdini script to create an Object Merge node that merges selected nodes
sel = hou.selectedNodes()

if len(sel) >= 1:
    curPath = sel[0].parent()
    pos = sel[0].position() + hou.Vector2(0, -1)

    # Create the object_merge node
    mkMerge = curPath.createNode("object_merge")
    mkMerge.setPosition(pos)

    # Attempt to name based on first node
    try:
        mkMerge.setName(sel[0].name() + "_merge")
    except:
        mkMerge.setName(sel[0].name() + "_merge1")

    mkMerge.parm("xformtype").set(1)  # Set "Into This Object" transform type

    # Set number of inputs to number of selected nodes
    mkMerge.parm("numobj").set(len(sel))

    # Set each objpath parameter
    for idx, node in enumerate(sel):
        objPath = node.path()
        mkMerge.parm(f"objpath{idx+1}").set(objPath)