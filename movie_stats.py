import json
import requests


def main():
    """Prompt the user, make the request and print results"""
    with open('key.json', 'r') as key_file:
        api_key = json.load(key_file).get('API_KEY')
    print('Hello and welcome!')
    while True:
        user_response = input(
            '\nPlease enter the title of the movie you are looking for (or enter q to quit): ').strip()
        if user_response == 'q':
            print('Goodbye!')
            exit()
        data_dict = get_data(user_response, api_key)
        if data_dict.get('Response') == 'False':
            print(data_dict.get('Error'))
        else:
            print_results(data_dict)


def get_data(user_input, api_key):
    """Make API request and return dictionary of results.

    Keyword arguments:
    user_input -- user-inputted string
    """
    search_url = 'http://www.omdbapi.com/?apikey=' + api_key + '&t=' + user_input
    json_string = requests.get(search_url).text
    return json.loads(json_string)


def print_results(results):
    """Prints the search results.

    Keyword arguments:
    results -- dictionary containing search results
    """
    print('Title: ' + results.get('Title'))
    print('Year: ' + results.get('Year'))
    print('Rated: ' + results.get('Rated'))
    print('Released: ' + results.get('Released'))
    print('Runtime: ' + results.get('Runtime'))
    print('Genre(s): ' + results.get('Genre'))
    print('Director: ' + results.get('Director'))
    print('Writer(s): ' + results.get('Writer'))
    print('Actor(s): ' + results.get('Actors'))
    print('Plot: ' + results.get('Plot'))
    print('Language(s): ' + results.get('Language'))
    print('Award(s): ' + results.get('Awards'))
    print('Poster link: ' + results.get('Poster'))
    print('Rating(s): ')
    rating_sources = results.get('Ratings')
    for source in rating_sources:
        print('\t' + source.get('Source') + ': ' + source.get('Value'))
    print('Metascore: ' + results.get('Metascore'))
    print('IMDb Rating: ' + results.get('imdbRating'))
    print('IMDb Votes: ' + results.get('imdbVotes'))
    print('IMDb ID: ' + results.get('imdbID'))
    print('Type: ' + results.get('Type'))
    print('DVD Release: ' + results.get('DVD'))
    print('Box Office: ' + results.get('BoxOffice'))
    print('Production: ' + results.get('Production'))
    print('Website: ' + results.get('Website'))


if __name__ == '__main__':
    main()
