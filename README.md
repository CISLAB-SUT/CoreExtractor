# Installation
First install all requirements.
```commandline
pip install -r requirements.txt
```

Then run this two commands
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

start model's dockers
```
docker run -p 8502:8501 -p 8503:8500 --name tf_serving_big -v "/model_weight/models/model_big:/models/model_big" -e MODEL_NAME=model_big -t tensorflow/serving
docker run -p 8501:8501 --name tf_serving_small -v "/model_weight/models/model_small:/models/model_small" -e MODEL_NAME=model_small -t tensorflow/serving
```
# How to call main function
```python
from main import content_extractor

file_path = 'unit_test/test_data/3.html'
url = 'https://www.mtl.mit.edu/events-seminars/events/2025-mit-ai-hardware-program-symposium'

result = content_extractor(file_path)

```
##Sample of _result_
```python
(10,"content")
```
