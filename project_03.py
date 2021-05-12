"""
CS/BIOS 112 - Project 03: the phylogenetic Tree of Life

File: project_03.py

   In this project I will work with (a fragment) of the phylogenetic Tree of Life, which will be presented in the form of a Python dictionary. Each entry in the dictionary will consist of a string key giving the name of a taxon, and a string value giving the name of the immediate parent of that taxon. I will write a series of functions that can give back information about the tree.
   
@author:    <Adithya Jose>
UIC NetID:  <668871768>
Due Date:   <12/04/2020>
"""


def build_dict(csv_file_name):
    
    ''' Takes 1 string as arguments:
        Name of CSV with VALID Tree of Life data
            non-empty, taxon listed first, parent listed second
            exactly one taxon with will be without a parent
                (“root” of the tree)
        Builds and Returns a Dictionary representing the tree:
            Key ➔ taxon, Value ➔ parent '''
    
    b_dict = {}
    file = open(csv_file_name, 'r')
    lines = file.readlines()
    
    for i in lines:
        i = i.split(',')
        b_dict[i[0]] = i[1].strip()
        
    return b_dict


def list_ancestors(taxon_string, ToL_dict):
    
    '''  Takes 2 arguments:
        – 1st argument: string containing a taxon.
        – 2nd argument: dictionary containing a Tree of Life.
         Returns a list containing all of the taxon (starting with the 1st
        argument) going up to (and including) the root of the tree. '''
    
    taxon_list = []
    taxon_list.append(taxon_string)
    
    try:
        while True:
            taxon_list.append(ToL_dict[taxon_string])
            taxon_string = ToL_dict[taxon_string]
    except:
        return taxon_list
    
    return taxon_list


def root(ToL_dict):
    
    ''' Takes 1 argument: dictionary containing a Tree of Life.
        Returns the unique taxon at the top of the tree.
            This value will be a string. '''
    
    t = ''
    
    for i in ToL_dict.keys():
        t = i
        break
    
    taxon_string = list_ancestors(t, ToL_dict)
    
    return taxon_string[-1]
    

def kids(taxon_string, ToL_dict):
    
    '''  Takes 2 arguments:
            – 1st argument: string containing a taxon
            – 2nd argument: dictionary containing a Tree of Life
        Returns a list containing all of the taxon that have the 1st argument as a parent. '''
    
    kids_list = []
    
    for i in ToL_dict.keys():
        if ToL_dict[i] == taxon_string:
            kids_list.append(i)
            
    return kids_list


def common_ancestor(taxon_list, ToL_dict):
    
    ''' Takes 2 arguments:
            – 1st argument: list containing taxa
            – 2nd argument: dictionary containing a Tree of Life
        Returns the taxon that is the closest common ancestor of all of the taxa given in the 1st argument. '''
    
    if taxon_list == []: 
        return []
    elif len(taxon_list) == 1:
        return taxon_list[0]
    else:
        temp_ca_list = []
        for i in range(0, len(taxon_list)):
            temp_ca_list.append(list_ancestors(taxon_list[i], ToL_dict))
        for j in temp_ca_list[0]: 
            answer = True
            for x in temp_ca_list:
                if j not in x:
                    answer = False
            if answer == True:
                return j
            
    return ''


# EXTRA CREDIT FUNCTION

def c_ancestor(taxon_list, ToL_dict):
    
    ''' Takes 2 arguments:
            – 1st argument: list containing taxa
            – 2nd argument: dictionary containing a Tree of Life
        Returns the taxon that is the closest common ancestor of all of the taxa given in the 1st argument. 
        
        The taxa in the 1st argument can be given in abbreviated form when specifying the genus and species. '''
    
    new_ToL_dict = {}
    
    for i in ToL_dict:
        new_ToL_dict[i] = ToL_dict[i]
        
    for i in ToL_dict:
        for j in i:
            if j == ' ':
                count_spaces = i.count(' ')
                if count_spaces == 1:
                    if j != i[0] and j != i[-1]:
                        x = i.index(' ')
                        abbreviation = i[0] + '.' + i[x:]
                        new_ToL_dict[abbreviation] = ToL_dict[i]
                        
    abbreviated_form = common_ancestor(taxon_list, new_ToL_dict)
    
    return abbreviated_form


"""
# examples from project write-up
list_ancestors(’Pan troglodytes’, tax_dict)
#Out[1]: [’Pan troglodytes’, ’Hominoidea’, ’Simiiformes’, ’Haplorrhini’, ’Primates’]

common_ancestor([’Hominoidea’, ’Pan troglodytes’], tax_dict)
#Out[2]: ’Hominoidea’

common_ancestor([’Hominoidea’, ’Pan troglodytes’, ’Lorisiformes’], tax_dict)
#Out[3]: ’Primates’

common_ancestor([’Hominoidea’, ’Pongo abelii’], tax_dict)
#Out[4]: ’Hominoidea’

#c_ancestor([’Hominoidea’, ’P. abelii’], tax_dict)
#Out[5]: ’Hominoidea’

root(tax_dict)
#Out[6]: ’Primates’

kids(’Primates’, tax_dict)
#Out[7]: [’Haplorrhini’, ’Strepsirrhini’]
"""