import sys
import xml.etree.ElementTree as ET 

objects = []

def parse_synthesis(root):
    for hardware in root.iter('Hardware'):
        parse_hardware(hardware)
    for reagents in root.iter('Reagents'):
        parse_reagents(reagents)
    for procedure in root.iter('Procedure'):
        parse_procedure(procedure)

def parse_hardware(root):
    for component in root.iter('Component'):
        objects.append(component.attrib['id'])

def parse_reagents(root):
    for reagent in root.iter('Reagent'):
        objects.append(reagent.attrib['name'])

def parse_procedure(root):
    for step in root:
        if step.tag == 'Add':
            vessel = step.attrib['vessel']
            reagent = step.attrib['reagent']
            goal = f'(and (hand_available) (added {vessel} {reagent}))'
            print(generate_problem('tmp', goal))

def generate_problem(name, goal):
    objects_str = ' '.join(objects)
    return f'''(define (problem {name})
  (:domain xdl)
  (:objects {objects_str})
  (:init (hand_available))
  (:goal 
    {goal}
  )
)'''



if __name__ == "__main__":
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()

    if root.tag == 'Synthesis':
        parse_synthesis(root)
    else:
        for child in root:
            if child.tag == 'Synthesis':
                parse_synthesis(child)
