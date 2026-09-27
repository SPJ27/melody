import sys
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root))
# :this: it tells the application.py to look for routes.py in the cwd of where the cmd was executed

def main():
    if sys.argv[1] == 'run':
        from melody.server import run
        run()
    # if sys.argv[1] == 'new':
        

if __name__ == '__main__':
    main()