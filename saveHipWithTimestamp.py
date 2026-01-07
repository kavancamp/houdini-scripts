import hou
from datetime import datetime
import os

hip = hou.hipFile.name()
if hip == "untitled.hip":
    base = "houdini_scene"
    folder = hou.expandString("$HIP")
else:
    folder = os.path.dirname(hip)
    base = os.path.splitext(os.path.basename(hip))[0]

stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
new_path = os.path.join(folder, f"{base}_{stamp}.hip")
hou.hipFile.save(new_path)
hou.ui.displayMessage(f"Saved: {new_path}")
