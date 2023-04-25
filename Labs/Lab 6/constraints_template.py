from random import shuffle


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment) == True:
            return assignment
        
        # Select unassigned variable
        variable = self.select_unassigned_variable(assignment)

        # for each value loop
        for value in self.order_domain_values(variable, assignment):
            if self.is_consistent(variable, value, assignment) == True:
                assignment[variable] = value
                result = self.recursive_backtracking(assignment)
                if result != None:
                    return result
                assignment.pop(variable)
        return None
                

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_australia_csp():
    wa, q, t, v, sa, nt, nsw = 'WA', 'Q', 'T', 'V', 'SA', 'NT', 'NSW'
    values = ['Red', 'Green', 'Blue']
    variables = [wa, q, t, v, sa, nt, nsw]
    domains = {
        wa: values[:],
        q: values[:],
        t: values[:],
        v: values[:],
        sa: values[:],
        nt: values[:],
        nsw: values[:],
    }
    neighbours = {
        wa: [sa, nt],
        q: [sa, nt, nsw],
        t: [],
        v: [sa, nsw],
        sa: [wa, nt, q, nsw, v],
        nt: [sa, wa, q],
        nsw: [sa, q, v],
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        wa: constraint_function,
        q: constraint_function,
        t: constraint_function,
        v: constraint_function,
        sa: constraint_function,
        nt: constraint_function,
        nsw: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)

def create_south_america_csp():
    cosric, pan, col, ven, guy, sur, guyfr, ecu, per, bra, bol, chi, arg, par, uru = 'CosRic', 'Pan', 'Col', 'Ven', 'Guy', 'Sur', 'GuyFR', 'Ecu', 'Per', 'Bra', 'Bol', 'Chi', 'Arg', 'Par', 'Uru'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [cosric, pan, col, ven, guy, sur, guyfr, ecu, per, bra, bol, chi, arg, par, uru]
    domains = {
        cosric: values[:],
        pan: values[:],
        col: values[:],
        ven: values[:],
        guy: values[:],
        sur: values[:],
        guyfr: values[:],
        ecu: values[:],
        per: values[:],
        bra: values[:],
        bol: values[:],
        chi: values[:],
        arg: values[:],
        par: values[:],
        uru: values[:],
    }
    neighbours = {
        cosric: [pan],
        pan: [cosric, col],
        col: [pan, ven, bra, ecu, per],
        ven: [col, guy, bra],
        guy: [ven, sur, bra],
        sur: [guy, guyfr, bra],
        guyfr: [sur, bra],
        ecu: [col, per],
        per: [ecu, bra, bol, chi, col],
        bra: [guyfr, sur, guy, ven, col, per, bol, par, arg, uru],
        bol: [per, bra, par, arg, chi],
        chi: [per, bol, arg],
        arg: [chi, bol, par, bra, uru],
        par: [bol, bra, arg],
        uru: [arg, bra],
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        cosric: constraint_function,
        pan: constraint_function,
        col: constraint_function,
        ven: constraint_function,
        guy: constraint_function,
        sur: constraint_function,
        guyfr: constraint_function,
        ecu: constraint_function,
        per: constraint_function,
        bra: constraint_function,
        bol: constraint_function,
        chi: constraint_function,
        arg: constraint_function,
        par: constraint_function,
        uru: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)

if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    if type(result) == dict:
        for area, color in sorted(result.items()):
            print("{}: {}".format(area, color))
    else:
        print("Failed to map Australia")

    print("*******************")

    south_america = create_south_america_csp()
    result = south_america.backtracking_search()
    if type(result) == dict:
        for area, color in sorted(result.items()):
            print("{}: {}".format(area, color))
    else:
        print("Failed to map South America")

    # Check at https://mapchart.net/australia.html
