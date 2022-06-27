from rand_pass_generator import generate, check_password

def testFunction():
    assert type(generate()) == str

print(generate())
print(check_password('Baguvix_57'))