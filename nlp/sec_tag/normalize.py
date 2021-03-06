#!/usr/bin/env python3

# map of frequently encountered synonyms and their 'normalized' form
NORM_MAP = {
    'additions':'addition',
    'administered':'administer',
    'admitting':'admit',
    'antibiotics':'antibiotic',
    'allergens':'allergen',
    'allergies':'allergy',
    'ankles':'ankle',
    'appointments':'appointment',
    'arrangements':'arrangement',
    'arteries':'artery',
    'assistants':'assistant',
    'alleviating':'alleviate',
    'biopsies':'biopsy',
    'breathing':'breathe',
    'breasts':'breast',
    'bruits':'bruit',
    'buttocks':'buttock',
    'changes':'change',
    'chemotherapy':'chemo',
    'children':'child',
    'clotting':'clot',
    'complaints':'complaint',
    'complications':'complication',
    'codes':'code',
    'corrections':'correction',
    'counts':'count',
    'defects':'defect',
    'deficits':'deficit',
    'digits':'digit',
    'diseases':'disease',
    'disorders':'disorder',
    'drugs':'drug',
    'eating':'eat',
    'elbows':'elbow',
    'electrolytes':'electrolyte',
    'estimated':'estimate',
    'examination':'exam',
    'extremities':'extremity',
    'eyes':'eye',
    'factors':'factor',
    'feet':'foot',
    'fields':'field',
    'findings':'finding',
    'fluids':'fluid',
    'follows':'follow',
    'goals':'goal',
    'grandparents':'grandparent',
    'habits':'habit',
    'hands':'hand',
    'herbals':'herbal',
    'hips':'hip',
    'hospitalizations':'hospitalization',
    'identifying':'identify',
    'illnesses':'illness',
    'impressions':'impression',
    'immunizations':'immunization',
    'immunosuppressants':'immunosuppresant',
    'indications':'indication',
    'injuries':'injury',
    'instructions':'instruction',
    'issues':'issue',
    'joints':'joint',
    'knees':'knee',
    'labs':'lab',
    'legs':'leg',
    'living':'live',
    'lungs':'lung',
    'measurements':'measurement',
    'medications':'medication',
    'murmurs':'murmur',
    'neoplasms':'neoplasm',
    'nerves':'nerve',
    'nodes':'node',
    'obtained':'obtain',
    'parents':'parent',
    'performed':'perform',
    'planning':'plan',
    'pregnancies':'pregnancy',
    'problems':'problem',
    'procedures':'procedure',
    'products':'product',
    'providers':'provider',
    'radiographs':'radiograph',
    'reactions':'reaction',
    'recommendations':'recommendation',
    'referring':'refer',
    'reflexes':'reflex',
    'reports':'report',
    'requesting':'request',
    'results':'result',
    'ribs':'rib',
    'risks':'risk',
    'seizures':'seizure',
    'shoulders':'shoulder',
    'siblings':'sibling',
    'signed':'sign',
    'sounds':'sound',
    'sources':'source',
    'stds':'std',
    'stressors':'stressor',
    'structures':'structure',
    'studies':'study',
    'substances':'substance',
    'supplements':'supplement',
    'symptoms':'symptom',
    'systems':'system',
    'teeth':'tooth',
    'testes':'teste',
    'testicles':'testicle',
    'tests':'test',
    'therapies':'therapy',
    'toes':'toe',
    'transfusions':'transfusion',
    'treatments':'treatment',
    'vaccinations':'vaccination',
    'vessels':'vessel',
    'visits':'visit',
    'vomiting':'vomit',
    'wrists':'wrist',
    'x-ray':'xray'
}
