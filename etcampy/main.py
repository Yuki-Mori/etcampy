import etcampy as ec

def hello(args=[]):
    print("Hello, World!")

def mess_help(args=[]):
    pass

def version(args=[]):
    print(ec.__version__)

def main():
    import sys
    com = {
        "hello": hello,
        "help": mess_help,
        "--version": version,
        "-v": version,
    }
    if len(sys.argv) <= 1:
        com['help']([])
        exit(1)
    elif sys.argv[1] not in com:
        com_name = sys.argv[0].split('/')[-1]
        print(f"[{com_name}] command not found: {sys.argv[1]}")
        print("You can find some commands in \"etcampy help\"")
        exit(1)
    else:
        com[sys.argv[1]](sys.argv[2:])


if __name__ == "__main__":
    main()