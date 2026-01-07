import hou

sel = hou.selectedNodes()
if not sel:
    raise hou.Error("Select a node.")

target = sel[0]
parent = target.parent()

# Bypass all other nodes in the same parent that are not cooking into the target chain
for n in parent.children():
    if n == target:
        n.bypass(False)
        continue
    # Don't touch locked/HDAs or nodes without outputs context
    try:
        n.bypass(True)
    except:
        pass
