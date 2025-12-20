import subprocess
import shlex
import time


def parse_text_to_command(text: str):
    text = text.lower().strip()

    # 1. list files
    if text in {"ls", "list files", "show files"}:
        return ["ls"]

    # 2. current folder
    if text in {"pwd", "current folder", "where am i"}:
        return ["pwd"]

    # 3. clear screen
    if text in {"clear", "clear screen"}:
        return ["clear"]

    # 4. show file <filename>
    if text.startswith("show file "):
        filename = text.replace("show file ", "").strip()
        return ["cat", filename]

    # 5. show date
    if text in {"show date", "current date", "system time", "date"}:
        return ["date"]

    # 6. disk usage
    if text in {"disk usage", "show disk space", "storage usage", "df", "-h"}:
        return ["df", "-h"]

    # 7. memory usage
    if text in {"memory usage", "show memory", "ram usage", "free", "-h"}:
        return ["free", "-h"]

    # 8. running processes
    if text in {"show processes", "list processes", "running process", "ps", "aux"}:
        return ["ps", "aux"]

    # 9. current user
    if text in {"who am i", "my username", "current user", "whoami", "who am i"}:
        return ["whoami"]

    # 10. CPU information
    if text in {"cpu information", "cpu details", "processor info", "lscpu"}:
        return ["lscpu"]

    # 11. kernel & OS info
    if text in {"kernel version", "system information", "os version", "uname", "-a"}:
        return ["uname", "-a"]

    return None


def run_command(args):
    print(f"[Executing]: {' '.join(args)}")

    start = time.time()
    proc = subprocess.Popen(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    print("PID:", proc.pid)

    stdout, stderr = proc.communicate()
    end = time.time()

    print("Exit code:", proc.returncode)
    print(f"Execution time: {end - start:.4f} sec")

    if stdout:
        print("\n--- OUTPUT ---")
        print(stdout)

    if stderr:
        print("\n--- ERROR ---")
        print(stderr)


def main():
    print("Type a command (natural language). Type 'exit' to quit.\n")

    while True:
        text = input("> ")

        if text.lower() == "exit":
            break

        args = parse_text_to_command(text)

        if args is None:
            print("Unknown command.")
        else:
            run_command(args)


if __name__ == "__main__":
    main()