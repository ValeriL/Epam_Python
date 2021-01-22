from homework11.task2 import Order


def test_order_class():
    def morning_discount(order):
        return order.price - order.price * 0.5

    def elder_discount(order):
        return order.price - order.price * 0.9

    order_1 = Order(100, morning_discount)
    order_2 = Order(100, elder_discount)
    order_3 = Order(100)

    assert order_1.final_price() == 50
    assert order_2.final_price() == 10
    assert order_3.final_price() == 100
