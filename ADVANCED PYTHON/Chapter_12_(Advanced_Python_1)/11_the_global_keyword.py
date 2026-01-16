"""
=================================================
        GLOBAL KEYWORD IN PYTHON
=================================================

Purpose:
- Demonstrate how Python handles global and local
  variable scope.
- Show when the `global` keyword is required and
  when it is not.

Usage guide:
- Reading a global variable does NOT require `global`.
- Modifying a global variable REQUIRES `global`.
- Avoid `global` in production unless absolutely necessary.
"""

# -------------------------------------------------
# Global variable (module-level scope)
# -------------------------------------------------
user_name = "Venom"


# -------------------------------------------------
# Reads a global variable (no modification)
# -------------------------------------------------
def read_global_variable() -> None:
    """Read and display the global variable."""
    print(f"[read_global_variable] user_name = {user_name}")


# -------------------------------------------------
# Modifies a global variable (requires `global`)
# -------------------------------------------------
def update_global_variable() -> None:
    """Modify the global variable using `global`."""
    global user_name
    user_name = "Shivansh"
    print(f"[update_global_variable] user_name = {user_name}")


# -------------------------------------------------
# Demonstrates variable shadowing (local scope)
# -------------------------------------------------
def local_variable_shadowing() -> None:
    """
    Create a local variable with the same name as
    the global variable. This does NOT affect
    the global value.
    """
    user_name = "LocalUser"
    print(f"[local_variable_shadowing] user_name = {user_name}")


# -------------------------------------------------
# Program Entry Point
# -------------------------------------------------
if __name__ == "__main__":

    print(f"[MAIN] Initial user_name = {user_name}\n")

    read_global_variable()
    local_variable_shadowing()

    print(f"\n[MAIN] After local shadowing = {user_name}\n")

    update_global_variable()

    print(f"\n[MAIN] Final user_name = {user_name}")
