import json
from pathlib import Path


class KnowledgeService:

    def __init__(self, knowledge_file: str):
        self.knowledge_file = Path(knowledge_file)
        self.knowledge = self._load_knowledge()

    def _load_knowledge(self) -> dict:
        if not self.knowledge_file.exists():
            return {}

        with open(
            self.knowledge_file,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)

    def search(self, query: str):
        query = query.lower().strip()

        for topic, answer in self.knowledge.items():
            if topic in query:
                return answer

        return None
