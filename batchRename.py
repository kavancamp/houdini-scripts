import hou

nodes = hou.selectedNodes()
if not nodes:
    raise hou.Error("Select nodes to rename.")

prefix = "fx_"
suffix = ""
for i, n in enumerate(nodes, start=1):
    n.setName(f"{prefix}{n.type().name()}_{i:02d}{suffix}", unique_name=True)
