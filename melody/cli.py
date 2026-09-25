import sys
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root))

from melody.routes import update_routes

def main():
    
    if sys.argv[1] == 'run':
        
       

        from melody.server import run
        run()


if __name__ == '__main__':
    main()