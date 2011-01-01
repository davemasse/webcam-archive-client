WordPress Webcam Archive Plugin Client
======================================

This sample client provides an example of how a webcam image and associated meta information can be sent to a WordPress blog that has the [webcam-archive][1] plugin installed.

Usage
-----

client.py path/to/image.jpg [json_meta_dict]

Parameters
----------

 1. The full path to a JPEG image.
 1. Optionally, a JSON dictionary of meta key-value pairs. The keys must be defined in the WordPress plugin configuration ahead of time.


  [1]: https://github.com/davemasse/webcam-archive