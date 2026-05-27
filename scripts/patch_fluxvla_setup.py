"""Patch FluxVLA's setup.py to remove CUDA extension builds."""
import re
from pathlib import Path

setup_py = Path("/opt/FluxVLA/setup.py")
text = setup_py.read_text()
text = re.sub(r"ext_modules=\[.*?\]", "ext_modules=[]", text, flags=re.DOTALL)
text = re.sub(r"cmdclass=\{.*?\}", "cmdclass={}", text, flags=re.DOTALL)
setup_py.write_text(text)
print("Patched setup.py: removed ext_modules + cmdclass")
