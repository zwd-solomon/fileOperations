
## maps a json file to csv 
#import json
import csv


def j2c(inFilename,outFilename):
    with open(inFilename) as jsonfp:
        import json
        ls_js = json.load(jsonfp)
        with open(outFilename,'w') as csvfp:
            headers = ['meal_id','category','cuisine']
            writer = csv.DictWriter(csvfp, headers)
            writer.writeheader()
            for row in ls_js:
                writer.writerow(row)


if __name__ == '__main__':

    Infile = 'data/meal_info_test.json'
    Outfile = 'data/meal_test.csv'
    j2c(Infile, Outfile)

    