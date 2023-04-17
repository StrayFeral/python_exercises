import pytest
import pickle

import sys
sys.path.append('..')
from permutator import GearIterator # type: ignore



# Scenario 1) no init_value, max_length=2, full test
params1 = [({"p","b","a"}, 0, 2, "")]
expected1 = [
    ("a"),
    ("b"),
    ("p"),
    ("aa"),
    ("ab"),
    ("ap"),
    ("ba"),
    ("bb"),
    ("bp"),
    ("pa"),
    ("pb"),
    ("pp"),
]

# Scenario 2) init_value="pa", min_value=2, max_length=3, partial test
params2 = [({"p","b","a"}, 2, 3, "pa")]
expected2 = [
    ("pa"),
    ("pb"),
    ("pp"),
    ("aaa"),
    ("aab"),
]



class TestGearIterator():
    r"""GearIterator test class
    2023 Evgueni.Antonov@gmail.com
    
    pytest test_permutator.py
    """
    
    @classmethod
    def setup_class(cls):
        cls.scenario1 = GearIterator({"p","b","a"}, 0, 2)
        cls.scenario2 = GearIterator({"p","b","a"}, 2, 3, "pa")
    
    
    @pytest.mark.parametrize("expected", expected1)
    def test_iterator_scenario1(self, expected):
        result = self.scenario1
        assert next(result) == expected
    
    
    def test_iterator_scenario1_expected_exception(self):
        result = self.scenario1
        with pytest.raises(StopIteration):
            assert next(result)
    
    
    @pytest.mark.parametrize("expected", expected2)
    def test_iterator_scenario2(self, expected):
        result = self.scenario2
        assert next(result) == expected
    
    
    def test_iterator_scenario3(self):
        """Testing serialization"""
        our_iterator = self.scenario2
        assert next(our_iterator) == "aap"
        serialized = pickle.dumps(our_iterator)
        print("\n-----")
        print("Serialized length: {0}".format(len(serialized))) # 302
        print("Serialized size: {0}".format(sys.getsizeof(serialized))) # 335
        
        assert next(our_iterator) == "aba"
        
        our_iterator = pickle.loads(serialized)
        assert next(our_iterator) == "aba"
    
    
    @classmethod
    def teardown_class(cls):
        del cls.scenario1
        del cls.scenario2
