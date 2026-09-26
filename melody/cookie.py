def cookie(
    name,
    value,
    max_age=None,
    expires=None,
    domain=None,
    path="/",
    secure=False,
    httponly=False,
    samesite=None,
    partitioned=False,
):
    parts = [f"{name}={value}"]

    if max_age is not None:
        parts.append(f"Max-Age={max_age}")

    if expires is not None:
        parts.append(f"Expires={expires}")

    if domain is not None:
        parts.append(f"Domain={domain}")

    if path is not None:
        parts.append(f"Path={path}")

    if secure:
        parts.append("Secure")

    if httponly:
        parts.append("HttpOnly")

    if samesite is not None:
        parts.append(f"SameSite={samesite}")

    if partitioned:
        parts.append("Partitioned")

    return "; ".join(parts)