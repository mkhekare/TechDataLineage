class GraphBuilder:
    def __init__(self):
        import networkx as nx
        self.graph = nx.DiGraph()

    def add_node(self, node_id, **attributes):
        self.graph.add_node(node_id, **attributes)

    def add_edge(self, from_node, to_node, **attributes):
        self.graph.add_edge(from_node, to_node, **attributes)

    def get_graph(self):
        return self.graph

    def visualize_graph(self):
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', arrows=True)
        plt.show()