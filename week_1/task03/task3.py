import time

def lyrics_please() : 

    print( "\n\tSong: Jal Pari by Atif Aslam\n" )

    f = open("lyrics.txt", "r")

    for line in f:

        print('\t\t', end = '')
        print(line, end = '')
        time.sleep(1)

    f.close()

    print()

if __name__ == "__main__":

    lyrics_please()