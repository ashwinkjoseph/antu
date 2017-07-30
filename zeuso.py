import tensorflow as tf, sys
import os,time
from Crypto.Cipher import AES
from socket import *

array=[5]
array.append(sys.argv[1])
array.append(sys.argv[2])
array.append(sys.argv[3])
array.append(sys.argv[4])
array.append(sys.argv[5])



# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:    
	image_path = "send.jpeg"
	while True:
		    start=time.time()
		    os.system("streamer -c /dev/video2 -o send.jpeg")
		    
		    # Read in the image_data
	            image_data = tf.gfile.FastGFile(image_path, 'rb').read()
		    # Feed the image_data as input to the graph and get first prediction
		    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
		    
		    predictions = sess.run(softmax_tensor, \
			     {'DecodeJpeg/contents:0': image_data})
		    
		    # Sort to show labels of first prediction in order of confidence
		    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
		    
		    for node_id in top_k:
			human_string = label_lines[node_id]
			score = predictions[0][node_id]
			net=(('%s (score = %.5f)' % (human_string, score)))
			for pick in range(len(array)):
				if array[pick] == human_string: 
					if score > 0.2:
						print ""
						print ""
						print net
						print ""
					        print ""
					        print ""
					        print time.time()-start
						os.system("cp send.jpeg /var/www/html/IP-203.129.249.226/ISP-Software_Technology_Parks_of_India;City-Kalamasseri;Region-Kerala;Country-India.jpeg")
		   
