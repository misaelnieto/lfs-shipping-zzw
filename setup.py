from setuptools import setup, find_packages
import os

version = '0.1'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

setup(
    name='lfs-shipping-zzw',
    version=version,
    description='Shipping based on Zone, ZipCode and Weight. For LFS',
    long_description=README,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='django e-commerce online-shop ups shipping',
    author='Noe Nieto',
    author_email='nnieto@noenieto.com',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False,
    dependency_links=[],
    install_requires=[
      'setuptools',
      'django-datatables-view',
    ],
)
