class Vector
  @val : Array(Int32) 
  def initialize(@val : Array)
  end
end

v1 = Vector.new [1, 2, 3]

puts v1.@val
