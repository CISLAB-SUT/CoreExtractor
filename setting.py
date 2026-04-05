TIMEOUT_VALUE = 120

# The list of tags that should be removed from the source code with their content
TAGE_TYPE_1 = ['head', 'script', 'style', 'button', 'label', 'dialog', 'fieldset', 'select', 'option',
               'input', 'svg']
# The list of tags that should be removed from the source code without their content
TAGE_TYPE_2 = ['u', 'strong', 'span', 'sup', 'sub', 'em', 'b', 'td', 'abbr', 'i', 'small', 'del', 'ins', 'ruby', 'kbd',
               'wbr', 'dfn', 'ins', 'U', 'STRONG', 'SPAN', 'SUP', 'SUB', 'EM', 'B', 'TD', 'ABBR', 'I', 'SMALL', 'DEL',
               'INS', 'RUBY', 'KBD', 'WBR', 'DFN', 'INS', 'cite', 'CITE', 'template', 'TEMPLATE']
# use for join to block
TAGE_TYPE_3 = ['ul', 'li', 'p', 'tr']

OPEN_A = '{{[#$a_tag'  # <a> replace with
CLOSE_A = ']}}#$a_tag'  # </a> replace with

CLIPPED_VALUES = {
    'b5': {'up': 230, 'down': 0},
    'b6': {'up': 13, 'down': 0},
    'b9': {'up': 1600, 'down': 0},
    'b13': {'up': 200, 'down': 0},
    'b24': {'up': 40, 'down': 0},
    'b34': {'up': 36000, 'down': 0},
    'b75': {'up': 43000, 'down': 0},
    'b95': {'up': 79000, 'down': 0}
}

BINARY_FEATURES = ['b1', 'b2', 'b3', 'b4', 'b7', 'b11', 'b14', 'b15', 'b16', 'b17', 'b18', 'b19', 'b23', 'b25', 'b28',
                   'b32', 'b36', 'b39', 'b40', 'b41', 'b42', 'b43', 'b44', 'b49', 'b50', 'b51', 'b52', 'b53', 'b54',
                   'b55', 'b56', 'b57', 'b58', 'b59', 'b60', 'b61', 'b62', 'b63', 'b64', 'b65', 'b66', 'b67', 'b68',
                   'b69', 'b73', 'b77', 'b80', 'b81', 'b82', 'b83', 'b84', 'b85', 'b97', 'b100', 'b101', 'b102', 'b103',
                   'b104', 'b105', 'b111','b112', 'b113', 'b114', 'b93', 'b110', 'b115', 'b116', 'b117', 'b118', 'b119',
                   'b120', 'b121', 'b122', 'b123', 'b124', 'b125', 'b126', 'b127', 'b128', 'b48', 'b131_0', 'b131_1',
                   'b131_2', 'b131_3', 'b132_0', 'b132_1', 'b132_2', 'b132_3']
# best features for next and previous blocks
N_P_FEATURES = ['b71', 'b75', 'b87', 'b30', 'b86', 'b130', 'b79', 'b88', 'b46', 'b137', 'b47', 'b70',
                            'b34', 'b45', 'b72', 'b9', 'b136', 'b29', 'b96', 'b106']
# best features for small blocks
SMALL_FEATURES = ['b71', 'b30', 'b87', 'b130', 'b137', 'b75', 'b86', 'b136', 'b72', 'b79', 'b31', 'b88',
                              'b34', 'b70', 'b47', 'b108', 'b46', 'b135', 'b45', 'b9', 'b96', 'b106', 'b29', 'b38',
                              'b107', 'b95', 'b74', 'b98', 'b90', 'b91', 'b118', 'b26', 'b27', 'b76', 'b6', 'b94',
                              'b127', 'b92', 'b99', 'b78', 'b35', 'b37', 'b13', 'b33', 'b3', 'b51', 'b22', 'b10', 'b5',
                              'b1', 'b20', 'b134', 'b12', 'b21', 'b85', 'b114', 'b53', 'b8', 'b24', 'b77', 'b36',
                              'b133', 'b104', 'b132_3', 'b102', 'b44', 'b56', 'b122', 'b112', 'b103']
# best features for big blocks
BIG_FEATURES = ['b71', 'b75', 'b87', 'b30', 'b86', 'b130', 'b79', 'b88', 'b46', 'b137', 'b47', 'b70', 'b34',
                            'b45', 'b72', 'b9', 'b136', 'b29', 'b96', 'b106', 'b135', 'b31', 'b118', 'b95', 'b5', 'b38',
                            'b74', 'b90', 'b108', 'b76', 'b98', 'b91', 'b107', 'b27', 'b26', 'b92', 'b94', 'b24', 'b22',
                            'b6', 'b99', 'b78', 'b35', 'b13', 'b112', 'b20', 'b33', 'b37', 'b21', 'b127', 'b1', 'b10',
                            'b3', 'b23', 'b51', 'b134', 'b8', 'b12', 'b85', 'b133', 'b25', 'b36', 'b77', 'b104', 'b53',
                            'b102', 'b132_0', 'b132_3', 'b44', 'b114']



# error coding for output
IGNORE_STATUS = 12
LEARNING_ERROR = 31
OK_STATUS = 10
FORMAT_ERROR = 25
TIMEOUT_ERROR = 48

SMALL_URL = "http://localhost:8501"
BIG_URL = "http://localhost:8502"