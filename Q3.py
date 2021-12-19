def Pascal_Triangle(N):
 
    for layer in range(1, N + 1):
        
        # The start value in each layer is 1
        s = 1
        
        for i in range(1, layer + 1):
            
            print(s, end = " ")
            
            # update the following value in current layer
            s = int(s * (layer - i) / i)
        
        # finish current layer,move next layer to new line
        print("")

#the 1st 4 layers
N = 4;
Pascal_Triangle(N)