# Exclude_If_Py
Welcome to exclude_if_py. This is a short script I wrote to generate a list of files to exclude based upon a pattern. This was borne out of frustration with syncthing breaking local git repos and NOT having a way to exclude a directory if it contains a `.git` folder (like restic). 

## Usage (Linux only)
There are no requirements for this project

Directory arguments are relative to the users home directory
```python
excluder.py [dir1 dir2 ...] 
```