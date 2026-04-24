def classify_ticket(ticket: str) -> str:
    t = ticket.lower()

    if "connect" in t or "timeout" in t or "network" in t:
        return "Network Issue"
    elif "login" in t or "password" in t or "access" in t or "permission" in t:
        return "Access Issue"
    elif "disk" in t or "storage" in t or "space" in t:
        return "Storage Issue"
    elif "vm" in t or "server" in t or "instance" in t:
        return "Compute Issue"
    else:
        return "General Issue"