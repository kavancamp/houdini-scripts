import hou

def make_null():
    nodes = hou.selectedNodes()
    if not nodes:
        hou.ui.displayMessage("Select a node first.")
        return

    src = nodes[0]
    parent = src.parent()
    null = parent.createNode("null", node_name=f"OUT_{src.name()}")
    null.setInput(0, src)
    null.setDisplayFlag(True)
    null.setRenderFlag(True)
    null.setPosition(src.position() + hou.Vector2(2, 0))
    null.setColor(hou.Color((0.2, 0.6, 1.0)))
    null.setUserData("nodeshape", "cloud")
    null.moveToGoodPosition()
    null.setSelected(True, clear_all_selected=True)

make_null()
