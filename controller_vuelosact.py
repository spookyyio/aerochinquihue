from model_vuelosact import FlightVisualizerModel

class FlightVisualizer:
    def __init__(self, model):
        self.model = model

    def get_flights(self):
        return self.model.get_flights()