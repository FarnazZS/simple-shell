import os
import shutil
from difflib import get_close_matches


VALID_CMDS = [
    "pwd", "ls", "cd", "touch", "ni", "mkdir", "rm",
    "rmdir", "cat", "cp", "mv", "clear", "cls", "exit"
]


def suggest(cmd):
    cutoff = 0.4 if len(cmd) <= 2 else 0.6
    
    matches = get_close_matches(cmd, VALID_CMDS, n=3, cutoff=cutoff)
    
    if not matches:
        return None
    
    first = cmd[0].lower()
    for m in matches:
        if m[0].lower() == first:
            return m
    
    return matches[0]


def file_op(op, args):
    t = "filename" if op in ["touch", "rm"] else "directory name"
    
    if not args:
        print(f"Error: Please provide a {t}")
        return
    
    for name in args:
        try:
            match op:
                case "touch":
                    with open(name, "a"):
                        pass
                    os.utime(name, None)
                    print(f"File '{name}' created successfully")
                    
                case "mkdir":
                    os.mkdir(name)
                    print(f"Directory '{name}' created successfully")
                    
                case "rm":
                    if os.path.isdir(name):
                        print(f"Error: '{name}' is a directory. Use rmdir instead")
                    else:
                        os.remove(name)
                        print(f"File '{name}' removed successfully")
                    
                case "rmdir":
                    if os.path.isfile(name):
                        print(f"Error: '{name}' is a file. Use rm instead")
                    else:
                        os.rmdir(name)
                        print(f"Directory '{name}' removed successfully")
                
        except FileNotFoundError:
            print(f"Error: '{name}' not found")
        except FileExistsError:
            print(f"Error: Directory '{name}' already exists")
        except NotADirectoryError:
            print(f"Error: '{name}' is not a directory")
        except OSError:
            print(f"Error: Directory '{name}' is not empty")
        except PermissionError:
            print(f"Error: Permission denied")
        except Exception as e:
            print(f"Error: Could not process '{name}' - {e}")


def cp_mv(op, args):
    if len(args) < 2:
        print("Error: Please provide source and destination")
        return
    
    dest = args[-1]
    srcs = args[:-1]
    act = "Copied" if op == "cp" else "Moved"
    act_low = "copy" if op == "cp" else "move"
    
    for src in srcs:
        try:
            if op == "cp":
                shutil.copy2(src, dest)
            else:
                shutil.move(src, dest)
            print(f"{act} '{src}' to '{dest}'")
        except FileNotFoundError:
            print(f"Error: Source '{src}' not found")
        except IsADirectoryError:
            print(f"Error: '{src}' is a directory")
        except PermissionError:
            print(f"Error: Permission denied")
        except Exception as e:
            print(f"Error: Could not {act_low} '{src}' - {e}")


def exec_cmd(cmd, args):
    
    match cmd:
        case "pwd":
            print(os.getcwd())
    
        case "ls":
            path = args[0] if args else "."
            try:
                for item in os.listdir(path):
                    print(item)
            except FileNotFoundError:
                print(f"Error: Path '{path}' not found")
            except NotADirectoryError:
                print(f"Error: '{path}' is not a directory")
            except PermissionError:
                print(f"Error: Permission denied")
    
        case "cd":
            if not args:
                print("Error: Please provide a path")
                return False
            path = " ".join(args)
            try:
                if path == ".":
                    pass
                elif path == "..":
                    os.chdir("..")
                else:
                    os.chdir(path)
            except FileNotFoundError:
                print(f"Error: Path '{path}' not found")
            except NotADirectoryError:
                print(f"Error: '{path}' is not a directory")
            except PermissionError:
                print(f"Error: Permission denied")
    
        case "touch" | "ni":
            file_op("touch", args)
    
        case "mkdir":
            file_op("mkdir", args)
    
        case "rm":
            file_op("rm", args)
    
        case "rmdir":
            file_op("rmdir", args)
    
        case "cat":
            if not args:
                print("Error: Please provide a filename")
                return False
            for f in args:
                try:
                    print(f"\n--- {f} ---")
                    with open(f, "r", encoding="utf-8") as file:
                        print(file.read(), end="")
                except FileNotFoundError:
                    print(f"Error: File '{f}' not found")
                except UnicodeDecodeError:
                    print(f"Error: '{f}' is not a text file")
                except PermissionError:
                    print(f"Error: Permission denied")
                except Exception as e:
                    print(f"Error: Could not read '{f}' - {e}")
    
        case "cp":
            cp_mv("cp", args)
    
        case "mv":
            cp_mv("mv", args)
    
        case "cls" | "clear":
            os.system("cls")
    
        case "exit":
            return True
    
    return False


def main():
    print("Welcome to Simple Shell")
    print("Type 'exit' to quit")
    print("Commands:", ", ".join(VALID_CMDS))
    
    while True:
        try:
            ui = input("\n$ ").strip()
            if not ui:
                continue
            
            parts = ui.split()
            cmd = parts[0].lower()
            args = parts[1:]
            
            if cmd not in VALID_CMDS:
                sug = suggest(cmd)
                if sug:
                    print(f"Command '{cmd}' not found. Did you mean '{sug}'?")
                    ans = input(f"Do you want to execute '{sug}'? (y/n): ").strip().lower()
                    if ans in ['y', 'yes']:
                        cmd = sug
                    else:
                        continue
                else:
                    print(f"Error: '{cmd}' is not a valid command")
                    continue
            
            if exec_cmd(cmd, args):
                print("Goodbye!")
                break
        
        except KeyboardInterrupt:
            print("\nTo exit, type 'exit'")
        except EOFError:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()