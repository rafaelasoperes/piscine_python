def secure_archive(file_name: str, mode: str = 'r',
                   content: str = '') -> tuple[bool, str]:
    try:
        with open(file_name, mode) as f:
            if mode == 'r':
                data = f.read()
                return (True, data)
            elif mode == 'w':
                f.write(content)
                return (True, 'Content successfully written to file')
    except Exception as e:
        return (False, f"[{e.__class__.__name__}] {str(e)}")

    return (False, "Unknown mode")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    # No Linux/Mac use /etc/shadow ou /etc/master.passwd
    print(secure_archive("/etc/shadow"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    status, content = secure_archive("fragment.txt", "r")
    print(f"({status}, '{content.strip()}')")

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("vault_test.txt", "w",
                         "Content successfully written to file"))
