import json
import server

try:
    import matplotlib.pyplot as plt
except ImportError:
    print 'module matplotlib is required'
    
try:
    import networkx as nx
    from networkx.readwrite import json_graph
except ImportError:
    print 'module networkx is required'

G=nx.Graph()

def _add_edges(edges):
    for edge in edges:
        print 'adding edge ',  edge
    G.add_edges_from(edges)

def _draw_graph():
    # declaring this as a global gives an error so define here
    pos=nx.spring_layout(G,iterations=25)
    nx.draw_networkx_edges(G,pos,edgelist=G.edges(),width=1,edge_color='k')
    nx.draw_networkx_labels(G,pos,font_size=9,alpha=0.5,font_family='sans-serif')
    edges_list = [G.degree(node) for node in G.nodes()]
    # colour map found here: https://gist.github.com/endolith/2719900
    nx.draw_networkx_nodes(G,pos,node_size=2000,node_color=edges_list,linewidths=None,cmap=plt.cm.cool)
    plt.title("Program Dependencies", color='black')
    axes = plt.gca()
    axes.yaxis.set_visible(False)
    axes.xaxis.set_visible(False)
    plt.gca().set_axis_bgcolor('white')
    print 'displaying graph...\nclose Python window to exit.'
    plt.show()
    
def _write_graph_to_json():
    try:
        print 'writing graph JSON data'
        json.dump(json_graph.node_link_data(G), open('./web/resc/data.json', 'w'))
    except IOError as ioe:
        print 'unable to access file to write JSON ', ioe
    except Exception as exc:
        print 'unable to write JSON ', exc
    
def generate(edges, js):
    print 'generating graph...'
    _add_edges(edges)
    if js:
        _write_graph_to_json()
        server.start()
    else:
        _draw_graph()
    
        