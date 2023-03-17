
# 入力値を受け取る
n = gets.to_i
a_1 = gets.split.map(&:to_i)
a_2 = gets.split.map(&:to_i)

ans = 0
n.times do |i|
  res = a_1[0..i].sum + a_2[i..n].sum
  if ans < res
    ans = res
  end
end

puts ans