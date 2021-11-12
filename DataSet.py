import pymongo as pymon

class DataSet(object) :
    dbs = {}
    def __init__(self,ip,port):
        serviceip = 'mongodb://{}:{}/'.format(ip,port)
        self.myclient = pymon.MongoClient(serviceip)
        #self.myclient = pymon.MongoClient("mongodb://localhost:27017/")
        pass
    def LinktoDB(self,DBname) :
        if self.myclient.list_database_names().__contains__(DBname) == False :
            return False,"No DBName[{}]".format(DBname)
        if self.dbs.__contains__(DBname) == False :
            self.dbs.setdefault(DBname,{})
        if self.dbs[DBname].__contains__("DB") == False :
            self.dbs[DBname].setdefault("DB",self.myclient[DBname])
            self.dbs[DBname].setdefault("Collections",{})
        return True,""
    def LinktoCollection(self,DBname,collect) :
        if self.checkDBs(DBname) == False:
            return False,"No DBName[{}]".format(DBname)
        if self.dbs[DBname]["Collections"].__contains__(collect) == False :
            if self.dbs[DBname]["DB"].list_collection_names().__contains__(collect) :
                self.dbs[DBname]["Collections"].setdefault(collect,self.dbs[DBname]["DB"][collect])
                return True,""
            else :
                return False,"No Collect[{}] in {}".format(collect,DBname)
        else :
            return True,"Collect Connected"
    def checkDBs(self,DBname) :
        return self.dbs.__contains__(DBname)
    def InsertData(self,DBname,collect,mongodataset) :
        if self.checkDBs(DBname) == False:
            return False,"No DBName[{}]".format(DBname)       
        if self.dbs[DBname]["Collections"].__contains__(collect) == False : 
            return False,"No Collect[{}] in {},please link collection first".format(collect,DBname)
        self.dbs[DBname]["Collections"][collect].insert_one(mongodataset)
        return True,""
    def UpdateData(self,DBname,collect,query,mongodataset) :
        if self.checkDBs(DBname) == False:
            return False,"No DBName[{}]".format(DBname)       
        if self.dbs[DBname]["Collections"].__contains__(collect) == False : 
            return False,"No Collect[{}] in {},please link collection first".format(collect,DBname)
        check = self.dbs[DBname]["Collections"][collect].find(query)
        if len(check) > 0 :
            self.dbs[DBname]["Collections"][collect].update_one(query, mongodataset)
            return True,str(len(check))
        else :
            return False,"Query Fail"
    def RemoveData(self,DBname,collect,query) :
        if self.checkDBs(DBname) == False:
            return False,"No DBName[{}]".format(DBname)       
        if self.dbs[DBname]["Collections"].__contains__(collect) == False : 
            return False,"No Collect[{}] in {},please link collection first".format(collect,DBname)
        check = self.dbs[DBname]["Collections"][collect].find(query)
        if len(check) > 0 :
            self.dbs[DBname]["Collections"][collect].update_one(query)
            return True,str(len(check))
        else :
            return False,"Query Fail"