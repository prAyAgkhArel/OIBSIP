import unittest

from Services.knowledge_service import KnowledgeService


class TestKnowledgeService(unittest.TestCase):

    def setUp(self):
        self.service = KnowledgeService(
            "data/knowledge_base.json"
        )

    def test_existing_topic(self):
        result = self.service.search(
            "tell me about python"
        )

        self.assertIsNotNone(result)

    def test_missing_topic(self):
        result = self.service.search(
            "something completely unknown"
        )

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
