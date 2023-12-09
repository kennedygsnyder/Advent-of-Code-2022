import re
class Monkey():
  def __init__(self, items, operation, test, throw_to):
    self.items = items
    self.operation = operation
    self.test = test
    self.throw_to = throw_to
    self.inspected_count = 0

  def inspect(self):
    throw_info = []
    while self.items:
      old = self.items.pop(0)
      self.inspected_count += 1
      new = eval(self.operation) // 3

      to_monkey = self.throw_to[0] if new % self.test == 0 else self.throw_to[1]
      throw_info.append([new, to_monkey])
      print(new,to_monkey)
    return throw_info

  def __repr__(self):
    return f'{str(self.items)}, {self.operation}, {self.test}, {self.throw_to}'

monkeys = []

with open('input.txt') as f:
  lines = f.readlines()
  
  while len(lines) > 0:
    lines.pop(0)

    starting_items = [int(x) for x in lines.pop(0).strip().split(":")[1].strip().split(', ')]
    operation = lines.pop(0).strip().split(":")[1].strip().split("= ")[1]

    test = int(re.search('\d+', lines.pop(0)).group())
    if_true = int(re.search('\d+', lines.pop(0)).group())
    if_false = int(re.search('\d+', lines.pop(0)).group())
    
    if len(lines) > 0:
      lines.pop(0)

    monkeys.append(Monkey(starting_items,operation,test,[if_true,if_false]))

for i in range(20):
  for monkey in monkeys:
    throw_info = monkey.inspect()
    for entry in throw_info:
      monkeys[entry[1]].items.append(entry[0])

monkey_counts = []
for i in range(len(monkeys)):
  print(f'Monkey {i}: {monkeys[i].inspected_count}')
  monkey_counts.append(monkeys[i].inspected_count)

monkey_counts.sort(reverse=True)
print(f'Monkey Business: {monkey_counts[0]*monkey_counts[1]}')