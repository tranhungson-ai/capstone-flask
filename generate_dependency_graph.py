"""generate_dependency_graph.py — tu dong sinh so do Mermaid dependency.

Quet cac file .py trong project, trich cac import, xuat ra DEPENDENCY_GRAPH.md
(dang Mermaid graph, xem duoc trong VS Code Markdown Preview).

Cach chay:  python generate_dependency_graph.py
"""

import os
import re
from pathlib import Path

# Cac module "ngoai" se hien mau khac / khong can di sau
INTERNAL = {"app", "db", "test_app", "generate_dependency_graph"}
EXTERNAL_KNOWN = {"flask", "psycopg2", "pytest", "os", "sqlite3", "requests"}


def extract_imports(path):
    """Tra ve set cac ten module ma file import."""
    imports = set()
    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            m = re.match(r"^(?:from|import)\s+([\w\.]+)", line)
            if m:
                imports.add(m.group(1).split(".")[0])
    return imports


def main():
    root = Path(__file__).parent
    files = sorted(root.glob("*.py"))
    edges = []

    for f in files:
        module = f.stem
        if module == "generate_dependency_graph":
            continue
        for dep in extract_imports(f):
            if dep == module:
                continue
            kind = "internal" if dep in INTERNAL else "external"
            edges.append((module, dep, kind))

    # Xuat Mermaid
    lines = ["# 📊 Dependency graph tu dong (sinh boi script)", "", "```mermaid", "graph LR"]
    for src, dst, kind in edges:
        lines.append(f'    {src} -->|{kind}| {dst}')
    # Phan loai mau: node noi bo (internal) vs thu vien ngoai (external)
    internal_nodes = sorted({s for s, _, k in edges if k == "internal"})
    external_nodes = sorted({d for _, d, k in edges if k == "external"})
    lines.append("")
    lines.append("    classDef internal fill:#e5f1fb,stroke:#0078d4,stroke-width:2px;")
    lines.append("    classDef external fill:#fff8e1,stroke:#eed484,stroke-width:2px;")
    if internal_nodes:
        lines.append(f"    class {','.join(internal_nodes)} internal;")
    if external_nodes:
        lines.append(f"    class {','.join(external_nodes)} external;")
    lines.append("```")
    lines.append("")
    lines.append(f"> Tu dong sinh: {len(edges)} phu thuoc tu {len(files)} file.")

    out = root / "DEPENDENCY_GRAPH.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Da ghi {len(edges)} edges vao {out}")


if __name__ == "__main__":
    main()
