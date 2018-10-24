coverage run --source=. -m unittest discover
coverage report --show-missing
python test/speed_test.py 50

