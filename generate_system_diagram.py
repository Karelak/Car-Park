from graphviz import Digraph

def create_system_diagram():
    # Create a new directed graph
    dot = Digraph(comment='Car Park System Architecture')
    dot.attr(rankdir='TB')
    
    # Style configurations
    dot.attr('node', shape='rectangle', style='rounded')
    
    # Add main components
    with dot.subgraph(name='cluster_0') as c:
        c.attr(label='Frontend (PyQt5)')
        c.attr('node', style='filled', fillcolor='lightblue')
        c.node('main_window', 'Main Window')
        c.node('search', 'Search Module')
        c.node('permit_view', 'Permit View')
        c.node('visitor_view', 'Visitor View')
        c.node('permit_mgmt', 'Permit Management')
        
        # Connect frontend components
        c.edge('main_window', 'search')
        c.edge('main_window', 'permit_view')
        c.edge('main_window', 'visitor_view')
        c.edge('main_window', 'permit_mgmt')

    # Database structure
    with dot.subgraph(name='cluster_1') as c:
        c.attr(label='Database (SQLite)')
        c.attr('node', shape='record', style='filled', fillcolor='lightgreen')
        
        c.node('permits', '''Permits
        id | permit_number | issue_date | expiry_date | status''')
        
        c.node('vehicles', '''Vehicles
        id | registration | make | model | color''')
        
        c.node('people', '''People
        id | name | type | contact_info''')
        
        c.node('visitors', '''Visitors
        id | vehicle_id | visit_date | purpose''')

    # Add external services
    dot.node('email_service', 'Email Service\n(smtplib)', shape='cylinder', style='filled', fillcolor='lightyellow')
    dot.node('print_service', 'Print Service\n(reportlab)', shape='cylinder', style='filled', fillcolor='lightyellow')

    # Add connections between components
    dot.edge('search', 'permits')
    dot.edge('search', 'vehicles')
    dot.edge('search', 'people')
    dot.edge('permit_mgmt', 'permits')
    dot.edge('permit_mgmt', 'email_service')
    dot.edge('permit_mgmt', 'print_service')
    dot.edge('visitor_view', 'visitors')

    # Save the diagram
    dot.render('system_diagram', format='png', cleanup=True)

if __name__ == '__main__':
    create_system_diagram()
