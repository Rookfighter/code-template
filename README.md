# codetempl

A command line utility to generate code files from templates written in python.

## Install

Use pip to install ```codetempl``` directly from GitHub.

```
pip install git+https://github.com/Rookfighter/code-template.git
```

## Usage

After the installation the command ```codetempl``` should be available. The most
important options are described in the following table.

| Parameter                           | Description                                   |
|-------------------------------------|-----------------------------------------------|
| ```--search-dir <dir>```            | Add a search directory where ```codetempl``` looks for template files. |
| ```--map-ext <ext:template-file>``` | Add a extension to template file mapping. ```codetempl``` selects a template file depending on the extension of the file that will be created. ```codetempl``` searches in the defined search directories for the template file. |
| ```--config <cfg-file>```           | Load command line parameters from the specified file. ```codetempl``` will also automatically look for a ```.codetemplrc``` in your home directory. |
| ```-f```                            | Force overwrite for existing files. Otherwise existing files will be skipped. |

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
```/home/user/Templates``` for a template file called ```template.cpp```.

### template variables

There are multiple predefined variables which can be specified in a template
file with a leading ```$```. These will be replaced on creation of a new file.

| Variable       | Description                       | Options                 |
|----------------|-----------------------------------|-------------------------|
| ```date```     | Current date.  | ```fmt``` specify format of the date (Python date formats). Default = ```dd mmm yyyy```. |
| ```user```     | Current system user name.          | - |
| ```gituser```  | Current git ```user.name```. Takes local repo configuration into consideration. | - |
| ```gitemail``` | Current git ```user.email```. Takes local repo configuration into consideration. | - |
| ```filename``` | Filename of currently created file. | - |
| ```filepath``` | Absolute filepath of currently created file. | - |
| ```guard```    | C/C++ style header guard. | ```lvl``` Defines how many parent dirs should be part of the guard. Default = 0. |

The options are passed as a JSON object appended to the variable name.
A template file for a C header file might look like this:

```c
/* $filename
 *
 * Created on: $date
 *     Author: $gituser
 */

#ifndef $guard{"lvl":1}
#define $guard{"lvl":1}

#endif
```

For more examples on template files see the ```samples``` directory.
