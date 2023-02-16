from collections import Counter


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({
            "customer": customer,
            "order": order,
            "day": day
              })

    def get_most_ordered_dish_per_customer(self, customer):
        list = []
        for order in self.orders:
            list.append(order["order"])
        return max(Counter(list).most_common(), key=self.orders.count)[0]

    def get_never_ordered_per_customer(self, customer):
        list = []
        new = []
        for order in self.orders:
            list.append(order["order"])
        for item in [day for day in list]:
            info = Counter(list).most_common()
            if item != max(info, key=self.orders.count)[0]:
                new.append(item)
        return Counter(new).keys()

    def get_days_never_visited_per_customer(self, customer):
        list = []
        new = []
        for order in self.orders:
            list.append(order["day"])
        for item in [day for day in list]:
            if item != max(Counter(list), key=self.orders.count):
                new.append(item)
        return Counter(new).keys()

    def get_busiest_day(self):
        list = []
        for order in self.orders:
            list.append(order["day"])
        return [result for result in Counter(list).keys()][0]

    def get_least_busy_day(self):
        list = []
        for order in self.orders:
            list.append(order["day"])
        return [result for result in Counter(list).keys()][-1]
