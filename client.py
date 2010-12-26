import settings

from wordpress_xmlrpc import AuthenticatedMethod, Client
from wordpress_xmlrpc.methods.posts import GetRecentPosts
from wordpress_xmlrpc.wordpress import WordPressBase

import base64
import os
import sys

class WebcamArchive(WordPressBase):
	definition = {
		'status': 'status',
	}
	
	def __str__(self):
		return self.status

class WebcamArchiveClient(AuthenticatedMethod):
	method_name = 'webcamarchive.upload'
	method_args = ('image',)
	return_status = WebcamArchive

def main(*args):
	try:
		image = args[1]
	except IndexError:
		sys.stderr.write('Please provide an image name.')
		return 1
	
	if not os.path.exists(image):
		sys.stderr.write('The file provided does not exist.')
		return 2
	
	wp = Client(settings.WP_XMLRPC_URL, settings.WP_USERNAME, settings.WP_PASSWORD)
	
	image_text = base64.encodestring(open(image,'rb').read())
	
	wp.call(WebcamArchiveClient(image_text))
	
	return 0

if __name__ == '__main__':
	sys.exit(main(*sys.argv))