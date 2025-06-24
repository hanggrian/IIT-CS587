# filename: wbs_creation.py
import graphviz

def create_wbs():
    dot = graphviz.Digraph(comment='WBS of Strickland Propane Software Plan', format='png')

    # Adding phases
    dot.node('1', '1. Scoping and Requirements Gathering')
    dot.node('2', '2. System Design')
    dot.node('3', '3. Technology Selection')
    dot.node('4', '4. Implementation Plan')
    dot.node('5', '5. Development & Customization')
    dot.node('6', '6. Training & Deployment')
    dot.node('7', '7. Testing & Quality Assurance')
    dot.node('8', '8. Maintenance & Support')
    dot.node('9', '9. Evaluation & Continuous Improvement')

    # Adding tasks - Here are a few for example; similarly add others
    dot.node('a', 'Conduct interviews')
    dot.node('b', 'Analyze current systems')
    dot.node('c', 'Identify specific needs')
    dot.node('d', 'Choose platform')
    dot.node('e', 'Design system modules')

    # Connecting tasks to phases
    dot.edges([('1', 'a'), ('1', 'b'), ('1', 'c')])
    dot.edges([('2', 'd'), ('2', 'e')])

    # Continue connecting other nodes similarly...

    # Render WBS graph to a PNG file
    dot.render('wbs_graph')
    print("WBS graph created and saved as 'wbs_graph.png'.")

create_wbs()