from rand_pass_generator import generate, check

def testFunction():
    assert type(generate()) == str

print(generate().random())
print(check('123M1r34c!3_@'))