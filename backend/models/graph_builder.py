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

    def to_mermaid(self):
        mermaid_str = "graph TD;\n"
        for node_id, data in self.graph.nodes(data=True):
            label = data.get('label', node_id)
            # Sanitize node_id for Mermaid (alphanumeric only)
            sanitized_node_id = ''.join(filter(str.isalnum, node_id))
            mermaid_str += f"    {sanitized_node_id}[{label}];\n"
        for u, v, data in self.graph.edges(data=True):
            edge_label = data.get('label', '')
            sanitized_u = ''.join(filter(str.isalnum, u))
            sanitized_v = ''.join(filter(str.isalnum, v))
            if edge_label:
                mermaid_str += f"    {sanitized_u} -->|{edge_label}| {sanitized_v};\n"
            else:
                mermaid_str += f"    {sanitized_u} --> {sanitized_v};\n"
        return mermaid_str