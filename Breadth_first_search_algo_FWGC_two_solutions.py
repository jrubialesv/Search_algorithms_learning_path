# Requiered code from Breadth_first_search_algo_FWGC.py

# this algorithm will find two possible solutions
def search2(problem, start):
  first1 = []
  path1 = []
  path2 = []  
  frontier2 = [(start,[start])]
  reached2 = []
  solution = False

  while solution == False:
    parent, path = frontier2.pop(0)
    reached2.append(parent)

    for child in expand(parent):

        if len(child['l']) == 0:
          # Put the condition of first solution reached and verify not the same end
          if len(first1) == 0:
            first1.append(child)
            path1 = path + [child]
            # return the two paths 
          elif first1[0] != child:
            path2 = path + [child]   
            return path1, path2
        
        # Add to the queue and array (frontier2 and reached2) if child has not been visited
        if child not in reached2:
          frontier2.append((child, path + [child]))
          reached2.append(child)
  #If no solution reached return False
  return solution


# Start variable is defined by the problem inital state and transformed for the expand function correct execution
start = transform_initial(problem["initial-state"])

# search fuinction will return the path of the solution
result = search2(problem, start)

# The result will return two vaulable outcomes
final_path1 = result[0]
final_path2 = result[1]

# Transform the path to the initial format and join them into a path format to submit into the assingment checking system x2
anwser1 = transform_last(start, final_path1)
anwser2 = transform_last(start, final_path2)

print(anwser1,"\n \n",anwser2)

# The funciton 'submit_anwser' does not work if all the letters are not in - 
# the exact postion even if they are in the same state
#'fWGC,-WC,fG-fWC,G-W,fCG-fWG,C-G,fWC-fG,WC-,fWGC'
