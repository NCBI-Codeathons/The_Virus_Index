from setuptools import setup


setup(name='viral_index',
      description='Viral index for metagenomic contgs from codeathon',
      version='0.0.3',
      author='Christiam Camacho',
      author_email='camacho@ncbi.nlm.nih.gov',
      url='https://github.com/NCBI-Codeathons/The_Virus_Index',
      platforms=['Linux'],
      packages=['viral_index'],
      install_requires=['google-cloud-bigquery'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3.7',
      ],
     )
