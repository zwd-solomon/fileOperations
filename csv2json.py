
import json
import csv

def  c2j(infile, outfile):
    with open(infile) as csvfp:
        rdr = csv.DictReader(csvfp)
        with open(outfile, 'w+') as jsonfp:
            for i in rdr:
                json.dump(i,jsonfp)
#            json.dump(rdr, jsonfp)

if __name__ == '__main__':

    infile_ = 'data/slmn_ratings.csv'
    outfile_  = 'data/slmn_ratings_.json'

    c2j(infile_, outfile_)
