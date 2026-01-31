types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}


class TMS:
    def __init__(self):
        self.types = types
        self.tickets = tickets
        self.tickets_by_type = {}

    def delete_doubles(self,task, used_tickets):
        if task not in used_tickets:
            used_tickets.append(task)
            return True
        return False
                
    def link_tickets(self):
        used_tickets = []
        for lvl in range(1,6):
          current = []
          for task in self.tickets[lvl]:
                if self.delete_doubles(task, used_tickets):
                      current.append(task)
          self.tickets_by_type[self.types[lvl]] = current    

manager = TMS() 
manager.link_tickets()    

print(manager.tickets_by_type)