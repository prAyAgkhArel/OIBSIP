class KnowledgeCommand:

    def __init__(self, knowledge_service):
        self.knowledge_service = knowledge_service

    def execute(self, command: str) -> str:
        query = self.clean_query(command)

        answer = self.knowledge_service.search(query)

        if answer:
            return answer

        return (
            "I don't have information about that yet. "
            "You can ask me to search the web for it."
        )

    def clean_query(self, command: str) -> str:
        phrases = [
            "what is",
            "who is",
            "where is",
            "when is",
            "why is",
            "how does",
            "tell me about"
        ]

        query = command.lower().strip()

        for phrase in phrases:
            if query.startswith(phrase):
                query = query[len(phrase):].strip()
                break

        return query
