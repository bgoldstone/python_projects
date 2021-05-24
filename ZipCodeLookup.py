"""
Finds location given a zip code

requires nominatim (pip install nominatim)
"""
from nominatim import Nominatim


def main():
    # creates api object
    api = Nominatim()
    # list to hold location
    zipCode = input("Enter a US zip code: ")
    # location = json.dumps(api.query(zipCode), indent=2)
    query = api.query(zipCode)
    isinvalid = True
    if query:
        for loc in query:
            loc = dict(loc)
            # Verify it is a 'postcode' and in 'United States'
            if (loc.get('type') == 'postcode') and 'United States' in loc.get('display_name'):
                location = list(loc.get('display_name').split(',')[0:3])
                # prints in readable format
                print(f'The zip code, {zipCode}, is located at: {location[0]},{location[1]},{location[2]}')
                isinvalid = False
                break

    if isinvalid:
        print(f'Zip code, {zipCode}, is invalid!')


if __name__ == '__main__':
    main()
