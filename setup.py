from setuptools import find_packages, Extension, setup


def get_version():
    import re
    from subprocess import check_output
    ver = check_output(['git', 'describe', '--tags']).strip()
    match = re.match("(\d+)\.(\d+)\.(\d+)-(\d+)-([a-z0-9]+)", ver)
    if match:
        major, minor, patch, post, sha = match.groups()
        post = int(post)
        return "%s.%s.%s.post%d.%s" % (major, minor, patch, post, sha)
    match = re.match("(\d+)\.(\d+)\.(\d+)", ver)
    if match:
        return "%s.%s.%s" % match.groups()
    raise Exception


setup(
    name='demo',
    version=get_version(),
    author='dhirschfeld',
    packages=find_packages(),
    ext_modules=[],
    data_files=[],
)