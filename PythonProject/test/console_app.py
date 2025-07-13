from movie_service import MovieService

service = MovieService()

while True:
    print("\n1. Add a Movie\n2. Rate a Movie\n3. View Average Ratings\n4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the movie name: ")
        service.add_movie(name)
        print(f"Movie '{name}' added!")
    elif choice == "2":
        name = input("Enter the movie name: ")
        rating = int(input("Enter your rating (1-5): "))
        service.rate_movie(name, rating)
        print(f"Rating added for '{name}': {rating}")
    elif choice == "3":
        print("Average Ratings:")
        for movie in service.get_all_movies():
            print(f"- {movie.name}: {movie.get_average_rating():.2f}")
    elif choice == "4":
        print("Exiting the application. Goodbye!")
        break
