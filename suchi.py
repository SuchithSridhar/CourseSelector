def StringWorker(lists):
    def PreReqtoJSON(string):
        if ('and' not in string) and ('or' not in string):
            return [string]
        if string=='':
            return ['']
        def orFormatter(s):
            print(s)
            if "(" in s:
                theors = []
                ors = []
                while "(" in s:
                    print(22,s)
                    theors.append((s[s.find("(")+1:s.find(")",s.find("(")) ]))
                    s = s.replace(str("("+(s[s.find("(")+1:s.find(")",s.find("(")) ])+")"),"")
                for x in theors:
                    ors.append(tuple(x.split(' or ')))
                return ors
            print(s,"returnedbyorFORM")
            return [s.strip()]

        def andFormatter(s):
            print(s)
            if "(" in s:
                theors = []
                ors = []
                while "(" in s:
                    theors.append((s[s.find("(")+1:s.find(")",s.find("(")) ]))
                    s = s.replace(str("("+(s[s.find("(")+1:s.find(")",s.find("(")) ])+")"),"")
                for x in theors:
                    ors.append(tuple(x.split(' and ')))
                return ors
            return [s.strip()]

        stuff = []
        ORSOMG = []
        string = string.replace(', ',' and ')
        s = string
        while "(" in s:
            s = s.replace(str("("+(s[s.find("(")+1:s.find(")",s.find("(")) ])+")"),"")
        if ' or ' and ' and ' in s:
            for x in s.split(' or '):
                ORSOMG.append(x)
            print(ORSOMG)
            for jkl in ORSOMG:
                if ' or ' in jkl:
                    for i in jkl.split(' or '):
                        for x in andFormatter(i):
                            try:
                                stuff.append(x.replace('or ','').strip())
                            except AttributeError:
                                stuff.append(x)
                elif ' and ' in jkl:
                    if (len(jkl.split(' and ')))>2:
                        for i in jkl.split(' and '):
                            print(53,i)
                            for x in orFormatter(i):
                                print(55,x)
                                try:
                                    stuff.append(x.replace('and ','').strip())
                                except AttributeError:
                                    stuff.append(x)
                    else:
                        stuff.append(jkl)
                else:
                    stuff.append(jkl)
        if len(ORSOMG)>1:
            bracks = []
            s = string
            while '(' in s:
                bracks.append(str("("+(s[s.find("(")+1:s.find(")",s.find("(")) ])+")"))
                s = s.replace(str("("+(s[s.find("(")+1:s.find(")",s.find("(")) ])+")"),"")
            for s in bracks:
                print(s,"from bracks")
                if ' or ' in s:
                        print("andformatting",s)
                        for x in orFormatter(s):
                            try:
                                stuff.append(x.replace('or ','').strip())
                            except AttributeError:
                                stuff.append(x)
                elif ' and ' in s:
                        print(53,s)
                        for x in andFormatter(s):
                            print(55,x)
                            try:
                                stuff.append(x.replace('and ','').strip())
                            except AttributeError:
                                stuff.append(x)
        else:
            if ' or ' in s:
                for i in string.split(' or '):
                    for x in andFormatter(i):
                        try:
                            stuff.append(x.replace('or ','').strip())
                        except AttributeError:
                            stuff.append(x)
            elif ' and ' in s:
                for i in string.split(' and '):
                    print(53,i)
                    for x in orFormatter(i):
                        print(55,x)
                        try:
                            stuff.append(x.replace('and ','').strip())
                        except AttributeError:
                            stuff.append(x)
        return stuff


    finalprereqlst = []
    prereqlst = []
    c=0


    for ele in lists:
        ele = ele.split("NOTE")[0]
        if "recommended" in ele:
            ele = ele.split(".")[0]     
        prereqlst.append(ele)


    for i in prereqlst:
        c+=1
        print(c)
        if i=='':
            finalprereqlst.append([''])
        elif PreReqtoJSON(i)!=[]:
            thelist=[]
            for j in PreReqtoJSON(i):
                if j!='':
                    if j not in ['and','or']:
                        thelist.append(j)
            finalprereqlst.append(thelist)

    print('\n'*5)
    for element in finalprereqlst:
        print(element,'\n')

StringWorker(["High School Mathematics", "PHYS 1081 or equivalent, or permission from instructor", "CS 1003", "", "", "", "CS 1073", "", "CS 1073", "", "None. NOTE: Intended only for first year computer science students and interested students from other Faculties", "", "", "", "CS 1083. NOTE: Credit is given for at most one of CS 2013, CS 2033, CS 2043, or ECE 4403", "", "CS 2043 or CS 2263 or ECE 4403", "", "CS 2043 or CS 2263 or ECE 4403", "", "", "CS 2263. NOTE: Credit cannot be obtained for CS 2253 by students who have completed both CS 2023 and CS 2813", "CS 1023 or CS 1083. NOTE: Credit will not be given for CS 2263 and CS 2023", "", "CS 1073, CS 1303, and 30 ch", "", "(CS 1083 or ECE 4403) and CS 1303. NOTE: Credit is not given for both CS 2383 and CS 3323", "", "CS 1103, CS 2263, and (MATH 1833 or CS 1303 or equivalent)", "", "CS 1073 or CS1003", "", "CS 1083 or equivalent", "", "CS 1083", "", "CS 2263 or knowledge of Java and C", "", "Experience in programming competition and permission of the instructor", "CS 2263, CS 2383", "60 ch and (CS 2043 or MAAC 3102 or permission of instructor)", "", "CS 2043 or (CS 1083 and MAAC 3102) or permission of instructor", "", "CS 2043. NOTE: Credit is not given for both CS 3013 and CS 3043", "", "CS 1103 and (CS 2043 or ECE 4403). CS 2613 is recommended", "", "(CS 1003 or CS 1073) and (MATH 2213 or MATH 1503)", "", "CS 2333, CS 2383 and (STAT 2593 or STAT 3083). NOTE: Credit is only given for one of CS 3383, CS 3913 and CS 3933", "", "CS 2263 or (CS 1023 and ECE 3221)", "", "CS 1103 and 60 ch", "", "CS 1103 and 60 ch (CS 3413 recommended)", "", "CS 1073 and 60 ch", "", "CS 2253. NOTE: Credit is not given for both CS 3853 and CS 3813", "", "CS 2253 or CS 2263. CS 2263 is recommended", "", "Enrolment in the BCS program and 40 ch completed", "", "CS 2043 or permission of the instructor", "", "CS2043 and 75 ch, or permission of the instructor. CS 3025 is recommended", "", "CS 2413 or approval of the instructor", "", "CS 3413 and (CS 3853 or ECE 3221)", "", "CS 3873 or approval of the instructor", "", "CS 2413 or approval of the instructor", "", "CS 2413 and CS 3873", "", "(CS 2413 and CS 2043) or approval of the instructor", "", "CS 2413 or approval of the instructor", "", "CS 4415 and CS 4419", "", "(CS 1103 or CS 2545) and 75 ch or permission of the instructor. CS 3545 is recommended", "", "CS 2263, CS 2333, and CS 2613", "", "CS 2333 and CS 2383", "", "CS 2263, CS 2613, and (MATH 1503 or MATH 2213)", "", "CS 3853", "", "CS 3383 and (STAT 2593 or STAT 3083)", "", "CS 3413 and CS 3853", "", "CS 3873", "", "CS 2333", "", "CS 3383", "", "CS 3997", "", "Normally, enrolment in the BCS or BScSwE program, at least 90 ch completed, and permission of the instructor", "", "CS 3997. Open to all CS students in their final year with a B average in the previous assessment year or a B CGPA. To receive an Honours designation please refer to the CS Curriculum regulations in the program Section of the Calendar", "", "Instructor approval and at least 90 ch completed", "", "Normally, Faculty approval and at least 90 ch", ""])
