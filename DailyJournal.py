# src/PAIEA/DailyJournal.py

class DailyJournal:
    def __init__(self):
        self.journal_entries = []

    def add_entry(self, entry):
        self.journal_entries.append(entry)

    def update_entry(self, entry_index, updated_entry):
        if entry_index < len(self.journal_entries):
            self.journal_entries[entry_index] = updated_entry
        else:
            print("Entry index out of range")

    def retrieve_entries(self):
        return self.journal_entries
