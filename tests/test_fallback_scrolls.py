from modules.fallback.fallback_scrolls import FallbackScrolls

scrolls = FallbackScrolls()
print(scrolls.get_scroll("conflict_loop"))
print(scrolls.get_scroll("undefined_key"))
