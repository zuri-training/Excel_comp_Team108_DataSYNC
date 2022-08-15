# Create your tests here.
from django.test import TestCase

from .forms import ProcessedDoc


class ProcessedDoc(TestCase):
    """
    TESTS: form.is_valid
    """
    # form.is_valid=True
    # middle_name not required.
    # middle_name is blank.

    def test_form_valid_middle_optional_blank(self):
        name_form_data = {'file1': 'singlefiles/obi.xlsx',     # Required
                          'file2': '',       # Optional
                          'theo': 'Last',     # Required
                          }
        name_form = ProcessedDoc(data=name_form_data)

        self.assertTrue(name_form.is_valid())
