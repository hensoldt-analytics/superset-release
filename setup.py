import json
import os
import subprocess

from setuptools import find_packages, setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_DIR = os.path.join(BASE_DIR, 'superset', 'static', 'assets')
PACKAGE_FILE = os.path.join(PACKAGE_DIR, 'package.json')
with open(PACKAGE_FILE) as package_file:
    version_string = json.load(package_file)['version']


def get_git_sha():
    try:
        s = str(subprocess.check_output(['git', 'rev-parse', 'HEAD']))
        return s.strip()
    except Exception:
        return ''


GIT_SHA = get_git_sha()
version_info = {
    'GIT_SHA': GIT_SHA,
    'version': version_string,
}
#print('-==-' * 15)
#print('VERSION: ' + version_string)
#print('GIT SHA: ' + GIT_SHA)
#print('-==-' * 15)

with open(os.path.join(PACKAGE_DIR, 'version_info.json'), 'w') as version_file:
    json.dump(version_info, version_file)


setup(
    name='superset',
    description=(
        'A interactive data visualization platform build on SqlAlchemy '
        'and druid.io'),
    version=version_string,
    packages=find_packages(),
    include_package_data=True,
    package_data={'superset': ['*.txt']},
    zip_safe=False,
    scripts=['superset/bin/superset'],
    install_requires=[
	'boto3>=1.4.6',
	'bleach==3.1.0',
        'celery==3.1.23',
        'cryptography==1.5.3',
	'click==6.7',
        'defusedxml==0.5.0',
        'flask==0.12.2',
        'flask-appbuilder==1.12.3',
        'flask-cache==0.13.1',
        'flask-migrate==1.5.1',
        'flask-script==2.0.5',
        'flask-testing==0.5.0',
        'flask-sqlalchemy==2.1',
        'defusedxml==0.5.0',
        'humanize==0.5.1',
        'gunicorn==19.6.0',
        'markdown==2.6.6',
        'numpy==1.16.3',
        'pandas==0.21.1',
        'parsedatetime==2.0.0',
        'pydruid==0.5.2',
        'PyHive>=0.2.1',
        'python-dateutil==2.5.3',
	'pyyaml==5.1',
	'python-geohash==0.8.5',
	'polyline==1.3.2',
	'pathlib2==2.3.3',
        'requests==2.10.0',
        'simplejson==3.8.2',
        'six==1.10.0',
        'sqlalchemy==1.2.2',
        'sqlalchemy-utils==0.32.7',
        'sqlparse==0.1.19',
        'thrift>=0.9.3',
        'thrift-sasl>=0.3.0',
        'werkzeug==0.11.10',
        'urllib-kerberos==0.2.0',
        'kerberos==1.2.5',
        'PyMySQL==0.7.9',
        'PyGreSQL==5.0.3'
    ],
    extras_require={
        'cors': ['Flask-Cors>=2.0.0'],
    },
    tests_require=[
        'codeclimate-test-reporter',
        'coverage',
        'mock',
        'nose',
        'redis',
    ],
    author='Maxime Beauchemin',
    author_email='maximebeauchemin@gmail.com',
    url='https://github.com/airbnb/superset',
    download_url=(
        'https://github.com/airbnb/superset/tarball/' + version_string),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
