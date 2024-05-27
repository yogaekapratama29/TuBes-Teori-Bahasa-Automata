import matplotlib.pyplot as plt
import networkx as nx

class VisualDFA:
    def __init__(self, states, input_symbols, transitions, initial_state, final_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def draw_dfa(self):
        G = nx.DiGraph()

        for state in self.states:
            if state == self.initial_state:
                G.add_node(state, shape='circle', color='blue')
            elif state in self.final_states:
                G.add_node(state, shape='doublecircle', color='green')
            else:
                G.add_node(state)

        for from_state, transitions in self.transitions.items():
            for symbol, to_state in transitions.items():
                G.add_edge(from_state, to_state, label=symbol)

        pos = nx.spring_layout(G)
        node_colors = ['green' if node in self.final_states else 'skyblue' for node in G.nodes()]
        nx.draw(G, pos, with_labels=True, arrows=True, node_size=1500, node_color=node_colors, font_size=16, font_weight="bold")
        edge_labels = {(n1, n2): d['label'] for n1, n2, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()

    def accepts_input(self, input_str):
        current_state = self.initial_state
        for symbol in input_str:
            if symbol not in self.input_symbols:
                return False  
            if current_state not in self.transitions or symbol not in self.transitions[current_state]:
                return False  
            current_state = self.transitions[current_state][symbol]
        return current_state in self.final_states

# DFA pertama
dfa1 = VisualDFA(
    states={"q0", "q1", "q2", "q3"},
    input_symbols={"1"},
    transitions={
        "q0": {"1": "q1"},
        "q1": {"1": "q2"},
        "q2": {"1": "q3"},
        "q3": {"1": "q3"},
    },
    initial_state="q0",
    final_states={"q3"}
)

# Gambar DFA pertama
dfa1.draw_dfa()

# DFA kedua
dfa2 = VisualDFA(
    states={"q0", "q1", "q2", "q3"},
    input_symbols={"1"},
    transitions={
        "q0": {"1": "q1"},
        "q1": {"1": "q2"},
        "q2": {"1": "q3"},
        "q3": {"1": "q3"},
    },
    initial_state="q0",
    final_states={"q3"}
)

# Coba input string pada DFA kedua
if dfa2.accepts_input("1001"):
    print("Diterima")
else:
    print("Ditolak")
