import json

# this.Unistrokes[0] = new Unistroke("triangle", new Array(new Point(137,139),new Point(135,141),new Point(133,144),new Point(132,146),new Point(130,149),new Point(128,151),new Point(126,155),new Point(123,160),new Point(120,166),new Point(116,171),new Point(112,177),new Point(107,183),new Point(102,188),new Point(100,191),new Point(95,195),new Point(90,199),new Point(86,203),new Point(82,206),new Point(80,209),new Point(75,213),new Point(73,213),new Point(70,216),new Point(67,219),new Point(64,221),new Point(61,223),new Point(60,225),new Point(62,226),new Point(65,225),new Point(67,226),new Point(74,226),new Point(77,227),new Point(85,229),new Point(91,230),new Point(99,231),new Point(108,232),new Point(116,233),new Point(125,233),new Point(134,234),new Point(145,233),new Point(153,232),new Point(160,233),new Point(170,234),new Point(177,235),new Point(179,236),new Point(186,237),new Point(193,238),new Point(198,239),new Point(200,237),new Point(202,239),new Point(204,238),new Point(206,234),new Point(205,230),new Point(202,222),new Point(197,216),new Point(192,207),new Point(186,198),new Point(179,189),new Point(174,183),new Point(170,178),new Point(164,171),new Point(161,168),new Point(154,160),new Point(148,155),new Point(143,150),new Point(138,148),new Point(136,148)));

# for nums in range(0, 10):
#     with open(f"./{nums}.json") as f:
#         num = json.load(f)
#         print(f'this.Unistrokes[{nums}] = ', end='')
#         print('new Unistroke(', end='')
#         print(f"\"{nums}\", ", end='')
#         print('new Array(', end='')


#         for i in range(len(num['Points'])):
#             p = num['Points'][i]
#             print(f"new Point({"%.2f" % p['X']},{"%.2f" % p['Y']})", end='')
#             if i != len(num['Points']) - 1:
#                 print(",", end='')
#         print("))")
        
for i in range(10):
    print(f'<option value="{i}">{i}</option>')