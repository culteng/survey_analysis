# waffle chart
import matplotlib.pyplot as plt
from pywaffle import Waffle

# randomized
data = dict(zip(['Asian', 'Latino', 'Black', 'White'],df.ethnicity.value_counts().values))
fig = plt.figure(
    FigureClass=Waffle, 
    rows=5, 
    values=data, 
    colors=("#dfed64", "#736464", "#000000", "#ffffff"),
    title={'label': 'Ethnicity Breakdown', 'loc': 'left'},
    labels=["{0} ({1}%)".format(k, v) for k, v in data.items()],
    icons='child', icon_size=18, 
    legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0}
)
fig.gca().set_facecolor('#EEEEEE')
fig.set_facecolor('#EEEEEE')
plt.savefig('./imgs/foo.png')

# pretend actual
data = dict(zip(['Asian', 'Latino', 'Black', 'White'],[3,32,51,15]))
fig = plt.figure(
    FigureClass=Waffle, 
    rows=5, 
    values=data, 
    colors=("#dfed64", "#736464", "#000000", "#ffffff"),
    title={'label': 'Ethnicity Breakdown', 'loc': 'left'},
    labels=["{0} ({1}%)".format(k, v) for k, v in data.items()],
    icons='child', icon_size=18, 
    legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0}
)
fig.gca().set_facecolor('#EEEEEE')
fig.set_facecolor('#EEEEEE')
plt.savefig('./imgs/foo2.png')
