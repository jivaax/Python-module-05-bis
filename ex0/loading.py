pandas_available = False
numpy_available = False

print("\nREAGENT STATUS: Loading reagents...")

print("\nChecking dependencies:")
try:
    import pandas
    pandas_available = True
    print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
except ImportError:
    print("\n[MISSING] pandas")
    print("Install with pip: pip install pandas")
    print("Install with Poetry: poetry add pandas")

try:
    import numpy
    numpy_available = True
    print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
except ImportError:
    print("\n[MISSING] numpy")
    print("Install with pip: pip install numpy")
    print("Install with Poetry: poetry add numpy")

print("\npip vs Poetry:\nrequirements.txt declares what to install; "
      "pip resolves it at install time. \npyproject.toml declares the same"
      " constraints, and Poetry pins the resolved \nversions in poetry.lock so"
      " every install is identical.")

if pandas_available and numpy_available:
    print("\nAll reagents present and accounted for.")
