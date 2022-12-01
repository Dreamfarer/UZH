class Order:
    def __init__(self, item_list):
        self.__item_list = self.__get_item_list(item_list)
        self.__bill_amount = self.__calculate_bill_amount(item_list)

    def __get_item_list(self, item_list):
        dict = {}
        for item in item_list:
            try:
                dict[item] += 1
            except KeyError:
                dict[item] = 1
        return dict

    def get_bill_amount(self):
        return self.__bill_amount

    def __calculate_bill_amount(self, item_list):
        bill_amount = 0
        for item in item_list:
            bill_amount = item.get_item_price() + bill_amount
        return bill_amount

    def __repr__(self):
        return "Order Items : {}, Order Bill Amount : {} ".format(self.__item_list, self.__bill_amount)
