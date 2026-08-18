import os
import sys
import importlib.util


spec = importlib.util.spec_from_file_location("Waip_AI_VPF_001", os.path.join(os.path.dirname(__file__), "..", "main", "Waip AI VPF 0.0.1.py"))
Waip_AI_VPF_001 = importlib.util.module_from_spec(spec)
sys.modules["Waip_AI_VPF_001"] = Waip_AI_VPF_001
spec.loader.exec_module(Waip_AI_VPF_001)

data = os.path.join(os.path.dirname(__file__), "data", "Waip AI VPF 0.0.1.txt")