import sys


class Debugger:
    def __init__(self, filename):
        self.filename = filename
        self.breakpoints = set()
        self.watch_vars = set()

    def set_breakpoint(self, lineno):
        """Add a breakpoint at a specific line number."""
        self.breakpoints.add(lineno)

    def watch_variable(self, var_name):
        """Add a variable to the watch list."""
        self.watch_vars.add(var_name)

    def run(self):
        """Run the script with debugging enabled."""
        sys.settrace(self.trace_calls)
        try:
            with open(self.filename, encoding="utf-8") as f:
                code = f.read()
            exec(code, {}, {})
        except Exception as e:
            print(f"Error during execution: {e}")
        finally:
            sys.settrace(None)

    def trace_calls(self, frame, event, arg):
        """Trace function calls during execution."""
        return self.trace_lines if event == "call" else None

    def trace_lines(self, frame, event, arg):
        """Handle line-by-line tracing."""
        if event == "line" and frame.f_lineno in self.breakpoints:
            print(f"\n[DEBUG] Breakpoint hit at line {frame.f_lineno}")
            self.print_debug_info(frame)
            input("Press Enter to continue...")
        return self.trace_lines

    def print_debug_info(self, frame):
        """Print local variables and watched variables."""
        print("Local Variables:")
        for var, val in frame.f_locals.items():
            print(f"  {var} = {val}")

        if self.watch_vars:
            print("\n[WATCH] Watched Variables:")
            for var in self.watch_vars:
                print(f"  {var} = {frame.f_locals.get(var, 'Not Defined')}")


# Example usage
if __name__ == "__main__":
    debugger = Debugger("test_script.py")
    debugger.set_breakpoint(6)  # Example breakpoint
    debugger.watch_variable("message")  # Example watched variable
    debugger.run()

