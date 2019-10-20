import numpy, datetime, math

"""
    maxBall maximo de bolitas en el sorteo 
    ballSelect bolitas que se seleccionan en el sorteo
    winnerSing numero de asiertos 
    sell boletos vendidos 
    totalTicket total de boletos impresos
    allWinnerProb Todas las cobinacionaes que hay para ser un ganador de la loteria
    allTicketGenerators  Numero total de ticket generados
    allTicketSeller Numero total de ticket vendidos
"""
class Lottery:
    __ONE = 1
    __num = __ONE
    allWinnerProb = []
    allTicketGenerators = []
    allTicketSeller = []

    def __init__(self, maxBall, ballSelect, winnerSing, sell, totalTicket):
        self.maxBall = maxBall
        self.ballSelect = ballSelect
        self.winnerSing = winnerSing
        self.sell = sell
        self.totalTicket = totalTicket
        self.__ball = range(self.__ONE, self.maxBall)
        self.__ball_imt_all = tuple(self.__ball)

    def run(self):
        tickets = self.ticketGenerator()
        sellers = self.sellerTicket()
        winPeople = self.winRaffle()
        for sell in sellers:
            print(sell, " bool:", sell in tickets)
        print(winPeople in sellers)
        return

    def sellerTicket(self):
        x = tuple(self.allTicketGenerators)
        while True:
            if len(self.allTicketSeller) == self.sell:
                break
            numberRandom = numpy.random.randint(len(x))
            val = x[numberRandom]
            if val not in self.allTicketSeller:
                self.allTicketSeller.append(val)
            else:
                continue
        return self.allTicketSeller

    """calcula todas las combinaciones posibles de boletos, cuidado el numero de combinaciones suele pasar 
     el MILLON de resultados"""

    def allCombiner(self):
        test = self.combinacion(self.maxBall, self.winnerSing)
        timeInit = datetime.datetime.now()
        while True:
            x = tuple(self.winnerRandom())
            if len(self.allWinnerProb) == test:
                break
            if x not in self.allWinnerProb:
                self.allWinnerProb.append(x)
                self.__num += 1
            else:
                continue
        timeEnd = datetime.datetime.now()
        print("proseso duro ", timeEnd - timeInit, "iteraxciones:", self.__num)
        return "listo"

    # simula el sorteo
    def selectRandom(self):
        select_array = []
        while True:
            numberRandom = numpy.random.randint(len(self.__ball_imt_all))
            val = self.__ball_imt_all[numberRandom]
            if val in select_array:
                continue
            else:
                select_array.append(val)
            if len(select_array) == self.ballSelect:
                break
            else:
                self.__num += self.__ONE
        return select_array
    #Ganador del sorteo
    def winRaffle(self):
        x = self.selectRandom()
        return x[0:self.winnerSing]

    # test que simula boleto ganador
    def winnerSelect(self):
        winnerSelect_array: []
        while True:
            numberRandom = numpy.random.randint(len(self.__ball_imt_all))
            val = self.__ball_imt_all[numberRandom]
            if val in winnerSelect_array:
                continue
            else:
                winnerSelect_array.append(val)
            if len(winnerSelect_array) == self.winnerSing:
                break
            else:
                continue
        return winnerSelect_array

    # Esta Funsion genera los boletos
    def ticketGenerator(self):
        tickets = []
        for i in range(self.totalTicket):
            ticketGenerator_array = []
            while True:
                numberRandom = numpy.random.randint(len(self.__ball_imt_all))
                val = self.__ball_imt_all[numberRandom]
                if val in ticketGenerator_array:
                    continue
                else:
                    ticketGenerator_array.append(val)
                if len(ticketGenerator_array) == self.winnerSing:
                    break
                else:
                    continue
            tickets.append(ticketGenerator_array)
        self.allTicketGenerators = tickets
        return self.allTicketGenerators

    def combinacion(self, n, r):
        n_fact = math.factorial(n)
        r_fact = math.factorial(r)
        rn = n - r
        rn_fact = math.factorial(rn)
        res = n_fact / (r_fact * rn_fact)
        return res

    def combTotalCurrent(self):
        n_fact = math.factorial(self.maxBall)
        r_fact = math.factorial(self.winnerSing)
        rn = self.maxBall - self.winnerSing
        rn_fact = math.factorial(rn)
        res = n_fact / (r_fact * rn_fact)
        return res

x = Lottery(25, 15, 15, 500, 1000)
print(x.combTotalCurrent())
