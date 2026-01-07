import hou

node = hou.selectedNodes()[0]
ptg = node.parmTemplateGroup()

toggle = hou.ToggleParmTemplate("use_cache", "Use Cache", default_value=False)
path = hou.StringParmTemplate("cache_path", "Cache Path", 1, default_value=("",))
path.setStringType(hou.stringParmType.FileReference)

ptg.append(toggle)
ptg.append(path)

node.setParmTemplateGroup(ptg)
