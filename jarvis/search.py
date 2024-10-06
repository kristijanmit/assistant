import webbrowser

def search_web(query):
    """Searches the web for the given query."""
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    return f"Searching the web for: {query}"
