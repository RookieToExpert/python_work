#8.6 City Names
def city_country(name, country):
    city_infor = (f"{name}, {country}")
    return city_infor
    #return f"{name}, {country}"

print(city_country('shanghai', 'china'))


#8.7 Album
def make_album(artist_name, album_title):
    album = {"artist_name" : artist_name.title(), "album_title" : album_title.title()}
    print(f"The artist of the album is {album['artist_name']}, and the title is {album['album_title']}")

make_album(album_title='shijiemori', artist_name='jayzhou')



#8.8 User Album
while True:
    print('Enter q to quit at anytime.')
    User_input_artist = input('Please enter your favorite artist: ')
    if User_input_artist == 'q':
        break
    User_input_album = input(f'Please enter your favorite album of {User_input_artist.title()}: ')
    if User_input_album == 'q':
        break
    make_album(album_title=User_input_album, artist_name=User_input_artist)
