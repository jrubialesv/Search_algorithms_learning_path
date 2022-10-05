import re
problem = get_problem('WGC')

#Expand function for the problem of the farmer with a wolf, goat and cobbage
#A farmer went to a market and purchased a wolf, a goat, and a cabbage. 
#On his way home, the farmer came to the bank of a river and rented a boat. 
#But crossing the river by boat, the farmer could carry only himself and a single one of his purchases: the wolf, the goat, or the cabbage.
#If left unattended together, the wolf would eat the goat, or the goat would eat the cabbage.
#The farmer's challenge was to carry himself and his purchases to the far bank of the river, leaving each purchase intact. 


def expand(parent):
  actions = [] 
  
  #When the farmer is on the left, find all possible moves including forbiden ones
  if 'f' in parent['l']:
    for v in parent['l']:

      nl = parent['l'].copy()
      nl.remove(v)
      if 'f' in nl:
        nl.remove('f')
      nr = parent['r'].copy()
      nr.append(v)
      if 'f' not in nr:
        nr.insert(0,'f')
      ns = {'l':nl,'r':nr}
      actions.append(ns)

  #When the farmer is on the right, find all possible moves including forbiden ones
  elif 'f' in parent['r']:
    for v in parent['r']:
      nr = parent['r'].copy()
      nr.remove(v)
      if 'f' in nr:
        nr.remove('f')
      nl = parent['l'].copy()
      nl.append(v)
      if 'f' not in nl:
        nl.insert(0,'f')
      ns = {'l':nl,'r':nr}
      actions.append(ns)
   # For all actions return the permitted actions
  check_forbiden_states(actions)

  return actions

# Check from all actions the forbidden ones and remove them
def check_forbiden_states(actions):
  action_ = actions.copy()
 
  for i in action_:
    l = ['l', 'r']
    for p in l:
      if 'f' not in i[p]:
        if 'W' in i[p] and 'G' in i[p]:
          actions.remove(i)
        elif 'C' in i[p] and 'G' in i[p]:
          actions.remove(i)

# Transformation of the initial state into a list of two arrays
def transform_initial(initial_state):
  s,r = initial_state.split(",")
  my_prob = {'l': [*s],'r':[*r]}
  return my_prob

# Transform the dictionary of two arrays into the desired string
def transform_last(path, final_path):
  solution_path = []
  for i in final_path:
    join = "".join(i['l']) + "," + "".join(i['r']) 
    solution_path.append(join)
  return "-".join(solution_path)
  
def search(problem, start):
  #Start the queue with the start as a parent and the start of the path
  frontier1 = [(start,[start])]
  
  #Create and array of reached nodes and a bool for the while loop
  reached = []
  solution = False

  while solution == False:
  
    # Extract from queue the first value as BFS follows FIFO
    parent, path = frontier1.pop(0)
    reached.append(parent)

    # For all permitted actions of the node
    for child in expand(parent):
        
        #Check if is the end by checking the condition of left state is empty
        if len(child['l']) == 0:
            solution = True    
            return path + [child]
        # Check if the child has been reached and if not, add it to the frontier and to the reached
        if child not in reached:
          frontier1.append((child, path + [child]))
          reached.append(child)
  
  #If no solution reached return False
  return solution


# Start variable is defined by the problem inital state and transformed for the expand function correct execution
start = transform_initial(problem["initial-state"]) #'fWCG,'

# search fuinction will return the path of the solution
final_path = search(problem, start) 

# Transform the path to the initial format and join them into a path format to submit into the assingment checking system
anwser = transform_last(start, final_path)
print(anwser) # fWGC,-WC,fG-WCf,G-C,fGW-fCG,W-G,fWC-Gf,WC-,fWCG

