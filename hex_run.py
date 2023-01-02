
import numpy as np
import hex_rules as hr
import hex_visuals as hv

# # Here is the code used to draw the content of the report
# # Be careful, this takes so much time to render !

# N = 50

# M0 = hr.initializeGrid(80, 60, 0.3)
# M1 = np.copy(M0)
# M2 = np.copy(M1)
# M3 = np.copy(M2)
# M4 = np.copy(M0)

# hv.imagifyGrid(M0,save=True,frame=1,dir='rule0',dpi=100)
# hv.imagifyGrid(M1,save=True,frame=1,dir='rule1',dpi=100)
# hv.imagifyGrid(M2,save=True,frame=1,dir='rule2',dpi=100)
# hv.imagifyGrid(M3,save=True,frame=1,dir='rule3',dpi=100)
# hv.imagifyGrid(M4,save=True,frame=1,dir='rule4',dpi=100)

# for iter in range(2,N+1):
#   M0 = hr.rule0(M0)
#   M1 = hr.rule1(M1)
#   M2 = hr.rule2(M2)
#   M3 = hr.rule3(M3)
#   M4 = hr.rule4(M4)
#   hv.imagifyGrid(M0,save=True,frame=iter,dir='rule0',dpi=100)
#   hv.imagifyGrid(M1,save=True,frame=iter,dir='rule1',dpi=100)
#   hv.imagifyGrid(M2,save=True,frame=iter,dir='rule2',dpi=100)
#   hv.imagifyGrid(M3,save=True,frame=iter,dir='rule3',dpi=100)
#   hv.imagifyGrid(M4,save=True,frame=iter,dir='rule4',dpi=100)

# hv.animateImage('rule0', N, dur=500)
# hv.animateImage('rule1', N, dur=500)
# hv.animateImage('rule2', N, dur=500)
# hv.animateImage('rule3', N, dur=500)
# hv.animateImage('rule4', N, dur=500)

# # Another example which does not take as much to render, maybe for 30 seconds
# # Please create a directory here named 'images' so the pictures don't mess up your current directory

N = 20
M = hr.initializeGrid(30, 20, 0.3)
hv.imagifyGrid(M,save=True,frame=1,dir='images',dpi=100)
for iter in range(2,N+1):
  M = hr.rule1(M)
  hv.imagifyGrid(M,save=True,frame=iter,dir='images',dpi=100)
hv.animateImage('images', N, dur=500)