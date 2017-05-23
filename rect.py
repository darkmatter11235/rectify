class Point(object):
	def __init__(self, x, y)
		self.x, self.y = x, y
	
	@staticmethod
	def from_point(other):
		return Point(other.x, other.y)

class Rect(object):
	def __init__(self, x1, y1, x2, y2):
		xl, xh = (x1,x2) if x1 < x2 else (x2,x1)
		yl, yh = (y1,y2) if y1 < y2 else (y2,y1)
		self.min, self.max = Point(xl, yl), Point(xh, yh)
	@staticmethod
	def from_points(p1,p2)
		return Rect(p1.xl, p1.yl, p2.xl, p2.yl)
