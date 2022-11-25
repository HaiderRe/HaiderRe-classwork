class NodeType:
    def __init__(self,name,pointer):
        self.name = name
        self.pointer = pointer
    #end constructor
    def __repr__(self) -> str:
     return f'(Name: {self.name}; Pointer: {self.pointer})'
    #end function
#end class
x = NodeType("Bob",-1)
x.name = "Ava"
x.pointer = 0
print(x.name, x.pointer)
myList = [NodeType("",x+1) for x in range(9)]
myList.append(NodeType("",-1))

for node in myList:
    print(node.name, node.pointer)
