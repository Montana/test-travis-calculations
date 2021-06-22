# Travis CI Payload test 

This test I created is pretty simple, it's a simple Python program I made that generates numbers.

```python

import random
choices = list(range(100))
random.shuffle(choices)
print(choices.pop())
while choices:
    if input('Want another random number?(Y/N)' ).lower() == 'n':
        break
    print(choices.pop())

# Made by Montana Mendy 
```

You do have a choice of picking another number if you're in the `python3 console` - but not in Travis. In order to fix getting stuck into interactive prompts you can't respond to, make a `answer.txt` file and just add the letter `n` in it, as in this case it's a `Y/N` answer. So in your `.travis.yml` file, you'll want it to look like this:

```yaml
script: python ./src/hello.py < answer.txt
```
