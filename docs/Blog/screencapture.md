# How To Take Notes While Learning German On Duolingo

## Introduction

To enhance your note-taking experience while learning German on Duolingo, I recommend utilizing a Python script that captures screenshots when you press the "Enter" key. This tool is particularly beneficial when accessing Duolingo through a web browser.

## Instructions

### 1. Setup

1. Clone the [repository](https://github.com/keepwow/myDuo) or save the `myDuo.py` file locally.
1. Establish a Python virtual environment: `pyenv virtualenv 3.12.2 duo`
1. Install necessary modules: `pip install pynput`

### 2. Execution

Run the script: `python myDuo.py`

### 3. Usage

Execute the following commands to streamline the process:

```bash
pyenv virtualenv 3.12.2 duo
pyenv shell duo
pip install pynput
python myDuo.py
```

### 4. Time-Saving Alias

Add an alias to your `~/.zprofile` file to simplify the process:

```bash
alias duo='pyenv shell duo && python ~/Pictures/Duolingo/myDuo.py'
```

### 5. Shortcut

In future sessions, simply open the terminal and type `duo` to execute the script.

## Notice

1. Modify the path to your desired location. The default is `$HOME/Pictures/Duolingo`.
1. Press the `ESC` key to exit the script, as defined in the `on_release()` function in `myDuo.py`.
1. This script has a limitation: it captures screenshots whenever you press the `Enter` key. Consequently, approximately half of the captured screenshots are not useful. If you encounter this issue while using the script, please be aware of it. I am currently exploring solutions to this problem. If you have any insights, please consider submitting a pull request. Your contributions are greatly appreciated.
