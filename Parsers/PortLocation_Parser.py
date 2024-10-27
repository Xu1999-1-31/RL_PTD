def Read_PortLocation(inrpt):
    with open(inrpt, 'r') as infile:
        lines = infile.readlines()
        PortList = {}
        for line in lines:
            index = line.split()
            if(len(index) > 0):
                bbox = []
                bbox.append((float(index[1].replace('{', '')), float(index[2].replace('}', ''))))
                bbox.append((float(index[3].replace('{', '')), float(index[4].replace('}', ''))))
                PortList[index[0]] = bbox
            
    return PortList