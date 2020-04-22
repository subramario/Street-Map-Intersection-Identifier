import sys
import re
import numpy
# YOUR CODE GOES HERE
def checks(x1,y1,x2,y2,x3,y3,x4,y4):
    try:
        t = ( ((x1-x3)*(y3-y4)) - ((y1-y3)*(x3-x4)) )/( ((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4)) )
        u = -( ((x1-x2)*(y1-y3)) - ((y1-y2)*(x1-x3)) )/( ((x1-x2)*(y3-y4)) - ((y1-y2)*(x3-x4)) )

        if (u < 0 or u > 1 or t < 0 or t > 1):
            return 0

        if ((0 <= u <= 1) and (0 <= t <= 1)):
            x_coord = x1 + (t * (x2 - x1))
            y_coord = y1 + (t * (y2 - y1))
            return [(float("{0:.2f}".format(x_coord)),float("{0:.2f}".format(y_coord)))]
    except:
        if ((x3 <= x1 <= x4 and x3 <= x2 <= x4 and y3 <= y1 <= y4 and y3 <= y2 <= y4) or
            (x4 <= x1 <= x3 and x4 <= x2 <= x3 and y4 <= y1 <= y3 and y4 <= y2 <= y3) or
            (x3 <= x1 <= x4 and x3 <= x2 <= x4 and y3 >= y1 >= y4 and y3 >= y2 >= y4) or
            (x4 <= x1 <= x3 and x4 <= x2 <= x3 and y4 >= y1 >= y3 and y4 >= y2 >= y3)):
            return [(x1, y1), (x2, y2)]

        if ((x2 <= x3 <= x1 and x2 <= x4 <= x1 and y2 <= y3 <= y1 and y2 <= y4 <= y1) or
            (x1 <= x3 <= x2 and x1 <= x4 <= x2 and y1 <= y3 <= y2 and y1 <= y4 <= y2) or
            (x2 <= x3 <= x1 and x2 <= x4 <= x1 and y2 >= y3 >= y1 and y2 >= y4 >= y1) or
            (x1 <= x3 <= x2 and x1 <= x4 <= x2 and y1 >= y3 >= y2 and y1 >= y4 >= y2)):
            return [(x3, y3), (x4, y4)]

        if ((x1 <= x3 <= x2 <= x4 and y1 >= y3 >= y2 >= y4) or
            (x4 <= x2 <= x3 <= x1 and y4 >= y2 >= y3 >= y1) or
            (x1 >= x3 >= x2 >= x4 and y1 >= y3 >= y2 >= y4) or
            (x4 >= x2 >= x3 >= x1 and y4 >= y2 >= y3 >= y1)):
            return [(x3, y3), (x2, y2)]

        if ((x1 <= x4 <= x2 <= x3 and y1 >= y4 >= y2 >= y3) or
            (x3 <= x2 <= x4 <= x1 and y3 >= y2 >= y4 >= y1) or
            (x1 >= x4 >= x2 >= x3 and y1 >= y4 >= y2 >= y3) or
            (x3 >= x2 >= x4 >= x1 and y3 >= y2 >= y4 >= y1)):
            return [(x2, y2), (x4, y4)]
        
        if ((x2 <= x4 <= x1 <= x3 and y2 >= y4 >= y1 >= y3) or
            (x3 <= x1 <= x4 <= x2 and y3 >= y1 >= y4 >= y2) or
            (x2 >= x4 >= x1 >= x3 and y2 >= y4 >= y1 >= y3) or
            (x3 >= x1 >= x4 >= x2 and y3 >= y1 >= y4 >= y2)):
            return [(x1, y1), (x4, y4)]

        if ((x4 <= x1 <= x3 <= x2 and y4 >= y1 >= y3 >= y2) or
            (x2 <= x3 <= x1 <= x4 and y2 >= y3 >= y1 >= y4) or
            (x4 >= x1 >= x3 >= x2 and y4 >= y1 >= y3 >= y2) or
            (x2 >= x3 >= x1 >= x4 and y2 >= y3 >= y1 >= y4)):
            return [(x1, y1), (x3, y3)]
    
    return 0

def distance(refx, refy, intx, inty):
    dist = sqrt((intx - refx)**2 + (inty - refy)**2)
    return dist

def main():

    a = re.compile(r'^\s*[a]\s+["][a-zA-Z\s]+\s*["]\s+([(]\s*-?[0-9]+\s*[,]\s*-?[0-9]+\s*[)]\s*){2,}\s*$')
    c = re.compile(r'^\s*[c]\s+["][a-zA-Z\s]+\s*["]\s+([(]\s*-?[0-9]+\s*[,]\s*-?[0-9]+\s*[)]\s*){2,}\s*$')
    r = re.compile(r'^\s*[r]\s+["][a-zA-Z\s]+\s*["]\s*$')
    g = re.compile(r'^\s*[g]\s*$')

    condition = True
    street_info = {}

    while condition:
        prompt = input()

        count = 0
        for key in street_info:
            count += 1

        street = re.search('["][a-zA-Z\s]+\s*["]', prompt)
        coord = re.search('([(]\s*-?[0-9]+\s*[,]\s*-?[0-9]+\s*[)]\s*){2,}\s*', prompt)

        if a.fullmatch(prompt):
            street_key = street.group().lower() 
            street_value = coord.group().replace(" ", "").replace(")", ".0)").replace(",", ".0,").replace(")(", ") (").split(" ")

            if street_key in street_info:
                print("Error: Street name already exists in the system, no duplicate entries allowed.", file = sys.stderr)
            else:
                street_info[street_key] = street_value
                count += 1

        elif c.fullmatch(prompt):
            if count == 0:
                print("Error: Cannot change specified street when no street has been added to the system.", file = sys.stderr)
            else:
                street_key = street.group().lower() 
                street_value = coord.group().replace(" ", "").replace(")", ".0)").replace(",", ".0,").replace(")(",") (").split(" ")
              
                if street_key in street_info:
                    street_info[street_key] = street_value
                else:
                    print("Error: 'c' specified for a street that does not exist.", file = sys.stderr)
                    
        elif r.fullmatch(prompt):
            if count == 0:
                print("Error: System does not have any entries to remove.", file = sys.stderr)
            else:
                street_key = street.group()
                if street_key in street_info:
                    del street_info[street_key]
                    count -= 1
                else:
                    print("Error: 'r' specified for a street that does not exist.", file = sys.stderr)
                   
        elif g.fullmatch(prompt):
            check = not bool(street_info)

            if check == True:
                print("Error: Cannot issue graphing command as no streets have been added.", file = sys.stderr)
            else:
                converted = {}
                for key,value in street_info.items():
                    converted[str(key)] = [eval(item) for item in value]

                vertices = []
                edges = []
                for key_temp in converted:
                
                    ip_dict = {}

                    value_curr = converted[key_temp]

                    for i in range(0, len(value_curr) - 1):
                        x1, y1 = value_curr[i][0], value_curr[i][1]
                        x2, y2 = value_curr[i + 1][0], value_curr[i + 1][1]
                        
                        for key in converted:

                            if key != key_temp:
                                other_street_val = converted[key]

                                for k in range(0, len(other_street_val) - 1):
                                    x3, y3 = other_street_val[k][0], other_street_val[k][1]
                                    x4, y4 = other_street_val[k + 1][0], other_street_val[k + 1][1]

                                    ip = checks(x1,y1,x2,y2,x3,y3,x4,y4)

                                    if ip != 0:
                                        for pt in ip:
                                            if pt in ip_dict:
                                                val = ip_dict[pt]
                                                val.append((x1, y1))
                                                val.append((x2, y2))
                                                val.append((x3, y3))
                                                val.append((x4, y4))
                                            else:
                                                ip_dict[pt] = [(x1, y1),(x2, y2),(x3, y3),(x4, y4)]

                    for x in range(0, len(value_curr) - 1):
                        
                        temp = []

                        p_x1, p_y1 = value_curr[x][0], value_curr[x][1]
                        p_x2, p_y2 = value_curr[x + 1][0], value_curr[x + 1][1]

                        for key_ip in ip_dict:

                            val = ip_dict[key_ip] 
                        
                            for j in range(0,len(val) - 1):

                                p1, q1 = val[j][0], val[j][1]
                                p2, q2 = val[j+1][0], val[j+1][1]
                                
                                if p_x1 == p1 and p_y1 == q1 and p_x2 == p2 and p_y2 == q2:
                                    if key_ip not in temp:
                                       
                                        temp.append(key_ip) 
                                    break
                                j = j + 1

                        if len(temp) > 1:
                            Ap = numpy.array([p_x1, p_y1])  
                            B = numpy.asarray(temp)  
                            dist = numpy.linalg.norm(B - Ap, ord=2,axis=1)  
                            sorted_B = B[numpy.argsort(dist)]
                
                            temp = sorted_B.tolist()
                            temp = [tuple(y) for y in temp]

                        if len(temp) >= 1:
                            temp.insert(0,(p_x1, p_y1))
                            temp.append((p_x2, p_y2))

                        final_list = []
                        for intersection in temp:
                             if intersection not in final_list:
                                final_list.append(intersection)
                       
                        if len(final_list) >= 2:
                            
                            for j in range(0,len(final_list)-1):
                                edges.append((final_list[j], final_list[j+1]))
                                
                final_edge = []        
                for item in edges:
                    if item not in final_edge:
                        final_edge.append(item)

                f_edge = []
                for y in range(0, len(final_edge)):
                    duplicate_1 = (final_edge[y][0], final_edge[y][1])
                    duplicate_2 = (final_edge[y][1], final_edge[y][0])
                    if (duplicate_1 not in f_edge) and (duplicate_2 not in f_edge):
                        f_edge.append(duplicate_1)
                
                for x in range(0, len(f_edge)):

                    if f_edge[x][0] not in vertices:
                        vertices.append(f_edge[x][0])

                    if f_edge[x][1] not in vertices:
                        vertices.append(f_edge[x][1])

                if len(vertices) == 0:
                    print("V = {")
                    print("}")
                else:
                    print("V = {")
                    i = 1
                    for item in vertices:
                        print("\t",i,":\t",item, sep = "")
                        i += 1
                    print("}")

                if len(f_edge) == 0:
                    print("E = {")
                    print("}")
                    
                elif len(f_edge) == 1:
                    print("E = {")
                    x = vertices.index(f_edge[0][0])+1
                    y = vertices.index(f_edge[0][1])+1
                    print("\t<",x,",",y,">", sep = "")
                    print("}")
                    
                else:
                    print("E = {")
                    for j in range(0, len(f_edge)-1):
                        x = vertices.index(f_edge[j][0])+1
                        y = vertices.index(f_edge[j][1])+1
                        print("\t<",x,",",y,">,", sep = "")
                    j += 1
                    x = vertices.index(f_edge[j][0])+1
                    y = vertices.index(f_edge[j][1])+1
                    print("\t<",x,",",y,">", sep = "")
                    print("}")
        else:
            print("Error: Invalid entry. Please adhere to the specified format and enter command again.", file = sys.stderr)

if __name__ == '__main__':
    main()




