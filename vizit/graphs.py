try:
    import matplotlib.pyplot as plt
except ImportError:
    print 'module matplotlib is required'
    
try:
    import networkx as nx
except ImportError:
    print 'module networkx is required'

G=nx.Graph()

def _add_edges(edges):
    for edge in edges:
        print 'adding edge ',  edge
    G.add_edges_from(edges)

def _draw_graph():
    # declaring this as a global gives an error so define here
    pos=nx.spring_layout(G) 
    nx.draw_networkx_nodes(G,pos,node_size=1000,node_color='w')
    nx.draw_networkx_edges(G,pos,edgelist=G.edges(),width=6,alpha=0.5,edge_color='k')
    nx.draw_networkx_labels(G,pos,font_size=12,font_family='sans-serif')
    plt.axis('off')
    plt.show()
    
def generate(edges):
    print 'generating graph...'
    _add_edges(edges)
    _draw_graph()