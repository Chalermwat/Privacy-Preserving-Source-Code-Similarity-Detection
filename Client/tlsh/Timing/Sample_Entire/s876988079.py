def flood(region_data,flood_data):
    height = 0
    water_num=0
    top=0
    i=-1
    for data in region_data:
        i+=1
        if(data=="\\"):
            if(height==0):
                top=i
            water_num+=height +0.5
            height+=1


        elif(data=="/"):
            if(height>=2):
                water_num+=height-0.5
                height-=1
            elif(height==1):
                water_num+=0.5
                flood_data.append(water_num)
                water_num=0
                height=0


        elif(data=="_"):
            water_num+=height
    if(height==0):
        top=-1
    return top







def flood2(region_data,flood_data):
    height = 0
    water_num=0
    top=0
    i=-1
    for data in region_data:
        i+=1
        if(data=="/"):
            if(height==0):
                top=i
            water_num+=height +0.5
            height+=1


        elif(data=="\\"):
            if(height>=2):
                water_num+=height-0.5
                height-=1
            elif(height==1):
                water_num+=0.5
                flood_data.append(water_num)
                water_num=0
                height=0


        elif(data=="_"):
            water_num+=height
    if(height==0):
        top=-1
    return top


region_data=list(input())
flood_data=[]
top=flood(region_data,flood_data)


if(top!=-1):
    region_data2=region_data[top:len(region_data)]
    region_data2.reverse()
    flood_data2=[]
    flood2(region_data2,flood_data2)
    flood_data2.reverse()
    flood_data_final=flood_data + flood_data2
else:
    flood_data_final=flood_data

flood_data_final=list(map(int,flood_data_final))
total=sum(flood_data_final)
num=[len(flood_data_final)]
flood_data_final=" ".join(list(map(str,num+flood_data_final)))

print(total)
print(f"{flood_data_final}")
