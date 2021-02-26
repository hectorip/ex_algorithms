examples = [
  {[0,1,0,2,1,0,1,3,2,1,2,1], 6},
  {[4,2,0,3,2,5], 9}
]
# [0 | [...]]

trapped_water = fn heigths ->
  for h <- heigths do
    IO.puts(h)
  end
end

examples
|> Enum.map(
  fn {heights, result} ->
    IO.puts("Prueba #{heights}: #{trapped_water.(heights)} == #{result}")
end)
