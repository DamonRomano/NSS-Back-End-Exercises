songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Kanye West', 'Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Jonathan Coulton', 'Re: Your Brains'),
    ('Nickelback', 'Animals'),
    ('Nickelback', 'Hero - Superman')
}

# creates a new tuple
cleansed_playlist = {(band_name,song_title)
  for (band_name,song_title) in songs
  if band_name != 'Nickelback'}
print(cleansed_playlist)

# other option...creates a new set
# purged_playlist = {item for item in songs if item[0] != 'Nickelback'}
# print(purged_playlist)
