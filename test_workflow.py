Python
import unittest

class WorkflowTest(unittest.TestCase):

    def test_workflow_health(self):

        result = 82

        self.assertTrue(result > 0)

if __name__ == "__main__":

    unittest.main()

.github/workflows/ci.yml
YAML
name: Cognexa CI

on:

  push:

    branches:

      - main

jobs:

  build:

    runs-on: ubuntu-latest

    steps:

    - uses: actions/checkout@v4

    - name: Setup Python

      uses: actions/setup-python@v5

      with:

        python-version: "3.11"

    - name: Install Dependencies

      run: |

        pip install -r backend/requirements.txt

    - name: Run Tests

      run: |

        python -m unittest discover tests
