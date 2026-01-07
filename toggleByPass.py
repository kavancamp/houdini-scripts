import hou

for n in hou.selectedNodes():
    n.bypass(not n.isBypassed())
