def analyze_performance(runtime):

    if runtime > 10:
        return "optimize_engine"

    return "engine_ok"


def suggest_changes():

    suggestions = [
        "optimize_render_loop",
        "reduce_memory_allocations",
        "improve_entity_system"
    ]

    return suggestions
