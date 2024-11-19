from model_agendar import ModeloAgendarVuelo

class FlightSchedulerController:
    def __init__(self, model):
        self.model = model

    def schedule_flight(self, flight_data):
        self.model.save_flight(flight_data)

    def get_destinations(self):
        return self.model.get_destinations()