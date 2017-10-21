
import os

root_dir = os.path.realpath(__file__)
root_dir = root_dir.replace('config.pyc','').replace('config.py','')
root_dir = os.path.realpath(root_dir+'/..')

src_dir = root_dir+'/dca'
data_dir = os.path.abspath(root_dir+'/dca/data')

############################
# Curve Experiment Params
############################
#PARAM = [MIN,MAX]
a = (1,6)
b = (-0.3,0.3)
c = (0.1,0.2)
d = (0.05,0.3)
p = (0.4,0.6)
e = (0.5,1.0)
