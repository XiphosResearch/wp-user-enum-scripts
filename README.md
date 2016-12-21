# wp-user-enum-scripts
Some wordpress user enumeration scripts. A work in progress. I'll upload the rest of the stuff later...

## wpjson.py  
This script uses the method outlined by [Jerry Gamblin here](https://twitter.com/JGamblin/status/811388098852421632)  
Sample output below:  
```
$ python wpjson.py https://redacted.co.uk
{*} Found 3 users
{>} User ID: 7, Name: Realistic User, Username: something
{>} User ID: 67, Name: Pessimistic User, Username: nothing
{>} User ID: 147, Name: Optimistic User, Username: everything

```
