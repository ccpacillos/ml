def to_vectors(modifier, examples):
  return list(map(lambda x: modifier(x), examples))
