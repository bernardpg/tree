"""
C:\\Users\\黃\\Desktop\\test
TreeExample-BranchInfo.txt
TreeExample-Branches.txt
"""
((3.14-2.255838895368532)/3.14)
########
#Input 兩個TXT
#先定義再放入
#####

def main ():
    from queue import Queue
    import os
    import sys
    from tree_Lzero import OLS_linear_regression as OLS
    #import OLS_linear_regression as OLS
    import numpy as np
    import math 
    q=Queue()
    q_br=Queue()
    my_path = input ('輸入你的路徑:')
    os.chdir(my_path) #切換路徑
    d=input("輸入你要的檔名.txt: ") 
    d=open(d,"w")
###
##data-in
###
    def inpu():
        tree_ex_braninfo=input("輸入braninfo.txt:")
        tree_ex_bran=input("輸入bran.txt:")
        if os.path.isfile(tree_ex_braninfo) and tree_ex_braninfo.endswith('.txt'):
            tree= open(tree_ex_braninfo)
        else: print("no_exist:braninfo")
        if os.path.isfile(tree_ex_bran) and tree_ex_bran.endswith('.txt'):
            tre= open(tree_ex_bran)
        else: print("no_exist:bran")
        braninfo=tree.readlines()
        bran=tre.readlines()
        return braninfo,bran
#list = os.listdir(my_path)
###
#data_process-ini
###
    def d_process_ini(infor):
        braninfo=infor[0]
        bran=infor[1]
        bran_info=[]
        bran_ex=[]
        total_branch = []
        i=0
        level=0
        bran_info=[]
        compa=[]
        length_ratio=[]
        ini_data=[]
        bran_local_in=[]
        local=input("local_structure : ")
        for var in braninfo:
            if var.startswith('Total branch point'):
                uid = var.split()[5]
                total_branch.append([uid])
         #bran_name = bran_cp = bran_volength = bran_level = bran_parent = None
            elif var.startswith('TreeExample',21):
                bran_name = var.split()[0]
                bran_cp = var.split()[1]
                bran_volength = var.split()[4]
                bran_level = var.split()[12]
                bran_parent = var.split()[13]
                compa.append(int(bran_cp))#total-every-cp
                bran_info.append([bran_name,bran_cp,bran_volength,bran_level,bran_parent])
        compar=sorted(compa,key=float)
        if int(local) < 3:
            print("variable less than need")
            sys.exit(1)
        if int(local) > compar[0] :
            print("variable less than that branch_length")
            print("min branch_length : "+ str(compar[0]))
            sys.exit(1)
        local=int(local) #local_structure
        
        for var in bran:
            i=i+1
            if var.startswith("Parent ID = 0"):
        #initialize
                bran_ex_ID=bran[i-2]
                #bran_ex_parentID=bran[i-1]
                bran_ex_level=bran[i]
                bran_ex_CP=bran[i+1]
                bran_ex_CP=bran_ex_CP.split()
                bran_ex_vlength=bran[i+4]
                cp=int(bran_ex_CP[2])
                BP_num=bran[cp+14+i]
                bp=int(BP_num.split()[2])
                BP_CHild_ID=[]
                for cha in range(1,bp+1):
                    BP_CHild_ID.append(bran[cp+15+i+bp+cha])
                bran_ex_cp_num=[]
                bran_local_in_z=[]
                bran_local_in_x=[]
                bran_local_in_y=[]
                for num in range(1,cp+1):
                    bran_ex_cp_num.append(bran[i+12+num])
                for ws in range(i+12+cp,(i+12+cp-local),-1):
                    z=int(bran[ws].split()[0])
                    x=int(bran[ws].split()[1])
                    y=int(bran[ws].split()[2])
                    bran_local_in_z.append(z)
                    bran_local_in_x.append(x)
                    bran_local_in_y.append(y)
                level=1
        bran_local_in.append([bran_local_in_z,bran_local_in_y,bran_local_in_x])
        def offspring(BP_CHild_ID):
            div=[]
            for var in BP_CHild_ID:
                x=var.split()[3]
                div.append(x)
            return div
        d.write("total_branch:")
        d.write(str(total_branch[0]))
        d.write("\n")
        d.write("==============")
        d.write("\n")
        d.write("from: ")
        d.write(str(bran_ex_ID))
        d.write("\n")
        d.write(str(bran_ex_vlength))
        d.write("\n")
        div=offspring(BP_CHild_ID)
        BP_CHild=[]
        child_le=[]
        #倒敘
        d.write("to: ")
        d.write("\n")
        ###先比較長度
        #根據長度找哪個
        #數據點
        ####
        XD=[]
        bran_chi=[]
        #外面調用np.array
        #append([])
        for i in range(len(div)-1, -1, -1): 
            child=div.pop(i)
            a="ID = "
            a=a+str(int(child))+("\n")
            XD.append(a)
            t=0
            #裡面調用list append
            ### need _ 修改按照長度順序(將數據點也一併輸出)
            for var in bran:
                t=t+1
                if var.startswith("ID") and a == bran[t-1]   :
                    child_vlength=bran[t+5].split()[2]
                    voxel=bran[t+5].split()[0]
                    eq=bran[t+5].split()[1]
                    voxel_length=bran[t+5].split()[2]#voxel_length
                    XD.append(voxel)
                    XD.append(eq)
                    XD.append(voxel_length)
                    child_vlength=float(child_vlength)
                    child_le.append(child_vlength)
        child_le=sorted(child_le,key=float,reverse=True)#finish sort
        #sort finish 再 load 一次 把 branch 拿出來
        bran_ex_vlength=float(bran_ex_vlength.split()[2])
        length_ratio.append([1])
        for dd in child_le:
            length_ratio.append([float((float(dd))/bran_ex_vlength)])
        for R in  child_le:
            for dd in range(len(XD)) :
                if  XD[dd] == str(R):
                    d.write(XD[dd-3])
                    d.write(XD[dd-2])
                    d.write(XD[dd-1])
                    d.write(XD[dd])
                    d.write("\n")
                    bran_chi.append(XD[dd-3])
        bran_local_out=[]
        for r in bran_chi:
            t=0
            for var in bran:
                t=t+1
                if var.startswith("ID") and r == bran[t-1]   :
                    bran_local_ch_z=[]
                    bran_local_ch_x=[]
                    bran_local_ch_y=[]
                    cp_num=int(bran[t+2].split()[2])
                    for ww in range(t+13+cp_num,(t+13+cp_num-local),-1):
                        z=int(bran[ww].split()[0])
                        x=int(bran[ww].split()[1])
                        y=int(bran[ww].split()[2])
                        bran_local_ch_z.append(z)
                        bran_local_ch_x.append(x)
                        bran_local_ch_y.append(y)
            bran_local_out.append([bran_local_ch_z,bran_local_ch_x,bran_local_ch_y])
        cof_init=[]
        for leng in range(len(bran_local_in)) :
            ini=bran_local_in[leng]
            for lengt in range(len(ini)) :
                z=np.array(ini[0])
                x=np.array(ini[1])
                y=np.array(ini[2])
            cof_ini=OLS.main(x,y,z)
            cof_init.append(cof_ini)
        cof_out=[]
        
        for leng in range(len(bran_local_out)) :
            ini=bran_local_out[leng]
            for lengt in range(len(ini)) :
                z=np.array(ini[0])
                x=np.array(ini[1])
                y=np.array(ini[2])
            cof_ini=OLS.main(x,y,z)
            q_br.put(cof_ini)
            cof_out.append([cof_ini])
        arc=[]
        for leng in range(len(cof_init)) :
            for lengt in range(len(cof_out)):
                coff=((cof_out[lengt])[:])
                theta=np.arccos(np.dot(cof_init[leng],coff[0]))
                if theta > (math.pi/2) :
                    theta=math.pi-theta
                arc.append(theta)
        tt=q_br.qsize()
        ##內積得後續的解(將裡面的計算)
        def bran_inner(tt,cof_out) :
            for vr in range(tt-1) :
                tr=q_br.get()
                for ar in range(vr+1,len(cof_out)):
                    coff=((cof_out[ar])[:])
                    theta=np.arccos((np.dot(tr,coff[0])))
                    if theta > (math.pi/2) :
                        theta=math.pi-theta
                    arc.append(theta)
            q_br.get()
            return
        bran_inner(tt,cof_out)            
        d.write("\n")
        d.write("level zero : ")
        d.write(str(level))
        d.write("\n")
        d.write("length_ratio :")
        d.write(str(length_ratio))
        d.write("\n")
        d.write("\n")
        d.write("theta_ratio :")
        d.write(str(arc))
        d.write("\n")
        d.write("==============")
        d.write("\n")
        d.write(str(bran_ex_ID))
        d.write("\n")
        for dd in bran_ex_cp_num:
            d.write(str(dd))
        d.write("==============")
        return child_le,BP_CHild_ID,bran_info,level,compa,local
###advance_process
##sorting 順序
##放入queue
##小bug
###
    def sorting(ini,q):
        child_le=ini[0]
        BP_CHild_ID=ini[1]
        bran_info=ini[2]
        t=0
        for d in child_le:
            for var in bran_info:
                if (float(var[2])) == d:
                    t=t+1
                    cd=var[0]
                    q.put(cd)
        return t #總共幾個
    
    def sorting_ad(ini,q):
        for ch in ini:
            child_le=ch[0]
            BP_CHild_ID=ch[1]
            bran_info=ch[2]
            t=0
            for dd in child_le:
                for var in bran_info:
                    if (float(var[2])) == dd:
                        t=t+1
                        cd=var[0]
                        q.put(cd)
        return t #總共幾個
###
##需要建立如果offspring ID=0 return
##input(offspring)
###
    def d_process_a(q,t):
        proce_ID=[]
        for var in range(t):
            proce_ID.append(q.get())
        if proce_ID == [] :
            return proce_ID
        return proce_ID
    def d_process_ad(proce_ID,infor,level,compa,local):
        braninfo=infor[0]
        bran=infor[1]
        bran_info=[]
        bran_local_in=[]
        local
        for var in braninfo:
            if var.startswith('TreeExample',21):
                bran_name = var.split()[0]
                bran_cp = var.split()[1]
                bran_volength = var.split()[4]
                bran_level = var.split()[12]
                bran_parent = var.split()[13]
                bran_info.append([bran_name,bran_cp,bran_volength,bran_level,bran_parent])
        if proce_ID == []:
            return
        def offspring(BP_CHild_ID):
            div=[]
            for var in BP_CHild_ID:
                x=var.split()[3]
                div.append(x)
            return div
        #倒敘
        fk=0
        d.write("\n")
        d.write("==============")
        for ch in proce_ID:
            i=0
            length_ratio=[]
            BP_CHild_ID=[]
            bran_ex_cp_num=[]
            BP_CHild=[]
            child_le=[]
            ini=[]
            bran_local_in=[]
            bran_local_out=[]
            bran_local_in_z=[]
            bran_local_in_x=[]
            bran_local_in_y=[]
            for var in bran:
                i=i+1
                if ch in var:#ID相同
                    #print(ch)
                    bran_ex_ID=bran[i]
                #bran_ex_parentID=bran[i-1]
                    bran_ex_level=bran[i+2]
                    bran_ex_CP=bran[i+3]
                    bran_ex_CP=bran_ex_CP.split()
                    bran_ex_vlength=bran[i+6]
                    cp=int(bran_ex_CP[2])
                    BP_num=bran[cp+16+i]
                    bp=int(BP_num.split()[2])
                    
                    for cha in range(1,bp+1):
    
                        BP_CHild_ID.append(bran[cp+17+i+bp+cha])
                    
                    for num in range(1,cp+1):
                        bran_ex_cp_num.append(bran[i+14+num])
                    for ws in range(i+14+cp,(i+14+cp-local),-1):
                        z=int(bran[ws].split()[0])
                        x=int(bran[ws].split()[1])
                        y=int(bran[ws].split()[2])
                        bran_local_in_z.append(z)
                        bran_local_in_x.append(x)
                        bran_local_in_y.append(y)
                    div=offspring(BP_CHild_ID)
                    bran_chi=[]
                    XD=[]
                    for i in range(len(div)-1, -1, -1):
                        child=div.pop(i)
                        a="ID = "
                        a=a+str(int(child))+("\n")
                        XD.append(a)
                        t=0
                        ### need _ 修改按照長度順序(將數據點也一併輸出)
                        for var in bran:
                            t=t+1
                            if var.startswith("ID") and a == bran[t-1]   :
                                child_vlength=bran[t+5].split()[2]
                                voxel=bran[t+5].split()[0]
                                x=bran[t+5].split()[1]
                                voxel_length=bran[t+5].split()[2]#voxel_length
                                XD.append(voxel)
                                XD.append(x)
                                XD.append(voxel_length)
                                child_vlength=float(child_vlength)
                                child_le.append(child_vlength)
                                child_le=sorted(child_le,key=float,reverse=True)#finish sort
                    bran_local_in.append([bran_local_in_z,bran_local_in_y,bran_local_in_x])
                    bran_ex_vlength_new=float(bran_ex_vlength.split()[2])
                    if len(child_le) == 0 :
                        break
                    else :
                        level=level+1
                        length_ratio.append([1])
                        for dd in child_le:
                            length_ratio.append([float((float(dd))/bran_ex_vlength_new)])
                        d.write("\n")
                        d.write("from: ")
                        d.write(str(bran_ex_ID))
                        d.write("\n")
                        d.write(str(bran_ex_vlength))
                        d.write("\n")
                        d.write("to: ")
                        d.write("\n")
                        for R in  child_le:
                            for dd in range(len(XD)) :
                                if  XD[dd] == str(R):
                                    d.write(XD[dd-3])
                                    d.write(XD[dd-2])
                                    d.write(XD[dd-1])
                                    d.write(XD[dd])
                                    bran_chi.append(XD[dd-3])
                                    d.write("\n")
                        bran_local_out=[]
                        for r in bran_chi:
                            t=0
                            for var in bran:
                                t=t+1
                                if var.startswith("ID") and r == bran[t-1]   :
                                    bran_local_ch_z=[]
                                    bran_local_ch_x=[]
                                    bran_local_ch_y=[]
                                    cp_num=int(bran[t+2].split()[2])
                                    for ww in range(t+12+cp_num,(t+12+cp_num-local),-1):
                                        z=int(bran[ww].split()[0])
                                        x=int(bran[ww].split()[1])
                                        y=int(bran[ww].split()[2])
                                        bran_local_ch_z.append(z)
                                        bran_local_ch_x.append(x)
                                        bran_local_ch_y.append(y)
                            bran_local_out.append([bran_local_ch_z,bran_local_ch_x,bran_local_ch_y])
                        cof_init=[]
                        for leng in range(len(bran_local_in)) :
                            init=bran_local_in[leng]
                            for lengt in range(len(init)) :
                                z=np.array(init[0])
                                x=np.array(init[1])
                                y=np.array(init[2])
                            cof_ini=OLS.main(x,y,z)
                            cof_init.append(cof_ini)
                        cof_out=[]
                        for leng in range(len(bran_local_out)) :
                            init=bran_local_out[leng]
                            for lengt in range(len(init)) :
                                z=np.array(init[0])
                                x=np.array(init[1])
                                y=np.array(init[2])
                            cof_ini=OLS.main(x,y,z)
                            q_br.put(cof_ini)
                            cof_out.append([cof_ini])
                        arc=[]
                        for leng in range(len(cof_init)) :
                            for lengt in range(len(cof_out)):
                                coff=((cof_out[lengt])[:])
                                theta=np.arccos(np.dot(cof_init[leng],coff[0]))
                                if theta > (math.pi/2) :
                                    theta=math.pi-theta
                                arc.append(theta)
                        tt=q_br.qsize()
                        ##內積得後續的解(將裡面的計算)
                        def bran_inner(tt,cof_out) :
                            for vr in range(tt-1) :
                                tr=q_br.get()
                                for ar in range(vr+1,len(cof_out)):
                                    coff=((cof_out[ar])[:])
                                    theta=np.arccos((np.dot(tr,coff[0])))
                                    if theta > (math.pi/2) :
                                        theta=math.pi-theta
                                    arc.append(theta)
                            q_br.get()
                            return
                        bran_inner(tt,cof_out)            
                        d.write("\n")
                        d.write("level zero : ")
                        d.write(str(level))
                        d.write("\n")
                        d.write("length_ratio :")
                        d.write(str(length_ratio))    
                        d.write("\n")
                        d.write("\n")
                        d.write("theta_ratio :")
                        d.write(str(arc))
                        d.write("\n")
                        d.write("==============")
                        d.write("\n")
                        d.write(str(bran_ex_ID))
                        d.write("\n")
                        for dd in bran_ex_cp_num:
                            d.write(str(dd))
                        d.write("\n")
                        d.write("==============")
                        ini.append([child_le,BP_CHild_ID,bran_info,level])
                        fk=fk+sorting_ad(ini,q)
                    #return child_le,BP_CHild_ID,bran_info
    
        proce_ID=d_process_a(q,fk)  
        d_process_ad(proce_ID,infor,level,compa,local)        
#####call(offspring):length
###執行function
    
    infor=inpu()           
    ini=d_process_ini(infor)
    local=ini[5]
    compa=ini[4]
    level=ini[3]
    t=sorting(ini,q)
    proce_ID=d_process_a(q,t)
    d_process_ad(proce_ID,infor,level,compa,local)
    d.close()
if __name__ == "__main__":
  main()
