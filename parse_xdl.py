import requests
import sexpdata
import xml.etree.ElementTree as ET 

def parse_synthesis(root, objects, actions):
    for hardware in root.iter('Hardware'):
        parse_hardware(hardware, objects)
    for reagents in root.iter('Reagents'):
        parse_reagents(reagents, objects)
    for procedure in root.iter('Procedure'):
        parse_procedure(procedure, objects, actions)

def parse_hardware(root, objects):
    for component in root.iter('Component'):
        objects.append(component.attrib['id'])

def parse_reagents(root, objects):
    for reagent in root.iter('Reagent'):
        objects.append(reagent.attrib['name'])

def generate_problem(name, objects, goal):
        objects_str = ' '.join(objects)
        return f'''(define (problem {name})
  (:domain xdl)
  (:objects {objects_str})
  (:init (hand_available))
  (:goal 
    {goal}
  )
)'''

def parse_procedure(root, objects, actions):
    for step in root:
        if step.tag == 'Add':
            vessel = step.attrib['vessel']
            reagent = step.attrib['reagent']
            goal = f'(and (hand_available) (added {vessel} {reagent}))'
            problem = generate_problem('tmp', objects, goal)
            domain = open('/home/naruki/chem-robotics/domain.pddl', 'r').read()

            data = {"domain": domain, "problem": problem}
            
            resp = requests.post('http://118.27.104.245:5000/solve',
                                 verify=False, json=data).json()
            for i, action in enumerate(resp['result']['plan']):
                symbols = sexpdata.loads(action['name'])
                actions.append(symbols)
        else:
            actions.append(['Unimplemented'])

def parse_xdl(xdl):
    root = ET.fromstring(xdl)
    objects = []
    actions = []
    parse_synthesis(root, objects, actions)
    return objects, actions

if __name__ == '__main__':
    XDL = """
<Synthesis>
  <Hardware>
    <Component id="beaker" type="beaker"/>
  </Hardware>
  
  <Reagents>
    <Reagent name="red_cabbage_soup"/>
    <Reagent name="baking_soda_solution"/>
    <Reagent name="vinegar"/>
  </Reagents>
  
  <Procedure>
    <Add vessel="beaker" reagent="red_cabbage_soup" amount="50 mL"/>
  </Procedure>
</Synthesis>
"""
    objects, actions = parse_xdl(XDL)
    action_list = []
    for action in actions:
        action_list.append(action[0].value())
    print(action_list)  # ['pick', 'move', 'pour', 'place']

