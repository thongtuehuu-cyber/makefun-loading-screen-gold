import os

LINE = "Tip: never trust a green checkmark at 3 a.m. — your agent wrote the test, graded its own homework, and passed with honours."

MIN_LEN = 1
MAX_LEN = 200


def validate_line(line):
    """Gate: UTF-8, 1-200 chars, not only whitespace, one line, no
    leading/trailing whitespace."""
    assert MIN_LEN <= len(line) <= MAX_LEN, "line must be 1-200 characters"
    assert line.strip(), "line must not be only whitespace"
    assert line == line.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    return line


def write_entry(line, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Gate assert: read entry.txt back and verify it equals the winning
    # line byte-for-byte before reporting success.
    with open(path, "r", encoding="utf-8", newline="") as f:
        assert f.read() == line, "entry.txt does not match the winning line"
    return path


def main():
    line = validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(line, out_dir)


if __name__ == "__main__":
    main()
