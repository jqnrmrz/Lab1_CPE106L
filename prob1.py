def median(numbers):
  numbers.sort()
  if len(numbers) % 2 == 0:
    # The list has an even number of elements, so the median is the average of the two middle elements.
    median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
  else:
    # The list has an odd number of elements, so the median is the middle element.
    median = numbers[len(numbers) // 2]
  return median

def mode(numbers):
  # Create a dictionary to store the number of times each number appears in the list.
  number_counts = {}
  for number in numbers:
    if number in number_counts:
      number_counts[number] += 1
    else:
      number_counts[number] = 1

  # The mode is the number that appears the most times.
  mode = None
  max_count = 0
  for number, count in number_counts.items():
    if count > max_count:
      mode = number
      max_count = count

  return mode
