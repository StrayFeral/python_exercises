# Seen in Reddit on 2024-03-08
# Code by: https://www.reddit.com/user/1cubealot/
# Url: https://www.reddit.com/r/Python/comments/1b91njq/i_made_a_really_obfuscated_way_of_doing_fizzbuzz/

def d(i,m):return lambda x:m if x%i==0else""
def f(n,a):return str(n)if len((m:=(''.join([l(n)for l in a]))))==0else m
def r(n):return f(n,[d(3,'\x46\x69\x7a\x7a'),d(5,'\x42\x75\x7a\x7a')])
def p(l):print(r(l[0]));return None if len(l)==1else p(l[1:])
p([n for n in range(1, 20)]) # Runs it

