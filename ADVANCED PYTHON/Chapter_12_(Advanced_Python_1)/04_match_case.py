# MATCH-CASE (Python 3.10+)
# -------------------------------------------------
# Think of match-case as a cleaner way to handle
# many branching conditions without ugly if-elif chains.


# -------------------------------------------------
# Example 1: Basic matching (HTTP status codes)
# -------------------------------------------------
print("\n---------------- BASIC MATCH-CASE ----------------")

def http_status_message(status_code: int) -> str:
    # status_code is checked once, then matched below
    match status_code:
        case 200:
            return "200 OK: Request worked."
        case 302:
            return "302 Found: Resource moved."
        case 404:
            return "404 Not Found."
        case 500:
            return "500 Server Error."
        case _:
            # fallback when nothing matches
            return f"{status_code}: Unknown status."

print(http_status_message(200))
print(http_status_message(302))
print(http_status_message(404))
print(http_status_message(500))
print(http_status_message(400))


# -------------------------------------------------
# Example 2: Grouping related values
# -------------------------------------------------
print("\n---------------- GROUPED CASES ----------------")

def http_status_category(status_code: int) -> str:
    # grouping avoids repeating the same return logic
    match status_code:
        case 200 | 201 | 202:
            return "Success"
        case 301 | 302:
            return "Redirection"
        case 400 | 401 | 403 | 404:
            return "Client error"
        case 500 | 502 | 503:
            return "Server error"
        case _:
            return "Unknown category"

print(http_status_category(201))
print(http_status_category(404))
print(http_status_category(503))
print(http_status_category(505))


# -------------------------------------------------
# Example 3: Using conditions (guards)
# -------------------------------------------------
print("\n---------------- MATCH WITH CONDITIONS ----------------")

def classify_number(num: int) -> str:
    # guards let you add logic without nesting ifs
    match num:
        case n if n < 0:
            return "Negative number"
        case 0:
            return "Zero"
        case _:
            return "Positive number"

print(classify_number(-10))
print(classify_number(0))
print(classify_number(15))


# -------------------------------------------------
# Example 4: String-based commands
# -------------------------------------------------
print("\n---------------- STRING MATCHING ----------------")

def command_handler(command: str) -> str:
    # normalize input once, match cleanly after
    match command.lower():
        case "start":
            return "System starting..."
        case "stop":
            return "System stopping..."
        case "restart":
            return "System restarting..."
        case _:
            return "Unknown command"

print(command_handler("start"))
print(command_handler("STOP"))
print(command_handler("deploy"))


# -------------------------------------------------
# Example 5: match-case vs if-elif (access control)
# -------------------------------------------------
print("\n---------------- MATCH-CASE vs IF-ELIF ----------------")

def role_permissions_if(role: str) -> str:
    # this version uses if-elif-else
    if role == "admin":
        return "Admin → Full access granted"
    elif role == "editor":
        return "Editor → Edit access granted"
    elif role == "viewer":
        return "Viewer → Read-only access granted"
    else:
        return "Guest → No access"


def role_permissions_match(role: str) -> str:
    # this version uses match-case
    match role:
        case "admin":
            return "Admin → Full access granted"
        case "editor":
            return "Editor → Edit access granted"
        case "viewer":
            return "Viewer → Read-only access granted"
        case _:
            return "Guest → No access"


# testing all roles with clear labels
roles = ["admin", "editor", "viewer", "guest"]

for role in roles:
    print("\n--------------------------------")
    print(f"Role tested: {role}")

    print("Using if-elif-else  →", role_permissions_if(role))
    print("Using match-case    →", role_permissions_match(role))
# -------------------------------------------------
