# pythonでの実装だとheapqを使っていましたが、Rubyだと自作で私自身でheapqは作れないため、TLEですがこちらで提出させていただきます。
# 入力値の受け取り
n,m = gets.split(" ").map(&:to_i)
a = gets.split.map(&:to_i)

def cal(num)
  tmp = num / 2
  return tmp
end

m.times do |i|
  a = a.sort
  res = cal(a[-1])
  a[-1] = res
end

p a.sum