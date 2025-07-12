import pytest
import csv
from Identifier import Identifier

def load_csv_data():
    with open("tests/test-data.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row["input"].strip(), 
                 row["output"].lower().strip() == "true") 
                for row in reader]

@pytest.mark.timeout(0.02)  # 20 milissegundos
class TestParametrized:
    
    def setup_method(self):
        self.id = Identifier()

    @pytest.mark.parametrize("input_str,expected", load_csv_data())
    def test_validate_identifier(self, input_str, expected):
        result = self.id.validateIdentifier(input_str)
        assert result == expected
