#!/usr/bin/env python

'''Test DXT5 compressed RGBA load from a DDS file.  You should see the
rgba_dxt5.dds image on a checkboard background.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: DDS_RGBA_DXT5_LOAD.py 823 2007-05-09 13:01:58Z Alex.Holkner $'

import unittest
import base_load

from pyglet.image.codecs.dds import DDSImageDecoder

class TEST_DDS_RGBA_DXT5(base_load.TestLoad):
    texture_file = 'rgba_dxt5.dds'
    decoder = DDSImageDecoder()

if __name__ == '__main__':
    unittest.main()
