from math import log
from time import time

#[(Vgs, Vds, Tj, Fmax)]
data = [(4.99, 0.456, 297.74, 3.936),
(4.99, 0.544, 298.14, 3.773),
(4.99, 0.56, 297.88, 3.691),
(4.99, 0.592, 298.16, 3.615),
(4.99, 0.608, 298.16, 3.595),
(4.99, 0.688, 298.73, 3.102),
(4.99, 0.728, 298.02, 2.981),
(4.99, 0.825, 298.3, 2.839),
(4.99, 0.976, 298.93, 2.739),
(4.99, 1.152, 298.63, 2.583),
(4.99, 1.362, 299.77, 2.441),
(4.99, 1.583, 299.33, 2.346),
(4.99, 1.847, 300.64, 2.18),
(4.99, 2.064, 301.06, 2.173),
(4.99, 2.285, 302.41, 2.131),
(4.99, 2.54, 302.83, 2.142),
(4.99, 2.864, 304.12, 2.128),
(4.99, 3.16, 305.03, 2.1),
(4.99, 3.683, 307.47, 1.999),
(4.99, 4.12, 309.46, 1.885),
(4.99, 4.686, 311.8, 1.817),
(4.99, 5.249, 316.63, 1.761),
(4.99, 5.764, 320.57, 1.711),
(4.99, 6.283, 326.1, 1.623),
(4.99, 4.05, 316.78, 2.035),
(4.99, 4.08, 321.4, 2.005),
(4.99, 4.08, 327.2, 2.069),
(4.99, 4.08, 324.12, 2.041),
(4.99, 4.06, 329.44, 2.078),
(4.99, 4.04, 333.94, 2.133),
(4.99, 4.04, 337.53, 2.094),
(4.99, 4.03, 341.87, 2.146),
(4.99, 4.02, 345.13, 2.184),
(4.99, 4.03, 348.29, 2.189),
(4.99, 4.02, 350.45, 2.199),
(4.99, 4, 354.15, 2.217),
(4.99, 6.066, 364.25, 2.023),
(4.99, 1.921, 346.28, 2.641),
(4.99, 0.679, 341.63, 3.321),
(4.99, 0.418, 341.11, 3.948),
(4.99, 3.234, 348.08, 2.357),
(4.99, 4.028, 345.34, 2.156),
(4.99, 1.478, 336.31, 2.767),
(4.99, 0.454, 330.08, 3.824),
(4.99, 5.602, 347.14, 1.973),
(4.99, 6.143, 347.58, 1.929),
(4.99, 4.025, 339.62, 2.181),
(4.99, 2.422, 330.85, 2.422),
(4.99, 1.499, 326.4, 2.709),
(4.99, 0.709, 323.06, 3.264),
(4.99, 0.598, 320.71, 3.497),
(4.99, 0.487, 320.38, 3.718),
(4.99, 4.085, 330.71, 1.999),
(4.99, 5.126, 334.79, 1.889),
(4.99, 6.265, 338.7, 1.695),
(4.99, 1.514, 317.97, 2.636),
(3.875, 1.877, 314.1, 1.103),
(3.875, 0.592, 311.85, 1.649),
(3.875, 0.732, 310.82, 1.466),
(3.875, 0.89, 310.52, 1.336),
(3.875, 3.029, 312.81, 0.984),
(3.875, 4.457, 314.47, 0.892),
(3.875, 6.571, 323.46, 0.807),
(3.875, 0.574, 326.43, 1.762),
(3.875, 0.705, 327.65, 1.566),
(3.875, 0.871, 327.45, 1.42),
(3.875, 3.035, 331.88, 0.967),
(3.875, 4.725, 336.29, 0.923),
(3.875, 6.799, 342.36, 0.831),
(3.875, 0.554, 340.56, 1.885),
(3.875, 0.687, 338.2, 1.635),
(3.875, 0.842, 337.64, 1.485),
(3.875, 1.776, 341.42, 1.232),
(3.875, 2.872, 340.83, 1.156),
(3.875, 4.812, 347.95, 1.004),
(3.875, 5.799, 347.55, 0.899),
(3.875, 6.763, 351.51, 0.792),
(3.875, 3.756, 308.54, 0.534),
(3.674, 3.952, 310.37, 0.199),
(4.156, 4.749, 309.99, 0.959),
(4.396, 4.281, 311.19, 1.289),
(4.63, 4.223, 312.91, 1.514),
(4.91, 4.126, 314.46, 1.808),
(5.07, 4.049, 315.26, 2.118),
(4.67, 1.64, 299.61, 1.821),
(4.67, 1.2, 299.05, 1.994),
(4.67, 0.84, 296.98, 2.3),
(4.67, 0.712, 296.91, 2.44),
(4.67, 2.16, 303, 1.567),
(4.67, 2.72, 305.33, 1.497),
(4.67, 3.24, 308.84, 1.427),
(4.67, 3.76, 310.49, 1.38),
(4.67, 4.44, 313.88, 1.285),
(4.67, 0.664, 297.7, 2.498),
(4.67, 0.648, 298.91, 2.56),
(4.67, 0.616, 299.17, 2.6),
(4.67, 0.608, 298.87, 2.637),
(4.67, 0.584, 299.05, 2.715),
(4.67, 0.608, 304.03, 2.6),
(4.67, 0.632, 304.43, 2.6),
(4.67, 0.728, 307.36, 2.45),
(4.67, 0.872, 307.74, 2.18),
(4.67, 1.22, 308.32, 1.956),
(4.67, 1.655, 310.27, 1.769),
(4.67, 2.18, 311.08, 1.512),
(4.67, 2.72, 313.07, 1.427),
(4.67, 3.24, 316.53, 1.453),
(4.67, 3.76, 317.54, 1.434),
(4.67, 4.4, 320.16, 1.34),
(4.67, 0.592, 318.04, 2.735),
(4.67, 0.6, 318.88, 2.693),
(4.67, 0.616, 319.48, 2.6),
(4.67, 0.656, 320.15, 2.56),
(4.67, 0.704, 320.66, 2.45),
(4.67, 0.84, 320.85, 2.21),
(4.67, 1.2, 321.53, 2.01),
(4.67, 1.64, 322.79, 1.819),
(4.67, 2.154, 324.38, 1.625),
(4.67, 2.661, 325.47, 1.581),
(4.67, 3.163, 327.87, 1.606),
(4.67, 3.732, 329.4, 1.457),
(4.67, 4.326, 332.74, 1.41),
(4.67, 0.56, 325.13, 2.877),
(4.67, 0.584, 326.94, 2.85),
(4.67, 0.6, 327.86, 2.77),
(4.67, 0.64, 327.44, 2.683),
(4.67, 0.68, 327.56, 2.58),
(4.67, 0.824, 329.31, 2.29),
(4.67, 1.016, 327.88, 2.015),
(4.67, 1.187, 328.4, 1.967),
(4.67, 1.652, 329.41, 1.772),
(4.67, 2.138, 330.21, 1.696),
(4.67, 2.656, 332.39, 1.6),
(4.67, 3.21, 334.24, 1.536),
(4.67, 3.755, 335.59, 1.484),
(4.67, 4.397, 337.79, 1.358),
(4.67, 0.536, 340.12, 2.996),
(4.67, 0.568, 336.67, 2.864),
(4.67, 0.576, 336.03, 2.84),
(4.67, 0.616, 335.65, 2.74),
(4.67, 0.672, 335.7, 2.638),
(4.67, 0.816, 335.5, 2.334),
(4.67, 0.984, 335.94, 2.226),
(4.67, 1.187, 336.22, 2.046),
(4.67, 1.6167, 336.55, 1.957),
(4.67, 2.102, 336.3, 1.822),
(4.67, 2.621, 338.52, 1.707),
(4.67, 3.158, 340.09, 1.609),
(4.67, 3.695, 342.55, 1.589),
(4.67, 4.258, 345.53, 1.507)
]

multiplied_by_zero = 0                  #Avoid a * .... = 0
for datapoint in data:
    multiplied_by_zero += datapoint[3] ** 2
multiplied_by_zero /= len(data)

lowest_dev = (10**50, (12, 3, 2.4, 25, 0.8))      #(a,b,c,d,e)

def deviation(datapoint, variables):    #return (measured fmax - calculated fmax)^2
    R25 = (datapoint[0]-variables[1]) ** -1
    R = R25 * (datapoint[2]/300) ** 2.3 + variables[2]
    Fmax = variables[0] / (log(variables[3] * datapoint[1] + variables[4]) * R)
    return (datapoint[3] - Fmax) ** 2

counter = 0
start_time = time()

for resolution_exponent in range(0,8):
    resolution = 1 * 10 ** (-resolution_exponent)
    print(resolution_exponent)
    starting_variables = lowest_dev[1]
    for i in range(-12,13):
        a = starting_variables[0] + i * resolution

        counter += 1
        print(100*counter/24, time() - start_time)

        for i in range(-12,13):
            b = starting_variables[1] + i * resolution / 10

            for i in range(-12,13):
                c = starting_variables[2] + i * resolution / 5
                
                for i in range(-12,13):
                    d = starting_variables[3] + i * resolution
                    if d <= 0: d = 1

                    for i in range(-12,13):
                        e = starting_variables[4] + i * resolution / 2
                        #if e < 0: e = 1

                        R_squared = 0
                        for datapoint in data:
                            R_squared += deviation(datapoint, (a,b,c,d,e))
                        R_squared /= len(data)
                        if R_squared <= lowest_dev[0] and R_squared != multiplied_by_zero:
                            lowest_dev = (R_squared, (a,b,c,d,e))
                            print('lower dev', lowest_dev)
    print('done', lowest_dev)

            