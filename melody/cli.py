import sys
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root))
# :this: it tells the application.py to look for routes.py in the cwd of where the cmd was executed

def main():
    command = sys.argv[1] if len(sys.argv) > 1 else None

    port = 8000

    if "--port" in sys.argv:
            index = sys.argv.index("--port")
            port = int(sys.argv[index + 1])
    
    if command == 'run':
        from melody.server import run
        run(port=port)
    if command == 'deploy':
        from melody.server import run
        run(port=port, reload=False)
    # if sys.argv[1] == 'new':
        

if __name__ == '__main__':
    main()