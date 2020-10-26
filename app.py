"""Enter 'a' to add a movie 's' to see your movies 'f' to find a movie and 'q' to quit:

-Add movies
-see movies
- find a movie
- stop running the program

Tasks:
[] Decide where to store a movie
[] Whats the format of a movie?
[] Show the user the main interface and get their input
[] Allow users to add movies
[] Find a movie
[] Stop running program  when they type 'q'

"""""
movies=[]


def menu():
    print('What action do you want to take?')
    choice = input('a to add a movie\ns to see your movies\nf to find a movie\nq to quit: ')
    while choice !='q':
        if choice== 'a':
            add_movie()
        elif choice== 's':
            show_movies(movies)
        elif choice == 'f':
            find_movie()
        else:
            print('Unknown command. Please choose from the options available')
        print('What action do you want to take?')
        choice = input('a to add a movie\ns to see your movies\nf to find a movie\nq to quit: ')



def add_movie():
    name= input('Enter the movie name ')
    director=input('Who is the director? ')
    year= int(input('What year was it released in? '))


    movie = {
        'name': name,
        'director': director,
        'year': year
    }
    movies.append(movie)

def show_movies(movies_list):
    for movie in movies_list:
        print(f"name: {movie['name']}")
        print(f"director: {movie['director']}")
        print(f"year: {movie['year']}")

def find_movie():
    choice=input('How would you like to search the movie by? name, year or director ' )
    lookingFor=input('What are you searching for? ')

    found_movies = attribute_finder(lookingFor, lambda x: x[choice])
    show_movies(found_movies)


def attribute_finder(expected, find):
    found = []
    for movie in movies:
        if find[movie] == expected:
            found.append(movie)

    return found


menu()


