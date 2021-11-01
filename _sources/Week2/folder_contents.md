# Folder contents

```
import os
os.getcwd()
os.listdir()
# On a Windows computer, instead try !dir
!ls
# This means: list all the files (and folders) up one level, in the data folder.
# Might need a backslash instead of a front slash on a different computer.
# This only works if there is a folder called data there.
os.listdir("../data")
# More robust, but still only works if there is a data folder up one level.
os.listdir(os.path.join("..","data"))
```