import check_cheapest_operator

prefix_dict = check_cheapest_operator.generate_dict('sample_price_lists copy.csv')
def no_prefix_match(self):
        self.assertAlmostEqual(check_cheapest_operator.select_operator('55332218', prefix_dict), None)
        self.assertAlmostEqual(check_cheapest_operator.select_operator('9195781990', prefix_dict), None)

def for_more_operators(self):
    self.assertAlmostEqual(check_cheapest_operator.select_operator('123', prefix_dict), {'operator': 'Operator A', 'price': 0.9})


def operator_maping(self):
    self.assertAlmostEqual(prefix_dict['7']['type']['6']['type']['2']['type']['0']['operator'], 'operator C')
