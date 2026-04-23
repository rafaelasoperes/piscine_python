import sys


def main():
    if len(sys.argv) < 2:
        return

    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            print("---")
            for i, line in enumerate(lines, 1):
                print(f"[FRAGMENT {i:03d}] {line.strip()}")

            print("---")
            print(f"File '{filename}' closed.\n")
            print("Transform data:\n---")
            for i, line in enumerate(lines, 1):
                print(f"[FRAGMENT {i:03d}] {line.strip()}#")
            print("---")

    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        return

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename = sys.stdin.readline().strip()

    if new_filename:
        print(f"Saving data to '{new_filename}'")
        try:
            with open(new_filename, 'w'):
                pass
        except Exception as e:
            sys.stderr.write("[STDERR] Error "
                             f"opening file '{new_filename}': {e}\n")
            print("Data not saved.")


if __name__ == "__main__":
    main()
