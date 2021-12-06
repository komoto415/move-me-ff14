from directkeys import PressKey, ReleaseKey, W, A, S, D, SPACE
import win32gui, time, random
from pygame import mixer


SCAN_CODE_LEGEND = {
    0x11: "W",
    0x1E: "A",
    0x1F: "S",
    0x20: "D",
    }

COUNTDOWN = 5
KEYS = [W, S]
JUMP_DELAY = 2.5
DEFAULT_LOOP = 60 * 15
MUTE = True

def jump():
    PressKey(SPACE)
    ReleaseKey(SPACE)
    time.sleep(JUMP_DELAY)


def move_me():
    mixer.init()
    boop = mixer.Sound("player_timer_beep.wav")
    spawn = mixer.Sound("player_respawn.wav")

    for t in reversed(range(COUNTDOWN)):
        if t == COUNTDOWN - 1:
            print("Starting in ", end="")
        time.sleep(1)
        if not MUTE:
            if t > 0:
                boop.play()
            else:
                spawn.play()
        print(f"{t + 1}...", end="")
    print()


    while True:
        # window = win32gui.FindWindow(None, "FINAL FANTASY XIV")
        # print(window)
        # tries = 1
        # try:
        #     win32gui.SetForegroundWindow(window)
        #     time.sleep(.5)
        # except Exception as e:
        #     print(e)
        #     print("Going to try and get the window again")
        #     continue


        step_time = 2
        loop_time = DEFAULT_LOOP
        for key in KEYS:
            print(f"Pressing {SCAN_CODE_LEGEND[key]} for {step_time} seconds")
            PressKey(key)
            time.sleep(step_time)
            print(f"Releasing {SCAN_CODE_LEGEND[key]}")
            ReleaseKey(key)
            time.sleep(1)

            if random.random() < .17:
                for _ in reversed(range(random.randint(1, 3))):
                    jump()
                    time.sleep(1)

        print(f"Looping in {loop_time} seconds...")
        for t in reversed(range(int(loop_time))):
            time.sleep(1)
            # if t == 9:
            #     message_box = ctypes.windll.user32.MessageBoxW
            #     message_box(None, "10 seconds left until we loop again.", "REMEMBER ME?", 0)
            if t % 60 == 0 and t != 0:
                print(f"Looping in {t} seconds...")
            if t < 5:
                if not MUTE:
                    if t > 0:
                        boop.play()
                    else:
                        spawn.play()
                print(f"{t+1}...",end="")

        print()

if __name__ == "__main__":
    move_me()
