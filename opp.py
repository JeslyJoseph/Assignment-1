class Movie(object):
     attr = "lang" #attribute

     def __init__(self,actor,year):
        self.actor= actor
        self.year=year

     def details(self):
        #print('My name is  {}\t'.format(self.name))
        print("and releasing year is {}".format(self.year))

class Romantic(Movie):

    def details(self):
        print("and {} is the famous movie in {}".format(self.actor,self.year)) #polymorphishm
        

class Director(Movie):  #inheritance
    def __init__(self, actor, year,music):
        self.music = music

        Movie.__init__(self,actor,year)

    def identify(self):
        print("{} is the Director of {}".format(self.actor,self.music))


#obj instant

a=Director("Rajamouli",2022,"RRR")
a.identify()
a.details()

b=Romantic("KGF",2022)
b.details()
