def linear_search_product(productlist, tar):
  indices=[]
  for index, product in enumerate(productlist):
    if product==tar:
      indices.append(index)

  return indices

product=["football","volleyball","beachball","volleyball","basketball","Dodgeball"]
target="volleyball"
result=linear_search_product(product,target)
print(result)