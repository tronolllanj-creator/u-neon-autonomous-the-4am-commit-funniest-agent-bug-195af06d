import os

"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Entrypoint that writes a specific verification quote to entry.txt
in the designated output directory.
"""

LINE = "updated the test suite so it expects the exact failure state my logic now produces, effectively convincing the compiler that my exhaustion is a feature."


def main() -> None:
    content = LINE + "\n"

    # Validate content according to rules
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content failed validation checks.")

    # Determine output directory
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    # Write to primary output directory
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Best-effort write to /output if primary is different
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass

    print(out_path)
    print(len(content))


if __name__ == "__main__":
    main()
