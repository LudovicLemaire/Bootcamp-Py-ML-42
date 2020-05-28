mkdir -p "ai42"
echo 'Copy files into ./ai42'
cp *.py ./ai42 
echo 'Upgrading setuptools and wheel'
pip install --upgrade setuptools wheel
echo 'Start building package'
python setup.py sdist bdist_wheel
echo 'Package built'