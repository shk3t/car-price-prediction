def is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False

def parse_bool(value: str) -> bool:
    return value.lower() in ("true", "1")