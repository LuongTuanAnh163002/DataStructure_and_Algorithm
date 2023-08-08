# def sortstack(stacks):
#     tmpstacks = []
#     while len(stacks) > 0:
#         tmp = stacks[-1]
#         stacks.pop()
#         while len(tmpstacks) > 0 and tmpstacks[-1] < tmp:
#             stacks.append(tmpstacks[-1])
#             tmpstacks.pop()
#             
#         tmpstacks.append(tmp)
#         
#     return tmpstacks
# 
# stack = [9, 8, 7, 6, 5, 4]
# new_stack = sortstack(stack)
# print(new_stack)