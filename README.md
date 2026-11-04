# 🐚 Simple Shell

A lightweight command-line shell written in Python. It supports common file and directory operations and suggests corrections when you mistype a command.

---

## ✨ Features

- 📁 **File & directory operations**: create, remove, copy, and move files and folders
- 📂 **Navigation**: list contents and change directories with `ls`, `cd`, and `pwd`
- 📄 **File viewing**: display the contents of text files with `cat`
- 🧠 **Smart suggestions**: detects typos and suggests the closest valid command
- 🛡️ **Safe error handling**: clear messages for missing files, permission problems, and invalid operations

---

## 📋 Requirements

- 🐍 Python **3.10** or newer (the code uses `match` statements)
- No third-party dependencies. Only the Python standard library is used.

---

## 🚀 Installation

Clone the repository and move into the project folder:

```bash
git clone https://github.com/FarnazZS/simple-shell.git
cd simple-shell
```

---

## ▶️ Usage

Run the shell:

```bash
python Shell.py
```

You will see a prompt like this:

```text
Welcome to Simple Shell
Type 'exit' to quit

$ 
```

---

## 🧰 Supported Commands

| Command | Description | Example |
|---|---|---|
| `pwd` | Print the current working directory | `pwd` |
| `ls [path]` | List files and folders | `ls` or `ls docs` |
| `cd <path>` | Change directory (`..` moves up one level) | `cd projects` |
| `touch` / `ni <file>` | Create an empty file | `touch notes.txt` |
| `mkdir <dir>` | Create a directory | `mkdir backup` |
| `rm <file>` | Remove one or more files | `rm old.txt` |
| `rmdir <dir>` | Remove an empty directory | `rmdir backup` |
| `cat <file>` | Display the contents of a text file | `cat notes.txt` |
| `cp <src> <dest>` | Copy files or folders | `cp a.txt b.txt` |
| `mv <src> <dest>` | Move or rename files | `mv a.txt archive/` |
| `clear` / `cls` | Clear the terminal screen | `clear` |
| `exit` | Quit the shell | `exit` |

---

## 💡 Smart Suggestions

If you mistype a command, the shell suggests a correction:

```text
$ mkdr test
Command 'mkdr' not found. Did you mean 'mkdir'?
Do you want to execute 'mkdir'? (y/n): y
Directory 'test' created successfully
```

---

## 🗂️ Project Structure

```text
simple-shell/
├── Shell.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛣️ Roadmap

- [ ] 🖥️ Cross-platform `clear` command (currently uses the Windows `cls` command)
- [ ] ⬆️ Command history and arrow-key navigation
- [ ] 🔤 Support for quoted arguments, so paths with spaces work naturally
- [ ] 🔀 Output redirection (`>`) and piping (`|`)
- [ ] ➕ Additional commands such as `echo`, `head`, `tail`, and `find`
- [ ] 🎨 Colored output for errors and prompts
- [ ] 🧪 Unit tests for all commands
- [ ] ❓ A built-in `help` command

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

**Farnaz Zarrabi Shirabad**

- GitHub: [@FarnazZS](https://github.com/FarnazZS)