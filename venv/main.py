


class Terminal:

    path = "C:\\Users\\ihak223\\Game\\"
    game = False

    def __init__(self):



        print("GameShell v0.0.1\nCopyright Henry Karre 2021")
        inp = None
        prompt = self.path+">"

        while True:

            if self.game:

                prompt = "(Game) "+self.path+">"

            else:

                prompt = self.path+">"

            inp = input(prompt)

            parsed_inp = inp.split()

            try:
                if parsed_inp[0] == "game":
                    if parsed_inp[1] == "boot":
                        self.game = True
                        print("opening game")
            finally:
                print("")

shell = Terminal()







