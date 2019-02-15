from .command_line import main

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass