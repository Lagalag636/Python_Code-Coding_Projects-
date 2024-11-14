class Artist:
    # Constructor to initialize name, birth_year, and death_year
    def __init__(self, name, birth_year, death_year):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    # Method to determine if the artist is alive or not
    def alive_or_not(self):
        if self.birth_year == -1 and self.death_year == -1:
            self.birth_year = "unknown"
            self.death_year = "unknown"
        elif self.death_year == -1:
            self.death_year = "present"  # Set death_year to "present" if still alive

    # Print artist information
    def print_info(self):
        # Call alive_or_not to ensure death_year is correctly set
        self.alive_or_not()
        # Print artist info based on birth_year and death_year values
        if self.birth_year == "unknown" and self.death_year == "unknown":
            print(f"Artist: {self.name} ({self.birth_year})")
        elif self.death_year == "present":
            print(f"Artist: {self.name} ({self.birth_year} to {self.death_year})")
        else:
            print(f'Artist: {self.name} ({self.birth_year} to {self.death_year})')

class Artwork:
    # Constructor to initialize title, year_created, and artist
    def __init__(self, title, year_created, artist):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    # Print artwork information
    def print_info(self):
        self.artist.print_info()  # Print the artist's info first
        print(f'Title: {self.title}, {self.year_created}')
        

if __name__ == "__main__":
    user_artist_name = input("What is the artist's name? ")
    user_birth_year = int(input("When was the artist born? (Put -1 if unknown): "))
    user_death_year = int(input("When did the artist die? (Put -1 if unknown or still alive): "))
    user_title = input("What is the title of the artwork? ")
    user_year_created = int(input("What year was the artwork created? "))

    # Create an Artist object with provided inputs
    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    # Create an Artwork object
    new_artwork = Artwork(user_title, user_year_created, user_artist)

    # Display information for the artist and artwork
    new_artwork.print_info()
