# Task 1 - installation check
# Run this after installing everything to see what's working and what's missing.
# Install steps (run in terminal):
#   Anaconda3  -> https://www.anaconda.com/  (download installer and run it)
#   PyTorch    -> pip install torch   (or use the command from pytorch.org/get-started/locally)
#   TensorFlow -> pip install tensorflow
#   VSCode     -> https://code.visualstudio.com/
#   PyCharm    -> https://www.jetbrains.com/pycharm/  (community edition)

import sys
import importlib

print("python version:", sys.version.split()[0])
print()

libs = ["numpy", "pandas", "matplotlib", "seaborn", "sklearn", "torch", "tensorflow"]

for name in libs:
    try:
        mod = importlib.import_module(name)
        version = getattr(mod, "__version__", "unknown version")
        print(f"[ok]      {name} {version}")
    except ImportError:
        print(f"[missing] {name}  -> pip install {name}")
