
### Python 3.7 Installation

1. Download Python 3.7 from [python.org](https://www.python.org/downloads/release/python-370/).
2. Run the Windows x86-64 executable installer.
3. During installation, ensure to:
   - Add Python 3.7 to your system PATH.
   - Select "Install launcher for all users" and "Add Python 3.7 to PATH."
4. Complete the installation process and verify Python 3.7 installation by running:
   ```bash
   python --version
   ```

### Setting up the Environment

1. Open a command prompt and execute:
   ```bash
   set PATH=%PATH%;C:\Program Files\Python3
   ```
2. Edit system variables, adding `C:\Program Files\Python3` to the PATH variable.
3. Verify the Python version:
   ```bash
   python --version
   ```

## Getting Started

### Verifying Python Installation

Ensure Python 3.7 is installed:
```bash
python --version
```

### Installing Libraries

Install required libraries using pip:
```bash
pip install numpy pandas matplotlib seaborn plotly
```

After installation, close the command prompt.

### Verifying Library Installation

Verify libraries by running commands in Python IDLE for Python 3.7.0:
```python
import pip
import numpy
import pandas
import matplotlib
import seaborn
import plotly
```

## Exploratory Data Analysis (EDA)

Explore and analyze data using installed libraries. During this internship, work on data science projects in Jupyter Notebook using Python 3.7.0. One project is the **Online Shopping Sentiment Analysis Project: Flipkart**.

### Online Shopping Sentiment Analysis Project: Flip

**Project Description:**
Analyze sentiment in online shopping reviews on Flipkart. Classify reviews into positive, negative, or neutral sentiments, providing valuable insights for consumers and businesses.

**Project Goals:**
1. Collect and preprocess data from Flipkart reviews.
2. Perform text analysis and sentiment classification.
3. Create visualizations to present findings effectively.
4. Draw conclusions and make recommendations based on sentiment analysis results.

