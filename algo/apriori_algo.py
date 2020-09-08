from algo.ultils import calculate_sup, build_new_list_candidate


class AprioriAlgo:
    minsup = 0
    n = 0
    db = []
    list_recent_candidate = []
    list_recent_sup = []
    list_first_candidate = []
    list_two_factor = []
    list_res_candidate = []

    def build_first_candidate(self):
        set_element = set()
        for record in self.db:
            for item in record:
                set_element.add(item)
        for item in set_element:
            self.list_first_candidate.append([item])
            self.list_recent_candidate.append([item])

    def calculate_recent_sup(self):
        self.list_recent_sup = []
        for candidate in self.list_recent_candidate:
            self.list_recent_sup.append(calculate_sup(candidate, self.db))

    def apriori_algo(self):
        self.build_first_candidate()

        while True:
            self.calculate_recent_sup()
            list_recent_res_candidate = []
            print(self.list_recent_sup)

            for i in range(len(self.list_recent_sup)):
                if float(self.list_recent_sup[i]) / self.n >= self.minsup:
                    list_recent_res_candidate.append(self.list_recent_candidate[i])

            if len(list_recent_res_candidate) > 0:
                self.list_res_candidate = list_recent_res_candidate
            else:
                break

            print(self.list_res_candidate)

            self.list_recent_candidate = build_new_list_candidate(list_recent_res_candidate, self.list_first_candidate)

    def __init__(self, db, minsup):
        self.db = db
        self.n = len(db)
        self.minsup = minsup
        self.apriori_algo()
