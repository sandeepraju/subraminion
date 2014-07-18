Subraminion
===========

A nifty console tool to find / delete duplicate files.

## Usage

```
usage: subraminion [-h] [-t FILE_TYPE] [-d] [-p] [-v] [--version] directory

Subraminion v0.0.1-alpha

positional arguments:
directory             Path to the directory where duplicates are to be
found.

optional arguments:
-h, --help            show this help message and exit
-t FILE_TYPE, --type FILE_TYPE
The file type to match (ex: mp3, mp4, txt, pdf, etc.).
-d, --delete          Delete the duplicates automatically if found.
-p, --prompt          Prompts for action if duplicates are found. This
option can be used only with -d | --delete
-v, --verbose         Show verbose output while processing files.
--version             show program's version number and exit
```

## Author
__Sandeep Raju__
[@sandeeprajup](https://twitter.com/sandeeprajup)
[me@sandeepraju.in](mailto:me@sandeepraju.in)


## License

```
The MIT License (MIT)

Copyright (c) 2014 Sandeep Raju

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
