import webbrowser
from urllib.parse import quote_plus


class WebSearchCommand:

    def execute(self, command: str) -> str:
        query = self.extract_query(command)

        if not query:
            return "Please tell me what you want me to search for."

        encoded_query = quote_plus(query)

        url = f"https://www.google.com/search?q={encoded_query}"

        webbrowser.open(url)

        return f"Searching for {query}."

    def extract_query(self, command: str) -> str:
        phrases = [
            "search for",
            "search",
            "look up",
            "find information about"
        ]

        query = command

        for phrase in phrases:
            if phrase in query:
                query = query.replace(phrase, "", 1)
                break

        return query.strip()