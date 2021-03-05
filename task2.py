def task2(nums):
  """
  TODO:
  
  Implement contains duplicate
  """
  return False
  

def test_task2():
  test_input = [1,2,3,1]
  result =  "task 2 success" if task2(test_input) == True else "task 2 failed"
  if "success" in result:
    print('Task 2 completed successfully!')
    f = open("test.result", "w")
    f.write(result)
    f.close()
  else:
    print("Task 2 failed! Try again.")

if __name__ == "__main__":
  test_task2()
