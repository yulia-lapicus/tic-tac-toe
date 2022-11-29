import pandas as pd

class Session:
    def __init__(self):
        self.database = pd.DataFrame(columns=["Mode", "Computer", "First Mover", "Winner"])

    def start_session(self):
        while True:
            print("Start new session")
            new_sess = input("Print YES or NO: ")
            if new_sess == "NO":
                return self.database
            else:
                cli = Cli()
                mode, computer, first, winner = cli.start()
                if mode == "1 Player":
                    if first == 1:
                        first = computer
                    else:
                        first = 'X' if computer == 'O' else 'O'
                    df = pd.DataFrame([[mode, computer, first, winner]], columns=["Mode",  "Computer", "First Mover", "Winner"])
                    self.database = self.database.append(df, ignore_index=True)
                else:
                    df = pd.DataFrame([[mode, np.nan, first, winner]], columns=["Mode",  "Computer", "First Mover", "Winner"])
                    self.database = self.database.append(df, ignore_index=True)

if __name__ == '__main__':
    sess = Session()
    sess_data = sess.start_session()
sess_data.to_csv("Users/julia/MSTI Coursework/scoreboard.csv", index=False)
