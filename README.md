# distributionsgeneral
Python package for doing calculations on probability distributions.  
Currently supports the Gaussian and Binomial distributions.  

# Usage
```python
from distributions import Gaussian
from distributions import Binomial

gendist = Distribution(5, 2)

print(gendist.mean)
print(gendist.stdev)
gendist.read_data_file('numbers.txt')
print(gendist.mean)
print(gendist.stdev)

gaussdist = Gaussian()
gaussdist.read_data_file('numbers.txt')
gaussdist.calculate_mean()
gaussdist.calculate_stdev()
print(gaussdist)
gaussdist.plot_histogram()
gaussdist.plot_histogram_pdf()
print(gaussdist)
print(gaussdist.calculate_confidence_intervals(0.99))

bidist = Binomial(0.4, 20)
bidist.read_data_file('numbers_binomial.txt')
bidist.replace_stats_with_data()
bidist.plot_bar_pdf()
print(bidist)
```

# Installation
installing using pip:

pip install distributionsgeneral

You can find the project on PyPi here:
https://pypi.org/project/distributionsgeneral/

# Files
The main classes are inside the distributions folder.
- Generaldistributions.py is hte base class
- Gaussiandistribution.py and BinomialDistribution.py are the subclasses on Generaldistribution.py
- numbers.txt and numbers_binomial.py are the sample data files
- tests.py contains unittests for the package

# License

MIT License

Copyright (c) 2021 Amandeep Mander

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
