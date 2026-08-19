import os
import sys
import importlib.util


spec = importlib.util.spec_from_file_location("main", os.path.join(os.path.dirname(__file__), "..", "main", "mian.py"))
main = importlib.util.module_from_spec(spec)
sys.modules["main"] = main
spec.loader.exec_module(main)

data = os.path.join(os.path.dirname(__file__), "data", "Waip AI VPF 0.0.1.txt")

if __name__ == "__main__":
    print("向量概率(Vector Probabilistic Framework, VPF)马上运行")
    while True:
        text = input()
        if text == "exit":
            break
        print(f"测试体：{main.Waip_AI_VPF(text)}")
