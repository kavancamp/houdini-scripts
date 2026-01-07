import hou

sel = hou.selectedNodes()
if not sel:
    raise hou.Error("Select a SOP node to cache.")

sop = sel[0]
obj = hou.node("/obj")
geo = sop.parent()  # usually /obj/geo1

ropnet = geo.node("ropnet1") or geo.createNode("ropnet", "ropnet1")
rop = ropnet.createNode("rop_geometry", f"cache_{sop.name()}")

rop.parm("soppath").set(sop.path())
rop.parm("sopoutput").set(f"$HIP/geo/{sop.name()}.$F4.bgeo.sc")
rop.parm("trange").set(0)  # render current frame
rop.moveToGoodPosition()
rop.setSelected(True, clear_all_selected=True)
