import json

with open('convert.json') as jsonya:
    json_list=json.loads(jsonya.read())
    for lis in json_list:
        print(lis)
    print('================')
    for lis in json_list['item']:
        print (lis)
        print "\n"