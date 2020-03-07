class BeanObject:
    id = ''
    name = ''
    street = ''
    city = ''
    zip = ''
    state = ''

    # Multiple field available (more than 100 field)
    # --------
    # --------
    def __init__(self,id,name,street,city,zip,state):
        print("This is non parametrized constructor")
        self.id=id
        self.name=name
        self.street=street
        self.city=city
        self.zip=zip
        self.state=state
        # --------
        # --------
