##UNIVERSIDAD DEL VALLE DE GUATEMALA 
## BASE DE DATOS 
## JORGE YASS
## FATIMA PRISCILLA GONZALEZ 20689
## SAYRA ESTEFANIA ELVIRA 20725



##CREACION DE UNA CLASE PARA DESARRROLLAR UN OBJETO QUE LEA EL ARCHIVO CSV E INSERTE LOS DATOS EN EL POSGRES
class insert_in_datos:
    def load_excel(self):
        import csv 
        self.archivo = open (r"Team.csv")
        self.filas = csv.reader (self.archivo, delimiter= ",")
        self.lista = list(self.filas)
        del ( self.lista[0])
        self.tuplaa = tuple (self.lista)
        for rw in self.tuplaa:
            print (rw)
    
    def insert_draft(self):
        import psycopg2
        self.connection = psycopg2.connect(dbname ="proyecto1-datos", user = "postgres", password ="3369")
        self.cursor = self.connection.cursor()
        self.cursor.executemany("insert into Draft (yearDraft,numberPickOverall,numberRound,numberRoundPick,namePlayer,slugTeam,nameOrganizationFrom,typeOrganizationFrom,idPlayer,idTeam,nameTeam,cityTeam,teamName,PLAYER_PROFILE_FLAG,slugOrganizationTypeFrom,locationOrganizationFrom) values(%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s)", self.tuplaa)
        self.connection.commit ()
        self.connection.close()


    def insert_draftCombine(self):
        import psycopg2
        self.connection = psycopg2.connect(dbname ="proyecto1-datos", user = "postgres", password ="3369")
        self.cursor = self.connection.cursor()
        self.cursor.executemany("insert into Team (id,	full_name,   	abbreviation,	nickname,    	city,        	state,       	year_founded) values(%s,	%s,	%s,	%s,	%s,	%s,	%s)", self.tuplaa)
        self.connection.commit ()
        self.connection.close()


ins_db = insert_in_datos()
ins_db.load_excel()
##ins_db.insert_draft()
ins_db.insert_draftCombine()
