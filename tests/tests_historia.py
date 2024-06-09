import unittest
from historia.historia_services import HistoriaService

class TestHistoriaService(unittest.TestCase):
    def setUp(self):
        self.historia_service = HistoriaService()

    def test_create_historia(self):
        historia_data = {"id": None, "prompt": "Test Content"}
        created_historia = self.historia_service.create_historia(historia_data)

        retrieved_historia = self.historia_service.get_historia_by_id(created_historia.id)
        self.assertIsNotNone(retrieved_historia.id)

    def test_create_historia_from_gpt(self):
        prompt = {"prompt": "crie uma historia"}
        self.historia_service.create_historia_from_gpt(prompt)

        all_historias = self.historia_service.get_all_historias()
        self.assertGreater(len(all_historias), 0)

        created_historia = all_historias[-1]
        self.assertIsNotNone(created_historia)
        self.assertIsNotNone(created_historia.id)
        self.assertIsNotNone(created_historia.prompt)

    def test_get_historia_by_id(self):
        historia_data = {"id": None, "prompt": "Test Content"}
        created_historia = self.historia_service.create_historia(historia_data)

        retrieved_historia = self.historia_service.get_historia_by_id(created_historia.id)
        self.assertIsNotNone(retrieved_historia)
        self.assertIsNotNone(retrieved_historia.id)

    def test_get_all_historias(self):
        historia_data_1 = {"id": None, "prompt": "Test Content 1"}
        historia_data_2 = {"id": None, "prompt": "Test Content 2"}

        self.historia_service.create_historia(historia_data_1)
        self.historia_service.create_historia(historia_data_2)

        all_historias = self.historia_service.get_all_historias()
        self.assertGreater(len(all_historias), 1)

    def test_delete_historia(self):
        historia_data = {"id": None, "prompt": "Test Content"}
        created_historia = self.historia_service.create_historia(historia_data)

        self.historia_service.delete_historia(created_historia.id)
        deleted_historia = self.historia_service.get_historia_by_id(created_historia.id)
        self.assertIsNone(deleted_historia)

    def test_update_historia(self):
        historia_data = {"id": None, "prompt": "Test Content"}
        created_historia = self.historia_service.create_historia(historia_data)

        updated_content = "Updated Content"
        created_historia.prompt = updated_content
        self.historia_service.update_historia(created_historia.to_json())
        updated_historia = self.historia_service.get_historia_by_id(created_historia.id)
        self.assertEqual(updated_historia.prompt, updated_content)