#Clase para calcular la regresion sin usar ningun modulo adicional
import math
class regresion():

    def __init__(self, x, y):
        #x =  [12,30,15,24,14,18,28,26,19,27]
        #y =  [20,60,27,50,21,30,61,54,32,57]
        self.x = x
        self.y = y
        sumx = 0
        sumy = 0
        sumxy = 0
        sumxx = 0
        for i in range(0, len(self.x)):
            sumx = sumx + self.x[i]
            sumy = sumy + self.y[i]
            sumxy = sumxy + (self.x[i] * self.y[i])
            sumxx = sumxx + (self.x[i] * self.x[i])

        self.b0 = (len(self.x) * (sumxy) - (sumx) * (sumy)) / (len(self.x) * sumxx - (sumx*sumx) )
        self.b1 = (sumy - (self.b0) * sumx) / len(self.x)



    def Predict(self, val):
        y = self.b0 * val + self.b1
        return y

    def PredictN(self, vals):
        resultado =  list()
        for i in vals:
            resultado.append(self.b0 * i + self.b1)
        return resultado

    def r2(self):
        sumx = 0
        sumy = 0
        sumx_med = 0.0
        sumy_med = 0.0
        total_med = 0.0
        for i in range(0, len(self.x)):
            sumx = sumx + self.x[i]
            sumy = sumy + self.y[i]
        x2 = sumx / len(self.x)
        y2 = sumy / len(self.x)
        for i in range(0, len(self.x)):
            sumx_med = sumx_med + (self.x[i] - x2) * (self.x[i] - x2)
            sumy_med = sumy_med + (self.y[i] - x2) * (self.y[i] - x2)
            total_med = total_med + sumx_med + sumy_med
        coeficiente = total_med / (math.sqrt(sumx_med)) * (math.sqrt(sumy_med))
        return coeficiente

    def r(self):
        sumx = 0
        sumy = 0
        sumx_med = 0
        sumy_med = 0
        total_med = 0
        for i in range(0, len(self.x)):
            sumx = sumx + self.x[i]
            sumy = sumy + self.y[i]
        x2 = sumx / len(self.x)
        y2 = sumy / len(self.x)
        for i in range(0, len(self.x)):
            sumx_med = sumx_med + (self.x[i] - x2) * (self.x[i] - x2)
            sumy_med = sumy_med + (self.y[i] - x2) * (self.x[i] - x2)
            total_med = total_med + sumx_med + sumy_med
        coeficiente = total_med / (math.sqrt(sumx_med)) * (math.sqrt(sumy_med))
        coeficiente = math.sqrt(coeficiente)
        return coeficiente

    def getAllRefParams(self):
        coer2 = self.r2()
        coer = self.r()
        resultado = {'b0': self.b0, 'b1': self.b1, 'r2':coer2, 'r': coer}
        return resultado

    @classmethod
    def from_file_name(cls, path):
        x = list()
        y = list()
        file = open(path, 'rb')
        a = file.readlines()
        t = []
        for f in a:
            f = str(f).replace('\\r\\n', '')
            f = f.replace("b'", '')
            f = f.replace("'", '')
            e = f.split(",")
            x.append(int(e[0]))
            y.append(int(e[1]))
        file.close()
        return cls(x, y)

x =  [12,30,15,24,14,18,28,26,19,27]
y =  [20,60,27,50,21,30,61,54,32,57]
pred = [5,3,5]
testClase1 = regresion(x, y)
print(testClase1.Predict(10))
print(testClase1.PredictN(pred))
print(testClase1.r2())
print(testClase1.r())
print(testClase1.getAllRefParams())

testClase2 = regresion.from_file_name("datos_input.csv")
print(testClase2.Predict(10))
print(testClase2.PredictN(pred))
print(testClase2.r2())
print(testClase2.r())
print(testClase2.getAllRefParams())