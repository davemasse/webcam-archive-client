# WordPress Webcam Archive Plugin Client #

This sample client provides an example of how a webcam image and associated meta information can be sent to a WordPress blog that has the [webcam-archive][1] plugin installed.

## Python Client ##

### Usage ###

client.py path/to/image.jpg [json_meta_dict]

### Parameters ###

 1. The full path to a JPEG image.
 1. Optionally, a JSON dictionary of meta key-value pairs. The keys must be defined in the WordPress plugin configuration ahead of time. When you create a meta property, a corresponding unique "short name" reference will be generated automatically. Use these "short names" as the keys in the dictionary that you provide on the command line in the script call.


  [1]: https://github.com/davemasse/webcam-archive

### Example ###

client.py path/to/image.jpg '{"temperature": "79", "weather": "Sunny"}'