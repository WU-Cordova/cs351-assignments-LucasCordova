from datastructures.avltree import AVLTree

def main():
    
    tree = AVLTree[int, int]()
    for node in [8, 9, 10, 2]:
        tree.insert(node, node)
    
    print(tree.bforder())

    def print_node(value: int) -> None:
        print(value)
    
    # using a built higher order func
    _ = tree.bforder(print)
    _ = tree.bforder(print_node)

    visit = print_node

    visit = lambda value: print(value)
    
    _ = tree.bforder(visit)







if __name__ == '__main__':
    main()
