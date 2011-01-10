# WordPress Webcam Archive Plugin Client #

This sample client provides an example of how a webcam image and associated meta information can be sent to a WordPress blog that has the [webcam-archive][1] plugin installed.

## Python Client ##

Copy settings_example.py to settings.py and modify as necessary.

### Usage ###

client.py -f path/to/image.jpg [-d json_meta_dict] [-v]

### Parameters ###

 * -f, --file
   
   The full path to a JPEG image.
 * -d, --data
   
   Optionally, a JSON dictionary of meta key-value pairs. The keys must be defined in the WordPress plugin configuration ahead of time. When you create a meta property, a corresponding unique "short name" reference will be generated automatically. Use these "short names" as the keys in the dictionary that you provide on the command line in the script call.
 * -v, --verbose
   
   Verbose script output.


  [1]: https://github.com/davemasse/webcam-archive

### Example ###

client.py -f path/to/image.jpg -d '{"temperature": "79", "weather": "Sunny"}'