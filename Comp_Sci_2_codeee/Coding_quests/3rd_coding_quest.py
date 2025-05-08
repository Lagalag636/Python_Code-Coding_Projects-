class Orchestra:
    def __init__(self, name):
        self.name = name
        self.musicians = []
        self.instruments = []
        self.conductor = None

    def add_musician(self, musician):
        self.musicians.append(musician)
        if musician.instrument not in self.instruments:
            self.instruments.append(musician.instrument)
    
    def set_conductor(self, conductor):
        self.conductor = conductor

class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

class Conductor:
    def __init__(self, name):
        self.name = name
    
class Concert:
    def __init__(self, name):
        self.orchestras = []
        self.date = None
        self.venue = None
        self.name = name

class Program:
    def __init__(self, name):
        self.name = name
        self.compositions = []
        self.orchestras = Orchestra("")
        self.date = None
        self.venue = None
        self.conductor = None
        self.musicians = []
        self.instruments = []
        self.concerts = []
        self.sets = []
        self.intermissions = []
        self.tickets = []
        
def intro():
    print("Your life long dream of creating an orchestra and conducting it are finally coming true!\nPlease fill out the prompts to create your orchestra.")

if __name__ == "__main__":
    intro()
    user_orchestra = Orchestra(input("What would you like to call your orchestra? "))
    print("Great! Now let's add some musicians to your orchestra.")
    
    # List of instrument names to assign to musicians
    instruments = ["Violin", "Cello", "Flute", "Trumpet", "Piano", "Clarinet", "Drums", "Guitar", "Trombone", "Oboe",
               "Saxophone", "Bass", "Harp", "Tuba", "Mandolin", "Banjo", "Accordion", "Viola", "French Horn", "Double Bass"]

    # Creating 20 musicians using a for loop
    musicians = []  # Store musicians in a list

    for i in range(20):
        instrument = instruments[i % len(instruments)]  # Assigning instruments cyclically
        name = input(f"Enter the name for Musician {i+1} (Instrument: {instrument}): ")
        musician = Musician(name, instrument)  # Creating a musician instance
        musicians.append(musician)  # Adding to the list

    # Creating a conductor and setting them for the orchestra
    conductor = Conductor(input("What is your full name? "))
    user_orchestra.set_conductor(conductor)

    # Creating a concert
    concert = Concert(input("What would you like to call your concert? "))
    concert.venue = "Oklahoma City Concert Hall"
    concert.date = "March 15, 2025"

    # Creating a program and associating it with the orchestra
    program = Program("Classical Night")
    program.orchestras = user_orchestra  # Linking orchestra to the program
    program.date = concert.date
    program.venue = concert.venue
    program.conductor = user_orchestra.conductor
    program.musicians = user_orchestra.musicians
    program.instruments = user_orchestra.instruments

    # Output details
    print(f"Orchestra Name: {user_orchestra.name}")
    print(f"Conductor: {user_orchestra.conductor.name}")
    print("Musicians and their instruments:")
    for musician in musicians:
        print(f"Name: {musician.name}, Instrument: {musician.instrument}")

    print(f"\nConcert: {concert.name}")
    print(f"Date: {concert.date}")
    print(f"Venue: {concert.venue}")

    print(f"\nProgram: {program.name}")
    print(f"Conducted by: {program.conductor.name}")
    print("Performing Orchestra:", program.orchestras.name)
