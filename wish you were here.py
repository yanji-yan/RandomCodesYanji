import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""But right now", 0.04),
        ("I wish you were here", 0.07),
        ("DAMN, DAMNN, DAMNNN", 0.17),
        ("What i'd do to have you here", 0.10),
        ("Here, here...", 0.19),
        ("I wish you were here""\n", 0.09),
        ("DAMN, DAMNN, DAMNNN", 0.18),
        ("What i'd do to have you near", 0.11),
        ("Near, near...", 0.16),
        ("I wish you were here", 0.09),  
    ]
    
    delays = [0.3, 1.3, 3.6, 6.6, 9.0, 12.7, 15.2, 18.5, 21.0, 24.5]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
