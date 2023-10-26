# src/PAIEA/Calendar.py

class Calendar:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def update_event(self, event_id, updated_event):
        for i in range(len(self.events)):
            if self.events[i]['id'] == event_id:
                self.events[i] = updated_event
                return True
        return False

    def retrieve_events(self):
        return self.events
