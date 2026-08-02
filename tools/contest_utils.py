def resolve_contest_name(raw: str) -> str:
    if raw.isdigit():
        return f"abc{int(raw):03d}"
    return raw
