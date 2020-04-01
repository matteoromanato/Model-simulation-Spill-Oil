from mesa import Agent

class Oil(Agent):
   
    def __init__(self,pos,model,qnt,qnt_prop):

        super().__init__(pos,model)
        self.pos = pos
        self.qnt = qnt                      # il petrolio avrà una certa quantità in una casella 
        self.qnt_prop = qnt_prop            # quantà quantità si sposta da una casella ad una adiacente in percentuale da 0 a 1
        self.type = 0 

    def step(self):
        # causa dele correnti il petrolio si sposta non rimane fermo
        possible_steps = self.model.grid.get_neighborhood(self.pos,moore=True,include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
 
        #oltre a spostarsi il petrolio si sparge coprendo un'area maggiore
        if (self.qnt*self.qnt_prop/100) >= 1:
            print("la nuova casella porta una quantità di petrolio di " + str(self.qnt*self.qnt_prop/100))

            possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
            new_position = self.random.choice(possible_steps)
            macchia = Oil(new_position, self.model, (self.qnt*self.qnt_prop/100), self.qnt_prop)
            self.qnt = self.qnt - (self.qnt*self.qnt_prop/100)
            self.model.grid.place_agent(macchia, new_position)
            self.model.schedule.add(macchia)



class Boat(Agent):

    def __init__(self,pos,model,power):

        super().__init__(pos,model)
        self.pos = pos
        self.power = power                      # power indica quanta qnt di petrolio riescono a smaltire ad ogni step
        self.type = 1

    def step(self):
       # se trova petrolio lo toglie finchè non libera la casella
       # se non trova petrolio si muove
        for neighbor in self.model.grid.neighbor_iter(self.pos):
            if neighbor.type == 0:
                neighbor.qnt = (neighbor.qnt)-self.power
                if(neighbor.qnt < 0):
                    self.model.grid._remove_agent(neighbor.pos, neighbor)
                    self.model.schedule.remove(neighbor)

  #     cellmates = self.model.grid.neighbor_iter(self.pos, moore=True)
  #     if len(cellmates) > 1:
  #         other = self.random.choice(cellmates)
  #         if(other.type == 0):
  #             other.qnt = (other.qnt)-power
  #             if(other.qnt < 0):
  #                 self.model.grid._remove_agent(other.pos, other)
  #                 self.model.schedule.remove(other)
        
        possible_steps = self.model.grid.get_neighborhood(self.pos,moore=True,include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

       
       

       

