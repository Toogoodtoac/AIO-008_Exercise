def check(tp,fp,fn):
  if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
        if not isinstance(tp, int):
          print("tp must be an integer")
        if not isinstance(fp, int):
          print("fp must be an integer")
        if not isinstance(fn, int):
          print("fn must be an integer")
        return
  if tp <= 0 or fp <= 0 or fn <= 0:
      print('tp and fp and fn must be greater than zero')
      return
  precision = tp / (tp + fp)
  recall = tp / (tp + fn)
  f1_score = 2 * (precision * recall) / (precision + recall)
  print(f'Precision: {precision}')
  print(f'Recall: {recall}')
  print(f'F1-score: {f1_score}')
if __name__=="__main__":
  tp=int(input("Enter tp: "))
  fp=int(input("Enter fp: "))
  fn=int(input("Enter fn: "))
  check(tp,fp,fn)