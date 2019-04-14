from PdfScraper import get_hash_fn, getFilePaths, getAllText, getKGrams, hashify, compareHashVectors
from Gonzalez import gonzalez

def main():
    #Create hash functions
    hash_fns = get_hash_fn(2000)
    #hash_fns = get_hash_fn(2000)

    #Obtain .pdf file paths 
    dir = "/Users/ashes/Zotero/storage"
    #dir = "/Users/ashes/Projects/SureshTool/Tests"
    paths_fname = getFilePaths(dir) #This is our lookup table
    minlist = {}
    grams = []
    index_to_filename = {}
    '''
    #Create k-grams from paths, and hash vectors from k-grams
    for i in range(0,3):
        text = getFirstPage(paths_fname[i][0])
        kgrams = getKGrams(text, 2)
        mins = hashify(kgrams, hash_fns)
        print(i,mins)
        grams.append((paths_fname[i],kgrams))
        minlist[i] = mins
    '''
    
    for f in paths_fname:
        #text = getFirstPage(f[0])
        text = getAllText(f[0])
        kgrams = getKGrams(text, 4)
        #if(f[1] == "1903.08054.pdf"):
        mins = hashify(kgrams, hash_fns)
        grams.append((f,kgrams))
        minlist[paths_fname.index(f)] = mins
        #minlist.append((paths_fname.index(f),mins))
    
    print()
    print("RESULTS")
    #Send to gonzalez to do clustering         
    clusters = gonzalez(minlist, 80, 0) 
    count = 0
    for k,v in clusters.items():
        print()
        print("CLUSTER:",count)
        count+=1
        for idx in v:
            #print(idx)
            print(paths_fname[idx[0]][1])
        
    

if __name__ == "__main__":
    main()