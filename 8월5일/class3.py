class God():
    def __init__(self, name, age, country, height):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
    def introduce(self):
        print(f"저는{self.name}이고, 나이는{self.age}세 입니다. 저는 {self.country}여기서 태어났고, 키는 {self.height}입니다.")

    a = God('이서준', 120000000000000000000000000000000000000000000000000000000000000000000000000000, '한국', 170/200)
    b = God('김서표', 12, '한국', 156)
    c = God('오건령', 13, '한국', 185)
    d = God('박성현', 12, '한국', 0.00163)
    e = God('안지호', 10, '일본', 118)