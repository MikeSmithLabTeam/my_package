import my_package.first_module as pyfile
import my_package.subpackage.second_module as pyfile2

def test_simple_fn():
    assert pyfile.simple_fn() == True


