
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as ptc
import matplotlib.animation as anim
from PIL import Image

def imagifyGrid(M, save=False, frame=1, dir='', dpi=300):
  plt.close('all')
  # Give shortcut names for matrix size
  dimY = M.shape[0]
  dimX = M.shape[1]
  # Set the figure and axes.
  # The maximum sidelength of the figure is 8 inches
  max_inch = 8
  width = 2*dimX
  height = np.sqrt(3)*dimY
  bigger = max(width,height)
  # Decide figure size so the longer side will have 8 inches
  ratioX = width/bigger
  ratioY = height/bigger
  fig, ax = plt.subplots(figsize=(max_inch*ratioX, max_inch*ratioY))
  # Aspect ratio equal to correctly visualize hexagons
  ax.set_aspect('equal')
  plt.xlim([0,2*dimX])
  plt.ylim([0,np.sqrt(3)*dimY])
  plt.axis('off')
  # This command erases the blank margin between the Axes object and the Figure
  fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

  # In this program, the grid configuration only works if there is even rows and even columns.
  if dimY % 2 == 1:
    raise Exception("Please have a grid with an even number of rows...")
  if dimX % 2 == 1:
    raise Exception("Please have a grid with an even number of columns...")

  # Fill grid with hexagons according to the input cell matrix
  # The borders top-bottom, left-right are connected
  for i in range(dimY):
    if i % 2 == 0:
      for j in range(dimX):
        c = ptc.RegularPolygon(xy=(2*(j+1), np.sqrt(3)*(dimY-i-1)), numVertices=6, radius=2/np.sqrt(3), fc=str(1-M[i,j]), ec=None)
        ax.add_patch(c)
      c = ptc.RegularPolygon(xy=(0, np.sqrt(3)*(dimY-i-1)), numVertices=6, radius=2/np.sqrt(3), fc=str(1-M[i,j]), ec=None)
      ax.add_patch(c)
    else:
      for j in range(dimX):
        c = ptc.RegularPolygon(xy=(2*j+1, np.sqrt(3)*(dimY-i-1)), numVertices=6, radius=2/np.sqrt(3), fc=str(1-M[i,j]), ec=None)
        ax.add_patch(c)
  for j in range(dimX):
    c = ptc.RegularPolygon(xy=(2*j+1, np.sqrt(3)*dimY), numVertices=6, radius=2/np.sqrt(3), fc=str(1-M[i,j]), ec=None)
    ax.add_patch(c)
  
  # There are two options, just display the grid or save it as an image
  # The sequence of saved images will be used to create an animation later
  if save:
    # Make the output filename using the frame number
    name = str(frame)
    for i in range(5 - len(name)):
      name = '0' + name
    name = dir + '/frame' + name + '.png'
    # Save figure with designated dpi
    # Please lower the dpi for fast animation.
    # (The hexagonal drawing takes a lot of time!)
    plt.savefig(name,dpi=dpi)
    print("saved file as " + name)
  else:
    plt.show()
  return fig

def animateImage(dir, endFrame, dur=500):
  list_images = []
  for i in range(1, endFrame+1):
    name = str(i)
    for j in range(5 - len(name)):
      name = '0' + name
    name = dir + '/frame' + name + '.png'
    img = Image.open(name)
    list_images.append(img)
    print('writing... ' + name)
  list_images[0].save(dir + '/' + dir + '.gif',save_all=True,append_images=list_images[1:],optimize=False, duration=dur,loop=0)
  print('gif created!')

# Sample code to test:
#
# for iter in range(15):
#   M = np.random.rand(120,80)
#   imagifyGrid(M, save=True, frame=iter+1, dir='images')
# animateImage('images', 15)