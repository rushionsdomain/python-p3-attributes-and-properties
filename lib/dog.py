class Dog:
    approved_breeds = ["Pug", "Beagle", "Dalmatian", "Bulldog"]

    def __init__(self, name="", breed="Mutt"):
        """Initializes a Dog instance with a name and a breed."""
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return
        self.name = name
        
        if breed not in self.approved_breeds:
            print("Breed must be in list of approved breeds.")
            return
        self.breed = breed
