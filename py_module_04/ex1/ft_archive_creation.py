import sys
import typing


def add_archive_char(text: str) -> str:
    result: str = ""
    i: int = 0

    while i < len(text):
        if text[i] == "\n":
            result += "#\n"
        else:
            result += text[i]
        i += 1

    if len(text) > 0 and text[len(text) - 1] != "\n":
        result += "#"

    return result


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file: typing.IO[str] = open(filename, "r")
        print("---")
        content: str = file.read()
        print(content, end="")
        print("\n---")
        file.close()
        print(f"File '{filename}' closed.")

        print("\nTransform data:")
        print("---")
        new_content: str = add_archive_char(content)
        print(new_content, end="")
        print("\n---")

        new_filename: str = input("Enter new file name (or empty): ")

        if new_filename == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_filename}'")
            new_file: typing.IO[str] = open(new_filename, "w")
            new_file.write(new_content)
            new_file.close()
            print(f"Data saved in file '{new_filename}'.")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
