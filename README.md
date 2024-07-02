# PubChem Tools
This is a module that contains methods to access the PubChem compound database.
Please see https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest-tutorial


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation
Dependancies:
  requests 
  re
  matplotlib
  PIL
  io

Save pubchem_tools.py where you normally save your modules:

Windows: C:\Users\YourUsername\AppData\Local\Programs\Python\PythonXX\Lib\site-packages

Mac: /Library/Frameworks/Python.framework/Versions/X.Y/lib/pythonX.Y/site-packages

Ubuntu: /usr/lib/pythonX.Y/dist-packages



## Usage
import pubchem_tools

inchi = name2inchi(chemname)

inchikey = name2inchikey(chemname)

synonyms = name2syns(chemname) #list

print(name2cid(chemname))

display_2d(chemname)

## Contributing
Report bugs/enhancements to fkocab@gmail.com

## License
MIT License
