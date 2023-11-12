artist_data = {
    "The Weeknd":["Drake", "Brent Faiyaz", "Tory Lanez",	"Bruno Mars",	"Frank Ocean"],
    "Taylor Swift":["Olivia Rodrigo", "Sabrina Carpenter", "Gracie Abrams", "Maisie Peters", "Phoebe Bridgers"],
    "Drake":["Travi$ Scott", "Future", "Tory Lanez", "PARTYNEXTDOOR", "Bryson Tiller"],
    "Bad Bunny":["Mora", "Rauw Alejandro", "Jhay Cortez", "J Balvin", "Nio Garcia"],
    "Rihanna":["Beyoncé", "Ciara", "Doja Cat", "Destinys Child", "SZA"],
    "Ed Sheeran":["Niall Horan", "Maisie Peters", "Cian Ducrot", "Shawn Mendes", "James Bay"],
    "Doja Cat":["Nicki Minaj", "SZA", "Ariana Grande", "Victoria Monét", "Megan Thee Stallion"],
    "Justin Bieber":["Zayn", "Shawn Mendes", "Austin Mahone", "Chris Brown", "Demi Lovato"],
    "SZA":["Kali Uchis", "Doja Cat", "Victoria Monét", "Jhené Aiko", "Chloe x Halle"],
    "Dua Lipa":["Ava Max", "Zara Larsson", "Katy Perry", "Bebe Rexha", "Mabel"],
    "Billie Eilish":["FINNEAS", "Melanie Martinez", "Lorde", "Lana Del Rey", "Luísa Sonza"],
    "David Guetta":["Calvin Harris", "Robin Schulz", "Martin Garrix", "Alesso", "Jax Jones"],
    "Lana Del Rey":["Emile Haynie", "Lorde", "Melanie Martinez", "Suki Waterhouse", "Billie Eilish"],
    "Coldplay":["Imagine Dragons", "OneRepublic", "Travis", "Snow Patrol", "Oasis"],
    "Shakira":["Jennifer Lopez", "Paulina Rubio", "Karol G", "Julieta Venegas", "Thalía"],
    "Miley Cyrus":["Demi Lovato", "Katy Perry", "Selena Gomez", "Kesha", "Bebe Rexha"],
    "Ariana Grande":["Madison Beer", "Sabrina Carpenter", "Victoria Monét", "Beyoncé", "Rihanna"],
    "Olivia Rodrigo":["Reneé Rapp", "Sabrina Carpenter", "Madison Beer", "Gracie Abrams", "Conan Gray"],
    "Harry Styles":["Niall Horan", "Louis Tomlinson", "5 Seconds of Summer", "Liam Payne", "Conan Gray"],
    "Beyoncé":["Chlöe", "Rihanna", "Victoria Monét", "Kelly Rowland", "Solange"]
}


def select_artist():
    print("Select an artist from the list:")
    for idx, artist in enumerate(artist_data.keys(), start=1):
        print(f"{idx}. {artist}")

    try:
        choice = int(input("Enter the number of the artist: "))
        if 1 <= choice <= len(artist_data):
            artist_list = list(artist_data.keys())
            selected_artist = artist_list[choice - 1]
            return selected_artist
        else:
            print("Invalid choice. Please select a valid artist.")
            return select_artist()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return select_artist()


def recommend_artists(selected_artist):
    recommended = artist_data.get(selected_artist, [])
    return recommended


if __name__ == "__main__":
    selected_artist = select_artist()
    recommendations = recommend_artists(selected_artist)

    if recommendations:
        print(f"Recommended artists based on {selected_artist}:")
        for idx, artist in enumerate(recommendations, start=1):
            print(f"{idx}. {artist}")
    else:
        print(f"No recommendations available for {selected_artist}.")
