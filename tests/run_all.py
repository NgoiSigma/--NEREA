# Σ-NEREA / tests/run_all.py

import subprocess

def run_tests():
    print("🧪 Running all Σ‑NEREA tests...\n")
    subprocess.call(["pytest", "tests/"])
    print("\n✅ All tests complete.")

if __name__ == "__main__":
    run_tests()
