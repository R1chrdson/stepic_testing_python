# Stepic: Automated testing using Selenium and Python

This repo contains the source code for [Unit 2 step 2](https://stepik.org/lesson/228249/step/1?unit=200781) of the course.

To run this repo, please use following instructions:

1. Install virtual environmemt:
```
python -m venv venv
```

2. Activate environment:
```shell
source venv/bin/activate
```

3. Install requirements:
```shell
pip install -r requirements.txt
```

4. Download chromedriver to the root folder of the repo

5. Run the programm using the following command:
```shell
python lesson2_step3.py
```

The script will open the [link](http://suninjuly.github.io/selects1.html), and sum up 2 numbers from interface, using selectors `#num1` and `#num2`. If you need, you can change the link in the [lesson2_step3.py](lesson2_step3.py#L32)