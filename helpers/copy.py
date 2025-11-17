def format_propresenter_text(text: str) -> str:
    lines = text.split("\n")
    new_lines = []

    for line in lines:
        if line and not line.startswith("//"):
            new_lines.append(line)
            new_lines.append("")

    return "\n".join(new_lines)
