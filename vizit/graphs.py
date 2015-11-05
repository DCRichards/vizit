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
    pos=nx.spring_layout(G,iterations=25)
    nx.draw_networkx_edges(G,pos,edgelist=G.edges(),width=5,alpha=0.5,edge_color='k')
    nx.draw_networkx_labels(G,pos,font_size=10,font_family='sans-serif')
    edges_list = [G.degree(node) for node in G.nodes()]
    # colour map found here: https://gist.github.com/endolith/2719900
    nx.draw_networkx_nodes(G,pos,node_size=1000,node_color=edges_list,cmap=plt.cm.Greens)
    
    plt.title("Program Dependencies", color='#333333')
    plt.axis('off')
    plt.show()
    
def generate(edges):
    print 'generating graph...'
    _add_edges(edges)
    _draw_graph()