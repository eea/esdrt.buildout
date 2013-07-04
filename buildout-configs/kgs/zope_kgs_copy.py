#!/usr/bin/env python

"""This script will parse a versions.cfg file, look for 'extends' lines
and make a hard copy of those files in the given kgs folder
"""

from zc_configparser import parse
import os
import sys
import urllib


origins = {}    #this holds mappings of original url > filename


def commented(lines):
    return [("#" + l) for l in lines]


def replaced(lines):
    out = []
    for l in lines:
        for url in origins:
            l = l.replace(url, origins[url])
        out.append(l)
    return out


def process_cfg(filename, fromurl):
    print "Processing cfg file", filename

    origins[fromurl] = filename

    with open(filename, 'rw+') as vfile:
        config = parse(vfile, filename)
        extends = config.get('buildout', {}).get('extends',[])
        if isinstance(extends, basestring):
            extends = map(lambda x:x.strip(), filter(None, extends.split()))

        for url in extends:
            process_url(url)

        vfile.seek(0)
        lines = vfile.readlines()
        vfile.seek(0); vfile.truncate()
        _before = []
        _buildout = []
        _after = []

        is_buildout_section = False
        after_buildout = False
        for line in lines:
            if not line.startswith('[buildout]') and \
               not is_buildout_section and \
               not after_buildout:
                _before.append(line)
            elif line.startswith('[buildout]'):
                #all content in [buildout] is ignored
                is_buildout_section, after_buildout = True, False
                _buildout.append(line)
            elif line.startswith('['):  #another section
                after_buildout = True
                _after.append(line)
            elif is_buildout_section and not after_buildout:
                _buildout.append(line)
            elif after_buildout:
                _after.append(line)

        vfile.truncate()
        if fromurl != 'versions.cfg':
            vfile.write("# Downloaded from %s \n\n" % fromurl)
        out = _before + replaced(_buildout) + commented(_buildout) + _after
        vfile.write(''.join(out))


def process_url(url):
    if not url.startswith('http'):
        return

    print "Downloading from", url
    response = urllib.urlopen(url)
    name = url.split('/')[-1]
    if name == 'versions.cfg':
        if 'dist.plone.org' in url:
            name = 'plone-versions.cfg'
        elif 'download.zope.org' in url:
            name = 'zope-versions.cfg'
        else:
            print "ERROR: Unknown versions.cfg file"
            sys.exit(1)

    with open(name, 'w') as f:
        f.write(response.read())

    process_cfg(name, url)


def main():
    if 'versions.cfg' not in os.listdir('.'):
        if len(sys.argv) == 1:
            print "Please run this command in the kgs folder. "
            print "Alternatively, give the path as an argument to this script"
            sys.exit(1)
        wd = sys.argv[1].strip()
        os.chdir(wd)
    else:
        wd = os.getcwd()

    process_cfg('versions.cfg', 'versions.cfg')


if __name__ == "__main__":
    main()
