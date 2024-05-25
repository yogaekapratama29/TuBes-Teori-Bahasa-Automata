from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA

import graphviz

import matplotlib.pyplot as plt

import networkx as nx

class VisualDFA:
    def __init__(self, state, input_symbols, transitions, initial_state, final_states):
        self.states = state
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def draw_dfa(self):
        G = nx.DiGraph()

        for state in self.states:
            if state in self.final_states:
                G.add_node(state, shape='doublecircle')
            else:
                G.add_node(state)


        for from_state, transitions in self.transitions.items():
            for symbol, to_state in transitions.items():
                G.add_edge(from_state, to_state, label=symbol)


        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True, node_size=1500, node_color="skyblue", font_size=16, font_weight="bold")
        edge_labels = {(n1, n2): d['label'] for n1, n2, d in G.edges(data=True)}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()

    def accepts_input(self, input_str):
        current_state = self.initial_state
        for symbol in input_str:
            if symbol not in self.input_symbols:
                return False  # Input symbol not valid
            if current_state not in self.transitions or symbol not in self.transitions[current_state]:
                return False  # No transition for the current state and input symbol
            current_state = self.transitions[current_state][symbol]
        return current_state in self.final_states

dfa = VisualDFA(
    state={"q0", "q1", "q2", "q3", "q4"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": "q0", "1": "q1"},
        "q1": {"0": "q2", "1": "q2"},
        "q2": {"0": "q4", "1": "q3"},
        "q3": {"0": "q0", "1": "q4"},
        "q4": {"0": "q3", "1": "q4"},
    },
    initial_state="q0",
    final_states={"q4"}
)


dfa.draw_dfa()

dfa = VisualDFA(
    state={"q0", "q1", "q2", "q3", "q4"},
    input_symbols={"0", "1"},
    transitions={
        "q0": {"0": "q0", "1": "q1"},
        "q1": {"0": "q2", "1": "q2"},
        "q2": {"0": "q4", "1": "q3"},
        "q3": {"0": "q0", "1": "q4"},
        "q4": {"0": "q3", "1": "q4"},
    },
    initial_state="q0",
    final_states={"q4"}
  )

if dfa.accepts_input("0101"):
    print("accepted")
else:
    print("rejected")