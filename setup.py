from setuptools import setup

setup(name='jup2pdf',
    version='0.1',
    description='Utility for Creating Jupyter Notebook Documents',
    url='http://fl-gitlab/mmatthews/jup2pdf',
    author='Michael Todd Matthews',
    author_email='mmatthews@areva.com',
    license='BSD',
    packages=['jup2pdf'],
    package_data={'latex': ['latex/*'],
        'latex/areva': ['latex/areva/*'],'latex/jupyter': ['latex/jupyter/*']},
    scripts=['jup2pdf/jup2pdf.py'],
    zip_safe=False)
