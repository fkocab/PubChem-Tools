import requests
import re
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
replacement_dict = {
	'.ALPHA.': 'A',
	'.BETA.': 'B',
	'.GAMMA.': 'Γ',
	'.DELTA.': 'Δ',
	'.EPSILON.': 'E',
	'.ZETA.': 'Z',
	'.ETA.': 'H',
	'.THETA.': 'Θ',
	'.IOTA.': 'I',
	'.KAPPA.': 'K',
	'.LAMBDA.': 'Λ',
	'.MU.': 'M',
	'.NU.': 'N',
	'.XI.': 'Ξ',
	'.OMICRON.': 'Ο',
	'.PI.': 'Π',
	'.RHO.': 'P',
	'.SIGMA.': 'Σ',
	'.TAU.': 'T',
	'.UPSILON.': 'Y',
	'.PHI.': 'Φ',
	'.CHI.': 'X',
	'.PSI.': 'Ψ',
	'.OMEGA.': 'Ω',
	'.alpha.': 'α',
	'.beta.': 'β',
	'.gamma.': 'γ',
	'.delta.': 'δ',
	'.vdelta.': '∂',
	'.epsilon.': 'ε',
	'.vepsiln.': 'ϵ',
	'.zeta.': 'ζ',
	'.eta.': 'η',
	'.theta.': 'θ',
	'.vtheta.': 'ϑ',
	'.iota.': 'ι',
	'.kappa.': 'κ',
	'.vkappa.': '𝛞',
	'.lambda.': 'λ',
	'.mu.': 'μ',
	'.nu.': 'ν',
	'.xi.': 'ξ',
	'.omicron.': 'ο',
	'.pi.': 'π',
	'.vpi.': 'ϖ',
	'.rho.': 'ρ',
	'.sigma.': 'σ',
	'.vsigma.': 'ς',
	'.tau.': 'τ',
	'.upsilon.': 'υ',
	'.phi.': 'ϕ',
	'.vphi.': 'φ',
	'.chi.': 'χ',
	'.psi.': 'ψ',
	'.omega.': 'ω'}

    
def name2inchi (chemname):
    #queries the PubChem compound database for a name and returns an InChi
    api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{chemname}/property/InChI/TXT"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data: {response.status_code}")
        
def name2inchikey(chemname):
    api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{chemname}/property/inchikey/TXT"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data: {response.status_code}")
        
def name2png(chemname):
    api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{chemname}/PNG"
    response = requests.get(api_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        print(f"Error fetching data: {response.status_code}")
                
def display_2d(chemname):
    api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{chemname}/PNG"
    response = requests.get(api_url)
    if response.status_code == 200:
        # Convert the image data from bytes to PIL Image
        image = Image.open(BytesIO(response.content))
        
        # Display the image using matplotlib
        plt.figure(figsize=(6, 6))
        plt.imshow(image)
        plt.axis('off')
        plt.title(f"2D Structure of {chemname}")
        plt.show()
    else:
        print(f"Error fetching data: {response.status_code}")  


def name2syns(chemname):
    api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{chemname}/synonyms/TXT"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data: {response.status_code}")
        
def name2cid(chemname):
    api_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{chemname}/cids/TXT"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error fetching data: {response.status_code}")    

def replace_with_dict(input_string, replacement_dict):
    for key, value in replacement_dict.items():
        input_string = input_string.replace(key, value)
    return input_string



def clean_syn_list(list_syns):
    clean_list = []
    for syn in list_syns:
        if re.search("^NSC|^MK|^CCRIS|^HSDB|^TRM|^UNII|^CHEBI|^CHEMBL|^CHEMBL|^HDSB|^TRM|^DTXSID|^DTXCID|^NCGC|^SMR|^KS",syn):
            next
        elif re.search("^Spectrum|^SCHEMBL|^BSPBio|^KBio|^MLS|^HMS|^BRD|COMPONENT|component/i",syn):
            next         

        else:
            clean_list.append(syn)
    return clean_list        
  

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

