from rand_pass_generator import generate, check

def testFunction():
    assert type(generate()) == str

print(generate().numberLetter())
print(check('54aB0e31ni'))