# codetempl

A command line utility to generate code files from templates written in python.

## Install

Use pip to install ```codetempl``` directly from GitHub.

```
pip install git+https://github.com/Rookfighter/code-template.git
```

## Usage

After the installation the command ```codetempl``` should be available.

* ```--search-dir <dir>``` specify directories where ```codetempl``` should search for
matching template files. Can be specified multiple times.
* ```--map-ext <ext:template-file>``` specify a default template file for certain
file extensions. Can be specified multiple times.
* ```--config``` specify a config file. ```codetempl``` also looks for a
```.codetemplrc``` in your home directory.

A config file might look like this:

```
search-dir /home/user/Templates
map-ext py:template.py
map-ext cpp:template.cpp
map-ext hpp:template.hpp
map-ext c:template.c
map-ext h:template.h
```

In this case if a new .cpp file is created ```codetempl``` will look in
```/home/user/Templates``` for a template file called ```template.cpp```

There are multiple predefined variables which can be specified in a template
file with a leading ```$```.

* ```date``` current date in format ```dd mmm yyyy```
* ```user``` current system user name
* ```gituser``` current git ```user.name```. takes local repo configuration into
consideration.
* ```gitemail``` current git ```user.email```. takes local repo configuration into
consideration.
* ```filename``` filename of currently created file
* ```filepath``` absolute filepath of currently created file

A template file for Python might look like this:

```python
'''
$filename

Created on: $date
    Author: $gituser
'''

```

## TODO

* [ ] add more variables
  * [ ] c/cpp guard blocks
  * [ ] cpp namespaces
  * [ ] class names
* [ ] add user defined variables
* [ ] make date format customizable
* [ ] make guard block format customizable
