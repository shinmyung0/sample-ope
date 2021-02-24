

def task1(n):
  """
  Implement fibonacci
  """
  # if n == 1:
  #   return 1
  # elif n == 2:
  #   return 2
  # return task1(n-1) + task1(n-2)
  return 0



def test_task1():
  result =  "task 1 success" if task1(4) == 5 else "task 1 failed"
  if "success" in result:
    print('Task 1 completed successfully!')
    f = open("test.result", "w")
    f.write(result)
    f.close()
  else:
    print("Task 1 failed! Try again.")

if __name__ == "__main__":
  test_task1()
