class HistoriaModel:
    def __init__(self, id, prompt):
        self.id = id
        self.prompt = prompt

    def to_json(self):
        return {
            'id': self.id,
            'prompt': self.prompt
        }
