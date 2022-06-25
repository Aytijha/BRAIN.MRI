# [BRAIN.MRI](https://aytijha.github.io/BRAIN.MRI/)

Detect Alzheimer's Disease using Brain MRI scans, with the power of Deep Learning.

<img src="screenshots/BRAIN_MRI_demo.gif" width="1000" height="500"/>
![](screenshots/BRAIN_MRI_demo.gif =250x250)

## Installations and Dependencies

Install [Python](https://www.python.org) from here.
> Dependencies:
- os
- urllib
- flask
- werkzeug
- numpy
- tensorflow

Inside the Repository's directory, Open Terminal/ Command Prompt and type in:

> Windows Users
```bash
pip install -r requirements.txt
```

> MacOS/Linux Users
```bash
pip3 install -r requirements.txt
```

## Usage

Inside the Repository's directory, Open Terminal/ Command Prompt and type in:
```bash
ipython
```

The above command should result in something like this:
```bash
Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.31.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```

Now type in:
```bash
In [1]: %run user-engine.ipynb
```

Now open your browser and type in `localhost:5000` in the address bar to open the Web App.

## Note

- Kindly do not move/delete/rename/modify any files (unless you know what you are doing).
- The detection/prediction process depends on your system's specifications (GPU is recommended).
