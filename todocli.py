#!/usr/bin/env python3
"""Todo list terminal, save ke todo.json."""
import json, os, sys
F = os.path.expanduser("~/todo.json")
items = json.load(open(F)) if os.path.exists(F) else []
if len(sys.argv) > 1 and sys.argv[1] == "add":
      items.append({"text": " ".join(sys.argv[2:]), "done": False})
elif len(sys.argv) > 2 and sys.argv[1] == "done":
      items[int(sys.argv[2]) - 1]["done"] = True
  for i, it in enumerate(items, 1):
        print(f"[{'x' if it['done'] else ' '}] {i}. {it['text']}")
    json.dump(items, open(F, "w"), indent=1)
