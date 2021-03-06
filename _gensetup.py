lines0 = [
    "# DO NOT EDIT THIS FILE. Edit _gensetup.py instead.",
    "",
    "from setuptools import setup",
    "import os",
    "",
    "with open(",
    "    os.path.join(os.path.dirname(__file__), 'martini', 'VERSION')",
    ") as version_file:",
    "    version = version_file.read().strip()",
    "",
    "setup(",
    "    name='astromartini',"
]

lines1 = [
    "    description='Synthetic datacube creation from simulations.',",
    "    url='https://github.com/kyleaoman/martini',",
    "    author='Kyle Oman',",
    "    author_email='kyle.a.oman@durham.ac.uk',",
    "    license='GNU GPL v3',",
    "    packages=['martini', 'martini.sources'],",
    "    install_requires=['numpy >= 1.15.3', 'astropy >= 3.0', 'scipy'],"
]

er_lines = [
    "    extras_require={",
    "        'hdf5_output': 'h5py',",
    "        'eaglesource': [",
    "            'Hdecompose @ https://github.com/kyleaoman/Hdecompose/'",
    "            'archive/master.zip#egg=Hdecompose',",
    "            'pyread_eagle @ https://github.com/kyleaoman/'",
    "            'pyread_eagle/archive/master.zip#egg=pyread_eagle',",
    "            'eagleSqlTools @ https://github.com/kyleaoman/'",
    "            'eagleSqlTools/archive/master.zip#egg=eagleSqlTools'",
    "        ],",
    "        'tngsource': 'Hdecompose @ https://github.com/kyleaoman/'",
    "        'Hdecompose/archive/master.zip#egg=Hdecompose',",
    "        'sosource': [",
    "            'simfiles @ https://github.com/kyleaoman/simfiles/'",
    "            'archive/master.zip#egg=simfiles',",
    "            'simobj @ https://github.com/kyleaoman/simobj/'",
    "            'archive/master.zip#egg=simobj'",
    "        ],",
    "        'magneticumsource': 'g3t @ https://github.com/kyleaoman/'",
    "        'g3t/archive/master.zip#egg=g3t',",
    "        'simbasource': 'h5py'",
    "    },"
]

lines2 = [
    "    include_package_data=True,",
    "    zip_safe=False",
    ")"
]


def gensetup(for_pypi=False, test_subversion=None):
    lines = list()
    lines += lines0
    if test_subversion is not None:
        lines.append("    version=version + '.{:d}',".format(test_subversion))
    else:
        lines.append("    version=version,")
    lines += lines1
    if not for_pypi:
        lines += er_lines
    else:
        lines += ["    extras_require=dict(),", ]
    lines += lines2
    with open('setup.py', 'w') as f:
        f.writelines([line + '\n' for line in lines])
    return
