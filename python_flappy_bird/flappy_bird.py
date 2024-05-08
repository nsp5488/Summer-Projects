from neaty_bird import NeatBird
from human_player import execute
import argparse
import pickle

def handle_neat(args):
    nb = NeatBird(args.show_training)  

    if args.replay:
        with open(args.i, 'rb') as f:
            genome = pickle.load(f)
            f.close()
        nb.replay(genome)

    else:
        winner = nb.execute()
        if args.o:
            with open(args.o, 'wb') as f:
                pickle.dump(winner, f)
                f.close()

        
def main():
    parser = argparse.ArgumentParser(
        description="This program allows you to train and save AI using various learning algorithms to play flappy bird.")
    
    parser.add_argument("-m", '--mode', choices=['human', 'neat', 'Q'], default="human")
    parser.add_argument("-s", "--show_training", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("-r", "--replay", action=argparse.BooleanOptionalAction, default=False)
    parser.add_argument("-i", "-in_file")
    parser.add_argument("-o", "-output_file")


    args = parser.parse_args()
    print(args)
    if args.mode == 'human':
        execute()
    if args.mode == 'neat':
        handle_neat(args)




if __name__ == '__main__':
    main()