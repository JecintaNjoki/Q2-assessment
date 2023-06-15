#QUESTION1 
#INPUTS
#story length
#moral lessons
#age group
#OUTPUTS
#Story
#Story teller
#Translator 
#PROCESS
#create a class Storytelling with attributes
#story length,moral lessons,age group
#and these methods check_length,check_age_group,check_type,check_storytellers
class Storytelling:
 def __init__(self,storylength,morallessons,agegroup):
     self.storylength=storylength
     self.morallessons=morallessons
     self.agegroup=agegroup

def check_length(self,storylength):
 length=100
 if self.storylength <=100:
   return f"This story is {self.storylength} short"
 else:
   return f"This story is {self.storylength} "
   
      

def check_age_group(self,agegroup):
  if self.agegroup <=17:
    return f"This books are for minors aged{self.agegroup} "
  elif self.agegroup>=17:
    return f"This books are for adults{self.agegroup}"
  else:
    return f"this books are for everyone"


class Story:
  def __init__(self,type):
    self.type=type
   

class Storyteller:
  def __init__(self,storytellers) :
    self.storytellers
   

class Translator: 
  def __init__(self,translator):
    self.translator=translator
    

#QUESTION2  
# INPUTS
# ingredients
# preparation time
# cooking method
# nutritional information.

# OUTPUTS
# MoroccanRecipe
# EthiopianRecipe
# NigerianRecipe
# PROCESS
# create a class Africancuisine with attributes
#  ingredients,preparation_time,cooking_method,nutritional_information
#             

class Africancuisine:
  def __init__(self, ingredients,preparation_time,cooking_method,nutritional_information):
    self.ingrideents=ingredients
    self.preparation_time=preparation_time
    self.cooking_method=cooking_method
    self.nutritional_information=nutritional_information

    
  








#INPUTS 
# available_flight
# destination
# date
#OUTPUTS


class Flightbooking:
  def __init__(self,available_flight,destination,date):
    self.available_flights=available_flight
    self.destination=destination
    self.date=date

    # def seats_for_customers(self):
      

    # def manage_passenger_information():
        

    # def generate_booking_confirmations():    
      
class  Student:
  def __init__(self,name,age,grades):
    self.name=name
    self.age=age
    self.grades=grades

    def average_grade(self,grades):
      if self.grades >=60:
        return f"average grade"
      
      elif self.grades<=60:
        return f"below average"
      else:
        return f"above average"
    def student_information(self,name,age):
      return f"Student information is displayed"
    
    def student_pass(self,grades):
      if self.grades<60:
        return f"student has passed"
      else:
        return f"student has failed"
  

    

  




class Librarycatalog:
  def __init__(self,books,catalogging,management):
      self.books=books
      self.catalogging=catalogging
      self.management=management



  def add_new_books(self,books):
    newbooks=50
    if self.books > newbooks:
      return f"new {self.books} has been added"
    else:
      return f"no new{self.books} has been added" 



def search_for_book_by_title(self,title):
  return f"book title"
  

def search_for_book_by_author(self):
  return f"authors name"


# def keep_track_of_available_copies(self):

# def display_book_details():         


  

    






