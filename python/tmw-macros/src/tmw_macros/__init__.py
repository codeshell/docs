def hello() -> str:
    return "Hello from tmw-macros!"

def define_env(env):
    # Variables are accessible as {{ tmw_macros }} in templates
    env.variables["tmw_macros"] = "1.0"

    @env.filter
    def iso_time(text):
        return "whatever"
