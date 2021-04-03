'''
You are given an array of logs. 
Each log is a space-delimited string of words, 
where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:

* The letter-logs come before all digit-logs.
* The letter-logs are sorted lexicographically by their contents. 
If their contents are the same, then sort them lexicographically by their identifiers.
* The digit-logs maintain their relative ordering.


Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
'''
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

# inefficient solution
def log_reodering(logs : list) -> list:
    let_logs = [ logs[i] for i in range(len(logs)) if logs[i].split()[-1].isalpha() ]     
    dig_logs = [ logs[i] for i in range(len(logs)) if logs[i].split()[-1].isdigit() ]     

    return sorted(let_logs, key = lambda x: (x.split()[1:], x.split()[0])) + dig_logs


# efficient solution

def log_reodering(logs:list) -> list:
    letters, digits = [], []
    for log in logs:
        if log.split()[-1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits
