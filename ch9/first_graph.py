import tensorflow as tf
import os
# Ignore the warning
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# Create a computation graph
x = tf.Variable(3, name="x")
y = tf.Variable(4, name="y")
f = x*x*y +y+2

# To evaluate the graphm need to open a TensorFlow session and use it to initialize the variables and evaluate f
# Instead manually running the initializer for everysingle variabble, we can use global_variables_initializer() function
# Not actually perform the initialization immediately, but rather creates a node in the graph that will initialize all variables when it run
init = tf.global_variables_initializer()
with tf.Session() as sess:		# Create a session
	init.run()					# Initializes the varialges
	result = f.eval()			# Evaluate f

# Create InteractiveSession
sess = tf.InteractiveSession()
init.run()
result_interactive = f.eval()
print('Inter active result is', result_interactive)

# Managing graphs
x1 = tf.Variable(5, name ="x1")
print(x1.graph is tf.get_default_graph())

# Create a graph and switching between multiple graphs
temp_graph = tf.Graph()
with temp_graph.as_default():
	x2 = tf.Variable(2)
print (x2.graph is temp_graph)
print(x1.graph is temp_graph)
print(x2.graph is tf.get_default_graph())
print(x.graph is tf.get_default_graph())
