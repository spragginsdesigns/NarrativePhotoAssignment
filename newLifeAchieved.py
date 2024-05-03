class Life:
    def __init__(self, constraints):
        self.constraints = constraints
        self.freedom = False
        self.faith = 0

    def break_free(self):
        if self.constraints == "prison":
            self.freedom = True
            print("Freedom from constraints achieved!")

    def embrace_faith(self):
        if self.freedom:
            self.faith += 100
            print("Faith embraced: Now living a life guided by Christian values.")

    def new_beginnings(self):
        if self.faith == 100:
            print("New life rebuilt with purpose and hope.")
            print("Enjoy Your New Life")  # Added print statement


# Create a Life object with 'prison' as the constraint
my_life = Life('prison')

# Call the break_free method
my_life.break_free()

# Call the embrace_faith method
my_life.embrace_faith()

# Call the new_beginnings method
my_life.new_beginnings()