import sys
import importlib


def load_dependency(module_name, display_name, description):
    try:
        module = importlib.import_module(module_name)
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {display_name} ({version}) - {description}")
        return module
    except ImportError:
        print(f"[MISSING] {display_name} - {description}")
        print(f"Please install missing dependency: {display_name}")
        print("Using pip:")
        print("  pip install -r requirements.txt")
        print("Using Poetry:")
        print("  poetry install")
        sys.exit(1)


def main():
    print("Loading Programs\n")
    print("LOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    pandas = load_dependency(
        "pandas",
        "pandas",
        "Data manipulation ready"
    )
    numpy = load_dependency(
        "numpy",
        "numpy",
        "Numerical computation ready"
    )
    load_dependency(
        "requests",
        "requests",
        "Network access ready"
    )
    load_dependency(
        "matplotlib",
        "matplotlib",
        "Visualization ready"
    )
    pyplot = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")

    matrix_data = numpy.random.randint(0, 100, 1000)
    data_frame = pandas.DataFrame({
        "matrix_value": matrix_data
    })

    print(f"Processing {len(data_frame)} data points...")
    print("Generating visualization...\n")

    pyplot.figure()
    pyplot.plot(data_frame["matrix_value"])
    pyplot.title("Matrix Data Analysis")
    pyplot.xlabel("Data point")
    pyplot.ylabel("Matrix value")
    pyplot.savefig("matrix_analysis.png")
    pyplot.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
