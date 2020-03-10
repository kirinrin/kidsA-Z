import os
import json
from pprint import pprint

def search(root):
    folders = []
    items = [name for name in os.listdir(root) if (os.path.isdir(os.path.join(root, name)) or name.endswith('.swf'))]
    items.sort()
    for item in items:
        path = os.path.join(root, item)
        if os.path.isdir(path):
            folders.append({"name": item, "sub": search(path)})
        else:
            folders.append({"name": item, "uri": path})

    return folders


basePath = "public"
result = search(basePath)
json_result = json.dumps(result)
print(json_result)

