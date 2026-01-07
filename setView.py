import hou

scene = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
if scene:
    vp = scene.curViewport()
    settings = vp.settings()
    settings.displayPointNumbers(True)
    settings.displayPointMarkers(True)
    settings.displayNormals(False)
