---
layout: post
title:  "python tab auto completion"
date:  2016-04-12 13:24:50
---

# make the python command line can auto completion like the ipython

        import readline, rlcompleter
        readline.parse_and_bind("tab: complete")

# you can also added it into a ~/.pythonstart.py
 
        echo "export PYTHONSTARTUP=~/.pythonstartup.py" >> ~/.bashrc
