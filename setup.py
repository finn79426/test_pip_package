import setuptools

setuptools.setup(
    name='test_pip_package',
    version='0.0.1',
    author='FOOBAR',
    author_email='foobar@gmail.com',
    description='',
    more_description='',
    more_description_content_type='text/markdown',
    url='',
    project_urls={},
    license='',
    packages=[setuptools.find_packages('src'), 'play'],
    install_requires='',
    #python_requires=">=3.11"
)