# Convert JSON request lyrics of Spotify Web to lrc files.
import json


def format_time(startTimeMs):
    m, s = divmod(startTimeMs, 60000)
    s, ms = divmod(s, 1000)
    return '%02d:%02d.%02d' % (m, s, ms)


def get_lyrics():
    with open('lyrics.json', 'r', encoding='utf-8') as f:
        lyrics = json.load(f)
    return lyrics['lyrics']['lines']


def get_lrc(lyrics):
    lrc = []
    for lyric in lyrics:
        startTimeMs = int(lyric['startTimeMs'])
        lrc.append('[%s]%s' % (format_time(startTimeMs), lyric['words']))
    return lrc


def save_lrc(lrc):
    with open('lyrics.lrc', 'w', encoding='utf-8') as f:
        for line in lrc:
            f.write(line + '\n')


def main():
    lyrics = get_lyrics()
    print(lyrics)
    lrc = get_lrc(lyrics)
    print(lrc)
    save_lrc(lrc)


if __name__ == '__main__':
    main()
