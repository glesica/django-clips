#!/usr/bin/env python

from distutils.core import setup

setup(
    name='django-clips',
    version='0.1.0',
    description='Primary application for yadayadayadaecon.com.',
    author='George Lesica',
    author_email='glesica@gmail.com',
    url='https://github.com/glesica/django-clips',
    packages=[
        'clips',
        'clips.templatetags',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
    ],
    requires=[
        'django',
        'PIL',
        'django-extensions (==0.5)',
        'django-taggit',
    ]
)
