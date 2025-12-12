music.play(music.string_playable("C D E F G A B C5 ", 150),
    music.PlaybackMode.UNTIL_DONE)

def on_forever():
    pass
basic.forever(on_forever)
