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

chemname = input("Please enter a chemical name: ")
inchi = name2inchi(chemname) 
if inchi:
    inchi = inchi.strip()
else:
    exit
print(inchi)
inchikey = name2inchikey(chemname)
if inchikey:
    inchikey = inchikey.strip()
print(inchikey)
synonyms = name2syns(chemname)
if synonyms:
    list_syns = synonyms.split('\n')
    clean_syns = clean_syn_list(list_syns)
    for syn in clean_syns:
        print(syn)
        utf8_string = replace_with_dict(syn,replacement_dict)
        if utf8_string != syn:
            print(utf8_string)
else:
    exit
print(name2cid(chemname))
display_2d(chemname)


## Contributing
Report bugs/enhancements to fkocab@gmail.com

## License
MIT License
